# 第三方组件许可说明

本项目的 Android 产物打包了以下第三方组件。各组件的版权归其各自作者所有，
本项目对这些组件的使用遵循其原始许可证。

**注意**：本仓库自身未声明许可证（见 `NOTICE`）。以下声明只覆盖**第三方组件**，
不构成对本项目自身源码的授权。

---

## 一、GPL 组件（重要）

### FFmpegKit min-gpl

| 项 | 值 |
|---|---|
| 包名 | `ffmpeg_kit_flutter_new_min_gpl` |
| 版本 | 2.6.2 |
| 插件许可 | LGPL-3.0 |
| **打包后整体许可** | **GPL-3.0** |
| 项目地址 | https://github.com/sk3llo/ffmpeg_kit_flutter |

该包为 **min-gpl 变体**，除 FFmpeg 基础库外还包含 **GPL 授权的编解码器**：
`x264`、`x265`、`xvidcore`、`vid.stab`。

上游说明原文：

> The plugin is licensed under LGPL 3.0. This package also includes GPL 3.0
> components (`x264`, `x265`, `xvidcore`, `vid.stab`), so an application that
> uses it is distributed under GPL 3.0.

**因此：本项目的 Android 产物的媒体处理部分受 GPL-3.0 约束。**
重新分发 APK 时须遵守 GPL-3.0，包括提供**完整对应源码**的义务。

产物中实际包含的 FFmpeg 动态库（从 APK 中确认）：

```
lib/<abi>/libffmpegkit.so
lib/<abi>/libffmpegkit_abidetect.so
lib/<abi>/libavcodec.so
lib/<abi>/libavdevice.so
lib/<abi>/libavfilter.so
lib/<abi>/libavformat.so
lib/<abi>/libavutil.so
lib/<abi>/libswresample.so
lib/<abi>/libswscale.so
```

FFmpegKit 只用于合并与导出，**不参与**正常播放或下载的转码。

> **对应源码说明**：上游 FFmpegKit 的完整对应源码可在其项目地址按其发布说明获取。
> 若你重新分发本项目的 APK，须自行确保满足 GPL 的对应源码提供要求。

### libmpv / media_kit

| 项 | 值 |
|---|---|
| 包名 | `media_kit` 1.2.6 / `media_kit_video` 2.0.1 / `media_kit_libs_video` 1.0.7 |
| 许可 | MIT（Dart 层） |
| 项目地址 | https://github.com/media-kit/media-kit |

media_kit 的 Dart 层为 MIT。其捆绑的 **libmpv** 原生库由 mpv 项目提供，
许可为 **LGPL-2.1-or-later**（默认构建，未启用 GPL-only 组件）。
产物中的 `lib/<abi>/libmpv.so` 即来自该路径。

> libmpv 采用 LGPL，动态链接方式下不影响本项目自有代码的许可选择，
> 但重新分发时须保留其许可声明并允许替换该库。

---

## 二、MIT / BSD 组件

| 组件 | 版本 | 许可 | 项目地址 |
|---|---|---|---|
| media_kit | 1.2.6 | MIT | https://github.com/media-kit/media-kit |
| media_kit_video | 2.0.1 | MIT | https://github.com/media-kit/media-kit |
| media_kit_libs_video | 1.0.7 | MIT | https://github.com/media-kit/media-kit |
| flutter_foreground_task | 11.0.3 | MIT | https://github.com/Dev-hwang/flutter_foreground_task |
| file_picker | 13.1.0 | MIT | https://github.com/miguelpruivo/flutter_file_picker |
| nsd | 5.0.1 | MIT | https://github.com/sebastianhaberey/nsd |

`file_picker` 与 `nsd` 的许可文本以 MIT 为准（`Copyright (c) 2018 Miguel Ruivo`、
`Copyright (c) 2021 Sebastian Haberey and others`）。

## 三、BSD 类组件（Flutter / Dart 官方与社区）

以下组件采用 BSD-3-Clause 或同等的 BSD 类许可，
版权归 Flutter Authors 或 Dart project authors：

| 组件 | 版本 | 许可 |
|---|---|---|
| video_player | 2.14.1 | BSD-3-Clause (The Flutter Authors) |
| path_provider | 2.1.6 | BSD-3-Clause (The Flutter Authors) |
| shared_preferences | 2.5.5 | BSD-3-Clause (The Flutter Authors) |
| crypto | 3.0.7 | BSD-3-Clause (Dart project authors) |
| ffi | 2.2.0 | BSD-3-Clause (Dart project authors) |
| path | 1.9.1 | BSD-3-Clause (Dart project authors) |

Flutter 框架本身（含 `libflutter.so`、`libapp.so`）采用 BSD-3-Clause，
其完整许可文本已随构建产物打入 `assets/flutter_assets/NOTICES.Z`。

---

## 四、其它随产物分发的许可文本

APK 中已包含以下许可文件：

```
assets/flutter_assets/NOTICES.Z                       # Flutter 自动汇总的全部 Dart 依赖许可
assets/flutter_assets/assets/video_enhancement/Anime4K-LICENSE.txt
META-INF/androidx/**/LICENSE.txt                       # AndroidX 组件
```

Anime4K 着色器许可见上表所列文件（随产物分发的 `Anime4K-LICENSE.txt`）。

---

## 五、剧集内容与版权（非软件许可）

开源许可只适用于**软件**，不授予任何剧集内容的再分发权：

1. 安装包**不包含**任何剧集媒体；所有视频、封面与元数据均来自第三方站点。
2. 作品版权归原平台及创作者所有。
3. 请仅处理你有权访问、下载或备份的内容，遵守平台条款与相关法律。
4. 平台接口可能调整，某次可用**不保证**持续可用。
