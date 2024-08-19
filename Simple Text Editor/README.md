# Simple Text Editor

This is a Python-based simple text editor with a graphical user interface (GUI) created using Tkinter. The editor allows you to create, edit, save, and open text files. It also includes basic text editing features like cut, copy, paste, undo, redo, and font customization.

## Features

- **Create New File:** Start a new document.
- **Open Existing File:** Open an existing `.txt` file.
- **Save File:** Save the current file.
- **Save As:** Save the current file with a new name or location.
- **Cut/Copy/Paste:** Standard text editing operations.
- **Undo/Redo:** Undo or redo recent changes.
- **Font Customization:** Change the font family, size, and style (bold/italic).

## Installation

1. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the text editor:
   ```bash
   python project.py
   ```

## Testing

The project includes unit tests to verify its functionality using `pytest`.

To run the tests, use:
```bash
python -m pytest test_project.py
```

## File Structure

- **project.py:** The main script containing the text editor implementation.
- **test_project.py:** Unit tests for the text editor.
- **requirements.txt:** The dependencies for the project.

## Requirements

- Python 3.x
- Tkinter
- Pytest

## Usage

- Open the text editor and use the menu options to create, open, save, or edit text files.
- Use the Edit menu to perform text operations like cut, copy, paste, undo, and redo.
- Customize the font using the Font option under the Edit menu.

## Video Demo

[Simple Text Editor](https://youtu.be/iYCDvH2e4Zo)

## License

This project is licensed under the MIT License. See the [LICENSE](https://github.com/muhammadhuzaifayousaf/CS50_Python/blob/main/LICENSE) file for details.
