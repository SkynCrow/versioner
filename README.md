# pkg_versionator

## Overview

`pkg_versionator` is a Python package designed to serve as a CI/CD base for other projects. It provides a set of command-line interface (CLI) commands that can be easily configured and extended for various deployment and saving tasks.

## Features

- Cross-platform compatibility
- Easily configurable for different projects
- Command-line commands for deployment and saving tasks

## Installation

To install `pkg_versionator`, you can use pip:

```bash
pip install pkg_versionator
```

## Usage

### Command-Line Interface

The package provides the following commands:

- **deploy**: Executes deployment tasks.
- **save**: Handles saving tasks.

You can run the commands from the terminal as follows:

```bash
deploy
save
```

### Configuration

You can customize the behavior of the commands by modifying the respective command files located in the `pkg_versionator/commands` directory. Each command can call external scripts or console commands as needed.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.