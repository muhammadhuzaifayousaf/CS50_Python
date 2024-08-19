import pytest
from tkinter import Tk
from tkinter import messagebox
from project import TextEditor


@pytest.fixture
def text_editor():
    root = Tk()
    editor = TextEditor(root)
    return editor


def test_new_file(text_editor, monkeypatch):
    monkeypatch.setattr(messagebox, 'showinfo', lambda *args, **kwargs: None)
    text_editor.new_file()
    assert text_editor.file_path is None
    assert text_editor.text_area.get(1.0, "end-1c") == ""


def test_open_file(text_editor, monkeypatch, tmp_path):
    file_path = tmp_path / "sample.txt"
    file_path.write_text("Hello, World!")

    monkeypatch.setattr('tkinter.filedialog.askopenfilename',
                        lambda *args, **kwargs: str(file_path))
    monkeypatch.setattr(messagebox, 'showinfo', lambda *args, **kwargs: None)

    text_editor.open_file()
    assert text_editor.text_area.get(1.0, "end-1c") == "Hello, World!"


def test_save_file(text_editor, monkeypatch, tmp_path):
    file_path = tmp_path / "test_save.txt"

    monkeypatch.setattr('tkinter.filedialog.asksaveasfilename',
                        lambda *args, **kwargs: str(file_path))
    monkeypatch.setattr(messagebox, 'showinfo', lambda *args, **kwargs: None)

    text_editor.text_area.insert(1.0, "Test Save Content")
    text_editor.save_as()

    with open(file_path, "r") as file:
        content = file.read().strip()

    assert content == "Test Save Content"


def test_cut_copy_paste(text_editor, monkeypatch):
    text_editor.text_area.insert(1.0, "Hello")
    text_editor.text_area.tag_add("sel", "1.0", "1.5")
    text_editor.copy()
    text_editor.cut()
    text_editor.paste()

    assert text_editor.text_area.get(1.0, "end-1c") == "Hello"
