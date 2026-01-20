# python-sdbus-modemmanager

## ModemManager binds for python-sdbus

Supports both asyncio (under `sdbus_async.ModemManager` module) and blocking (under `sdbus_block.ModemManager` module)

Implements most ModemManager dbus interfaces and objects.

## Requirements

`python-sdbus` version higher than 0.8rc2
See [python-sdbus requirements](https://github.com/igo95862/python-sdbus#requirements).

## Installation

`pip install --only-binary ':all:' sdbus-ModemManager`

## Documentation

This is the sub-project of [python-sdbus](https://github.com/igo95862/python-sdbus).

See the [python-sdbus documentation](https://python-sdbus.readthedocs.io/en/latest/).

## Format

Use YAPF in command line:

```
yapf --style="{use_tabs: true, indent_width: 4, column_limit:180, continuation_align_style: 'valign-right'}" --in-place <filename.py>
```

## packaging

This project uses [Poetry](https://python-poetry.org/) for packaging and dependency management.

```shell
poetry publish --build
```

## Changelog

See [changelog.md](changelog.md).
