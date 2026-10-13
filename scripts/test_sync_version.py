import tempfile
import unittest
from pathlib import Path

from sync_version import read_version, render_readme, synchronize_version


class VersionSyncTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory(prefix='duanju-version-test-')
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        self.write('pubspec.yaml', 'name: synthetic_app\nversion: 0.4.1+7\n')
        self.write('README.md', '说明。当前源码版本：**0.4.0+6**。结尾。\n')

    def write(self, name, content):
        path = self.root / name
        path.write_text(content, encoding='utf-8')

    def read(self, name):
        return (self.root / name).read_text(encoding='utf-8')

    def test_reads_version_from_pubspec(self):
        self.assertEqual(read_version(self.root), '0.4.1+7')

    def test_readme_is_updated_to_match_pubspec(self):
        result = synchronize_version(self.root)
        self.assertTrue(result.changed)
        self.assertEqual(result.previous, '0.4.0+6')
        self.assertEqual(result.version, '0.4.1+7')
        self.assertIn('当前源码版本：**0.4.1+7**', self.read('README.md'))

    def test_surrounding_text_is_preserved(self):
        synchronize_version(self.root)
        self.assertEqual(self.read('README.md'), '说明。当前源码版本：**0.4.1+7**。结尾。\n')

    def test_check_reports_mismatch_without_writing(self):
        result = synchronize_version(self.root, check=True)
        self.assertTrue(result.changed)
        self.assertIn('**0.4.0+6**', self.read('README.md'))

    def test_check_passes_when_already_aligned(self):
        self.write('README.md', '说明。当前源码版本：**0.4.1+7**。\n')
        result = synchronize_version(self.root, check=True)
        self.assertFalse(result.changed)
        self.assertEqual(result.version, '0.4.1+7')

    def test_repeated_runs_are_stable(self):
        synchronize_version(self.root)
        first = self.read('README.md')
        self.assertFalse(synchronize_version(self.root).changed)
        self.assertEqual(self.read('README.md'), first)

    def test_render_readme_replaces_only_the_marker(self):
        text = '版本：**1.0.0+1** 与再次出现的 1.0.0+1 字面量\n'
        rendered = render_readme('当前源码版本：**1.0.0+1**' + text, '2.0.0+2')
        self.assertEqual(rendered, '当前源码版本：**2.0.0+2**' + text)

    def test_missing_marker_is_reported(self):
        self.write('README.md', '没有任何版本标记。\n')
        with self.assertRaises(ValueError):
            synchronize_version(self.root)

    def test_missing_pubspec_version_is_reported(self):
        self.write('pubspec.yaml', 'name: synthetic_app\n')
        with self.assertRaises(ValueError):
            synchronize_version(self.root)


if __name__ == '__main__':
    unittest.main()