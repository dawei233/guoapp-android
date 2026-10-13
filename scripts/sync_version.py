import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path


PUBSPEC_VERSION = re.compile(r'^version:[ \t]*(\S+)', re.MULTILINE)
README_VERSION = re.compile(r'(当前源码版本：\*\*)([^*\n]+)(\*\*)')


@dataclass(frozen=True)
class VersionSync:
    version: str
    previous: str

    @property
    def changed(self):
        return self.version != self.previous


def read_version(root):
    text = (root / 'pubspec.yaml').read_text(encoding='utf-8')
    match = PUBSPEC_VERSION.search(text)
    if not match:
        raise ValueError('pubspec.yaml 缺少 version 字段')
    return match.group(1)


def render_readme(text, version):
    match = README_VERSION.search(text)
    if not match:
        raise ValueError('README.md 缺少「当前源码版本：**...**」标记')
    return README_VERSION.sub(
        lambda found: found.group(1) + version + found.group(3), text, count=1
    )


def synchronize_version(root, check=False):
    version = read_version(root)
    path = root / 'README.md'
    current = path.read_text(encoding='utf-8')
    updated = render_readme(current, version)
    if updated != current and not check:
        path.write_text(updated, encoding='utf-8')
    return VersionSync(version=version, previous=README_VERSION.search(current).group(2))


def main():
    parser = argparse.ArgumentParser(description='让 README 的当前源码版本号跟随 pubspec.yaml。')
    parser.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument('--check', action='store_true', help='只检查是否一致，不修改文件')
    options = parser.parse_args()
    try:
        result = synchronize_version(options.root.expanduser(), check=options.check)
    except (OSError, ValueError) as error:
        print(str(error), file=sys.stderr)
        return 2
    if options.check:
        if result.changed:
            print(f'README 版本号 {result.previous} 与 pubspec.yaml {result.version} 不一致，'
                  f'请执行 python3 scripts/sync_version.py')
            return 1
        print('README 版本号一致：' + result.version)
        return 0
    if result.changed:
        print(f'已更新 README 版本号：{result.previous} → {result.version}')
    else:
        print('README 版本号无需更新：' + result.version)
    return 0


if __name__ == '__main__':
    raise SystemExit(main())