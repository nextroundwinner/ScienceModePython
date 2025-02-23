# ScienceModePython

## Introduction

Python implementation of ScienceMode 4 protocol (https://github.com/ScienceMode/ScienceMode4_P24)

## Requirements

Python 3.11 or higher

## Installation

Coming soon

## Dependencies

- PySerial
  - https://pypi.org/project/pyserial/
  - `pip install pyserial`
- Keyboard (only for examples)
  - https://pypi.org/project/keyboard/
  - `pip install keyboard`

## Build library

- Install dependencies
  - `python -m pip install --upgrade build`
- Build project
  - `python -m build`
- Install local library
  - `pip install .\dist\science_mode_4-0.0.0-py3-none-any.whl --force-reinstall`
