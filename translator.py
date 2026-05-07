import tkinter as tk
from tkinter import ttk, messagebox
from deep_translator import GoogleTranslator

class LanguageTranslatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("CodeAlpha - AI Language Translation Tool")
        self.root.geometry("550x550")
        self.root.configure(bg="#f0f2f5")

        # Language Dictionary (Full Name: Code)
        self.languages = {
            'English': 'en', 'Spanish': 'es', 'French': 'fr', 'German': 'de', 
            'Hindi': 'hi', 'Arabic': 'ar', 'Japanese': 'ja', 'Russian': 'ru'
        }

        # Title
        tk.Label(root, text="AI Language Translator", font=("Arial", 18, "bold"), bg="#f0f2f5", fg="#1c1e21").pack(pady=20)

        # Source Language
        tk.Label(root, text="From:", bg="#f0f2f5", font=("Arial", 10, "bold")).pack(anchor="w", padx=50)
        self.src_lang = ttk.Combobox(root, values=list(self.languages.keys()), state="readonly", width=40)
        self.src_lang.current(0) 
        self.src_lang.pack(pady=5)

        # Target Language
        tk.Label(root, text="To:", bg="#f0f2f5", font=("Arial", 10, "bold")).pack(anchor="w", padx=50)
        self.dest_lang = ttk.Combobox(root, values=list(self.languages.keys()), state="readonly", width=40)
        self.dest_lang.current(1) 
        self.dest_lang.pack(pady=5)

        # Input Text
        tk.Label(root, text="Enter Text:", bg="#f0f2f5", font=("Arial", 10, "bold")).pack(anchor="w", padx=50)
        self.input_area = tk.Text(root, height=5, width=50, font=("Arial", 10))
        self.input_area.pack(pady=5)

        # Buttons
        btn_frame = tk.Frame(root, bg="#f0f2f5")
        btn_frame.pack(pady=15)

        tk.Button(btn_frame, text="Translate", command=self.translate_text, bg="#007bff", fg="white", font=("Arial", 10, "bold"), width=15).grid(row=0, column=0, padx=10)
        tk.Button(btn_frame, text="Clear", command=self.clear_all, bg="#6c757d", fg="white", font=("Arial", 10, "bold"), width=15).grid(row=0, column=1, padx=10)

        # Output Text
        tk.Label(root, text="Translation:", bg="#f0f2f5", font=("Arial", 10, "bold")).pack(anchor="w", padx=50)
        self.output_area = tk.Text(root, height=5, width=50, font=("Arial", 10), bg="#e9ecef")
        self.output_area.pack(pady=5)

    def translate_text(self):
        text = self.input_area.get("1.0", tk.END).strip()
        if not text:
            messagebox.showwarning("Empty Input", "Please type something to translate!")
            return

        try:
            source = self.languages[self.src_lang.get()]
            target = self.languages[self.dest_lang.get()]
            
            # Use deep-translator
            result = GoogleTranslator(source=source, target=target).translate(text)
            
            self.output_area.delete("1.0", tk.END)
            self.output_area.insert(tk.END, result)
        except Exception as e:
            messagebox.showerror("Error", f"Something went wrong: {e}")

    def clear_all(self):
        self.input_area.delete("1.0", tk.END)
        self.output_area.delete("1.0", tk.END)

if __name__ == "__main__":
    window = tk.Tk()
    app = LanguageTranslatorApp(window)
    window.mainloop()