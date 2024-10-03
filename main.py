import pynvim
import os
import argparse

# init pynvim
nvim = pynvim.attach('child', argv=["nvim", "--embed"])

# all supported nvim plugins
modules = [
    'nvim-telescope/telescope.nvim',
    'nvim-treesitter/nvim-treesitter',
    # add more
]


def display_modules():
    print("Available Neovim Modules:")
    for i, module in enumerate(modules, 1):
        print(f"{i}. {module}")


def get_user_selection():
    selected_modules = []
    while True:
        choice = input("Enter the module number to select (or 'done' to finish): ")
        if choice.lower() == 'done':
            break
        try:
            idx = int(choice) - 1
            if 0 <= idx < len(modules):
                selected_modules.append(modules[idx])
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number or 'done'.")
    return selected_modules


def generate_config(selected_modules, generate_full_init):
    config_lines = [
        '-- Generated Neovim configuration',
        'require("lazy").setup({'
    ]
    for module in selected_modules:
        config_lines.append(f"  {{'{module}'}},")
    config_lines.append('})')

    if generate_full_init:
        init_lines = [
            '-- Full init.lua configuration',
            'vim.g.mapleader = " "',  # Set the leader key to space
            'require("generated_config")'
        ]
        config_lines = init_lines + config_lines

    with open('generated_config.lua', 'w') as config_file:
        config_file.write('\n'.join(config_lines))
    print('Configuration file generated: generated_config.lua')


def main():
    parser = argparse.ArgumentParser(description='Generate Neovim configuration')
    parser.add_argument('--full-init', action='store_true', help='Generate a full init.lua file')
    args = parser.parse_args()

    display_modules()
    selected_modules = get_user_selection()
    generate_config(selected_modules, args.full_init)


if __name__ == "__main__":
    main()
