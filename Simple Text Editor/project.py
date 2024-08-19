import tkinter as tk
from tkinter import filedialog, messagebox, font
import os


def main():
    root = tk.Tk()
    editor = TextEditor(root)
    root.mainloop()


class TextEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Text Editor")
        self.root.geometry("800x600")

        self.text_area = tk.Text(self.root, wrap="word", undo=True)
        self.text_area.pack(fill=tk.BOTH, expand=1)
        self.file_path = None

        self._create_menu()
        self._default_font = font.Font(family="Arial", size=12)

    def _create_menu(self):
        menu_bar = tk.Menu(self.root)
        self.root.config(menu=menu_bar)

        # File Menu
        file_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="New", command=self.new_file)
        file_menu.add_command(label="Open", command=self.open_file)
        file_menu.add_command(label="Save", command=self.save_file)
        file_menu.add_command(label="Save As", command=self.save_as)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.root.quit)

        # Edit Menu
        edit_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Edit", menu=edit_menu)
        edit_menu.add_command(label="Cut", command=self.cut)
        edit_menu.add_command(label="Copy", command=self.copy)
        edit_menu.add_command(label="Paste", command=self.paste)
        edit_menu.add_separator()
        edit_menu.add_command(label="Undo", command=self.text_area.edit_undo)
        edit_menu.add_command(label="Redo", command=self.text_area.edit_redo)
        edit_menu.add_separator()
        edit_menu.add_command(label="Font", command=self.choose_font)

    def new_file(self):
        try:
            self.text_area.delete(1.0, tk.END)
            self.file_path = None
            messagebox.showinfo("Success", "New file created successfully!")
        except Exception as e:
            print(f"Error: {e}")

    def open_file(self):
        try:
            self.file_path = filedialog.askopenfilename(defaultextension=".txt", filetypes=[
                                                        ("Text files", "*.txt"), ("All files", "*.*")])
            if self.file_path:
                with open(self.file_path, "r") as file:
                    self.text_area.delete(1.0, tk.END)
                    self.text_area.insert(1.0, file.read())
                messagebox.showinfo("Success", "File opened successfully!")
        except Exception as e:
            print(f"Error: {e}")

    def save_file(self):
        try:
            if self.file_path:
                with open(self.file_path, "w") as file:
                    file.write(self.text_area.get(1.0, tk.END))
                messagebox.showinfo("Success", "File saved successfully!")
            else:
                self.save_as()
        except Exception as e:
            print(f"Error: {e}")

    def save_as(self):
        try:
            self.file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[
                                                          ("Text files", "*.txt"), ("All files", "*.*")])
            if self.file_path:
                with open(self.file_path, "w") as file:
                    file.write(self.text_area.get(1.0, tk.END))
                messagebox.showinfo("Success", "File saved successfully!")
        except Exception as e:
            print(f"Error: {e}")

    def cut(self):
        try:
            self.text_area.event_generate("<<Cut>>")
        except Exception as e:
            print(f"Error: {e}")

    def copy(self):
        try:
            self.text_area.event_generate("<<Copy>>")
        except Exception as e:
            print(f"Error: {e}")

    def paste(self):
        try:
            self.text_area.event_generate("<<Paste>>")
        except Exception as e:
            print(f"Error: {e}")

    def choose_font(self):
        try:
            font_window = tk.Toplevel(self.root)
            font_window.title("Font Settings")
            font_window.geometry("350x200")
            font_window.resizable(False, False)

            # Grid layout with padding
            font_window.columnconfigure(1, weight=1)
            font_window.rowconfigure([0, 1, 2, 3], pad=10)

            # Font Family
            tk.Label(font_window, text="Family:", anchor="e").grid(
                row=0, column=0, sticky="e", padx=10)
            font_family = tk.StringVar(value="Arial")
            font_family_list = tk.OptionMenu(font_window, font_family, *font.families())
            font_family_list.grid(row=0, column=1, sticky="w", padx=10)

            # Font Size
            tk.Label(font_window, text="Size:", anchor="e").grid(
                row=1, column=0, sticky="e", padx=10)
            font_size = tk.StringVar(value="12")
            tk.Entry(font_window, textvariable=font_size, width=10).grid(
                row=1, column=1, sticky="w", padx=10)

            # Font Style (Bold/Italic)
            tk.Label(font_window, text="Style:", anchor="e").grid(
                row=2, column=0, sticky="e", padx=10)
            font_style = tk.StringVar(value="normal")
            style_options = tk.OptionMenu(font_window, font_style,
                                          "normal", "bold", "italic", "bold italic")
            style_options.grid(row=2, column=1, sticky="w", padx=10)

            # Apply button centered
            tk.Button(font_window, text="Apply", command=lambda: self._apply_font(font_family.get(
            ), font_size.get(), font_style.get(), font_window)).grid(row=3, column=0, columnspan=2, pady=10)
        except Exception as e:
            print(f"Error: {e}")

    def _apply_font(self, family, size, style, font_window):
        try:
            # Map the style to font properties
            weight = "bold" if "bold" in style else "normal"
            slant = "italic" if "italic" in style else "roman"

            # Update the text area's font
            new_font = font.Font(family=family, size=int(size), weight=weight, slant=slant)
            self.text_area.config(font=new_font)

            # Close the font window
            font_window.destroy()

            messagebox.showinfo("Success", "Font applied successfully!")
        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()
