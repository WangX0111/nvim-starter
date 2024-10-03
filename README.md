# Neovim Starter

A Python-based Neovim starter project that allows you to select and configure Neovim modules using lazy.nvim. This script helps you generate a configuration file based on the selected modules.

## Features

- Display a list of available Neovim modules.
- Allow users to select the desired modules.
- Generate a configuration file (`generated_config.lua`).
- Option to generate a full `init.lua` file.

## Prerequisites

- Neovim
- Python 3.x
- pynvim

## Installation

1. **Install Neovim**: Follow the [official installation guide](https://github.com/neovim/neovim/wiki/Installing-Neovim) to install Neovim on your system.

2. **Install Python and pynvim**:
    ```sh
    pip install pynvim
    ```

3. **Clone this repository**:
    ```sh
    git clone https://github.com/yourusername/neovim-starter.git
    cd neovim-starter
    ```

4. **Install lazy.nvim**:
    ```sh
    git clone https://github.com/folke/lazy.nvim.git ~/.config/nvim/lazy
    ```

## Usage

### Running the Script

To run the script and generate the configuration file, use the following command:

```sh
python your_script.py
```

### Generating a Full init.lua

FileIf you want to generate a full init.lua file, use the --full-init option:

```sh
python your_script.py --full-init
```

### Selecting Modules

After running the script, you will be prompted to select the desired modules from the list. Enter the module numbers separated by commas or type done when you are finished.

### Example

```sh
python your_script.py
```

Output:

```
Available Neovim Modules:
1. nvim-telescope/telescope.nvim
2. nvim-treesitter/nvim-treesitter
Enter the module number to select (or 'done' to finish): 1
Enter the module number to select (or 'done' to finish): 2
Enter the module number to select (or 'done' to finish): done
Configuration file generated: generated_config.lua
```

Generated:
```sh
-- Generated Neovim configuration
require("lazy").setup({
  {'nvim-telescope/telescope.nvim'},
  {'nvim-treesitter/nvim-treesitter'},
})
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request or open an issue to discuss improvements or new features.