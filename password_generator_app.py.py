import tkinter as tk
from tkinter import ttk, messagebox
import random
import string

# ------------------ Password Generator Logic ------------------ #
def generate_password(length, strength):
    if strength == "Weak":
        chars = string.ascii_lowercase
    elif strength == "Average":
        chars = string.ascii_letters + string.digits
    elif strength == "Strong":
        chars = string.ascii_letters + string.digits + string.punctuation
    else:
        chars = string.ascii_letters
    return ''.join(random.choice(chars) for _ in range(length))

# ------------------ App Class ------------------ #
class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator - CodSoft Task 3")
        self.root.geometry("400x400")
        self.root.resizable(False, False)

        self.theme = "light"
        self.set_theme()

        self.strength_var = tk.StringVar(value="Strong")
        self.length_var = tk.IntVar(value=12)
        self.password_var = tk.StringVar()

        self.build_ui()

    def set_theme(self):
        if self.theme == "light":
            self.bg_color = "#f5f5f5"
            self.fg_color = "#333333"
            self.btn_color = "#6c63ff"
            self.entry_bg = "white"
        else:
            self.bg_color = "#2c2f33"
            self.fg_color = "white"
            self.btn_color = "#7289da"
            self.entry_bg = "#40444b"
        self.root.configure(bg=self.bg_color)

    def toggle_theme(self):
        self.theme = "dark" if self.theme == "light" else "light"
        self.set_theme()
        self.build_ui()

    def build_ui(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        title = tk.Label(self.root, text="🔐 Password Generator", font=("Helvetica", 18, "bold"), bg=self.bg_color, fg=self.fg_color)
        title.pack(pady=10)

        # Strength Option
        frame1 = tk.Frame(self.root, bg=self.bg_color)
        frame1.pack(pady=10)
        tk.Label(frame1, text="Select Strength:", bg=self.bg_color, fg=self.fg_color).grid(row=0, column=0, padx=5)
        strength_menu = ttk.Combobox(frame1, textvariable=self.strength_var, values=["Weak", "Average", "Strong"], state="readonly", width=10)
        strength_menu.grid(row=0, column=1)

        # Length Slider
        frame2 = tk.Frame(self.root, bg=self.bg_color)
        frame2.pack(pady=10)
        tk.Label(frame2, text="Length:", bg=self.bg_color, fg=self.fg_color).grid(row=0, column=0, padx=5)
        length_slider = tk.Scale(frame2, from_=4, to=32, orient=tk.HORIZONTAL, variable=self.length_var, bg=self.bg_color, fg=self.fg_color)
        length_slider.grid(row=0, column=1)

        # Generate Button
        gen_btn = tk.Button(self.root, text="Generate Password", command=self.on_generate, bg=self.btn_color, fg="white", font=("Helvetica", 12), width=20)
        gen_btn.pack(pady=10)

        # Output Field
        self.output = tk.Entry(self.root, textvariable=self.password_var, font=("Helvetica", 14), justify="center", bg=self.entry_bg, fg=self.fg_color, relief=tk.FLAT)
        self.output.pack(pady=10, ipadx=6, ipady=6, padx=20, fill="x")

        # Copy & Theme Buttons
        frame3 = tk.Frame(self.root, bg=self.bg_color)
        frame3.pack(pady=10)

        copy_btn = tk.Button(frame3, text="Copy", command=self.copy_password, bg="#43b581", fg="white", width=10)
        copy_btn.grid(row=0, column=0, padx=10)

        theme_btn = tk.Button(frame3, text="Toggle Theme", command=self.toggle_theme, bg="#faa61a", fg="white", width=15)
        theme_btn.grid(row=0, column=1, padx=10)

    def on_generate(self):
        length = self.length_var.get()
        strength = self.strength_var.get()
        if length < 4:
            messagebox.showwarning("Too Short", "Password length must be at least 4 characters.")
            return
        password = generate_password(length, strength)
        self.password_var.set(password)

    def copy_password(self):
        password = self.password_var.get()
        if password:
            self.root.clipboard_clear()
            self.root.clipboard_append(password)
            messagebox.showinfo("Copied", "Password copied to clipboard!")

# ------------------ Run App ------------------ #
if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()
