# accesskit

> 用 C++23 模块使用 AccessKit 的 C 绑定：一棵无障碍树，交给各平台的辅助技术。

[English](README.md) · **简体中文** · [上游](https://github.com/AccessKit/accesskit-c) · [发布](https://github.com/mcpplibs/accesskit-m/releases) · [mcpp](https://github.com/mcpp-community/mcpp) · [索引](https://github.com/mcpplibs/mcpp-index)

[![C++23](https://img.shields.io/badge/C%2B%2B-23-blue.svg)](https://en.cppreference.com/w/cpp/23)
[![License](https://img.shields.io/badge/license-Apache--2.0-blue.svg)](LICENSE)
[![mcpp-community](https://img.shields.io/badge/mcpp--community-mwrap-blue)](https://github.com/mcpp-community)
[![CI](https://github.com/mcpplibs/accesskit-m/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/mcpplibs/accesskit-m/actions/workflows/ci.yml)

`mcpplibs.mwrap.accesskit` 0.23.1 原样导出 `<accesskit.h>` 的全部公开名字：
`accesskit_node_new`、`ACCESSKIT_ROLE_BUTTON`、`accesskit_tree_update_push_node`，
以及各平台的适配器（Linux 的 `accesskit_unix_adapter_*`、Windows 的
`accesskit_windows_subclassing_adapter_*`、macOS 的
`accesskit_macos_subclassing_adapter_*`），条件与头文件一致。界面建好节点树，
AccessKit 把它交给 UI Automation、NSAccessibility 或 AT-SPI，并把读屏器、语音控制
的请求交回来。

库本身是 `compat.accesskit` 0.23.1：上游预编译的静态库（用 Rust 写成），支持
Linux x86_64、macOS arm64、Windows x86_64。

## 开始

```sh
mcpp new hello --template mcpplibs.mwrap.accesskit@0.23.1
cd hello
mcpp run
```

## 模块

`src/accesskit.cppm` 由 `tools/gen_module.py` 从头文件生成（CI 会检查是否最新）：
函数、结构、typedef、枚举和每个枚举值，不改名，不添加。头文件没有需要映射的宏。

## 许可

封装部分为 Apache-2.0（[LICENSE](LICENSE)）；AccessKit 为 MIT 或 Apache-2.0
（[upstream/LICENSE-MIT](upstream/LICENSE-MIT)、[upstream/LICENSE-APACHE](upstream/LICENSE-APACHE)）。见 [NOTICE](NOTICE)。
