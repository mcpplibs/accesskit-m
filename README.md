# accesskit

> AccessKit's C bindings through a C++23 module: one accessibility tree, served to every platform's assistive technology.

**English** · [简体中文](README.zh.md) · [Upstream](https://github.com/AccessKit/accesskit-c) · [Releases](https://github.com/mcpplibs/accesskit-m/releases) · [mcpp](https://github.com/mcpp-community/mcpp) · [Index](https://github.com/mcpplibs/mcpp-index)

[![C++23](https://img.shields.io/badge/C%2B%2B-23-blue.svg)](https://en.cppreference.com/w/cpp/23)
[![License](https://img.shields.io/badge/license-Apache--2.0-blue.svg)](LICENSE)
[![mcpp-community](https://img.shields.io/badge/mcpp--community-mwrap-blue)](https://github.com/mcpp-community)
[![CI](https://github.com/mcpplibs/accesskit-m/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/mcpplibs/accesskit-m/actions/workflows/ci.yml)

`mcpplibs.mwrap.accesskit` 0.23.1 exports every public name of `<accesskit.h>`
unchanged: `accesskit_node_new`, `ACCESSKIT_ROLE_BUTTON`,
`accesskit_tree_update_push_node`, the platform adapters
(`accesskit_unix_adapter_*` on Linux, `accesskit_windows_subclassing_adapter_*`
on Windows, `accesskit_macos_subclassing_adapter_*` on macOS) under the same
conditions the header declares them. A UI builds its tree of nodes and AccessKit
serves it to UI Automation, NSAccessibility or AT-SPI, and hands back what a
screen reader or voice control asks of it.

The library itself is `compat.accesskit` 0.23.1: upstream's prebuilt static
library (it is Rust) for Linux x86_64, macOS arm64 and Windows x86_64.

## Getting started

```sh
mcpp new hello --template mcpplibs.mwrap.accesskit@0.23.1.1
cd hello
mcpp run
```

```cpp
import std;
import mcpplibs.mwrap.accesskit;

int main() {
    accesskit_node* window = accesskit_node_new(ACCESSKIT_ROLE_WINDOW);
    accesskit_node_set_label(window, "Settings");
    accesskit_tree_update* update = accesskit_tree_update_with_focus(1);
    accesskit_tree_update_set_tree_info(update, accesskit_tree_info_new(1));
    accesskit_tree_update_push_node(update, 1, window);
    char* debug = accesskit_tree_update_debug(update);
    std::println("{}", debug);
    accesskit_string_free(debug);
    accesskit_tree_update_free(update);
}
```

## The module

`src/accesskit.cppm` is generated from the header by `tools/gen_module.py`
(CI checks it is current): functions, structs, typedefs, enums and every
enumerator, nothing renamed, nothing added. The header has no macros to map.

## License

The wrapper is Apache-2.0 ([LICENSE](LICENSE)); AccessKit is MIT or
Apache-2.0 ([upstream/LICENSE-MIT](upstream/LICENSE-MIT),
[upstream/LICENSE-APACHE](upstream/LICENSE-APACHE)). See [NOTICE](NOTICE).
