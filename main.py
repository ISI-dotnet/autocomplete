

from nltk.corpus import words
import tkinter as tk
from tkinter import messagebox
import nltk
nltk.download('words')


class AutocompleteTextbox:
    def __init__(self, root):
        self.root = root
        # Using NLTK's words corpus as the word list
        self.words = set(words.words())

        self.entry = tk.Entry(root)
        self.entry.pack()
        self.entry.bind("<Tab>", self.autocomplete)

    def autocomplete(self, event):
        current_text = self.entry.get()
        word_to_complete = self.get_word_to_complete(current_text)

        if word_to_complete:
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, word_to_complete)
        else:
            messagebox.showinfo("Autocomplete", "No suggestion available")

    def get_word_to_complete(self, current_text):
        for word in self.words:
            if word.startswith(current_text):
                return word
        return None


def main():
    root = tk.Tk()
    root.title("Autocomplete Textbox")
    app = AutocompleteTextbox(root)
    root.mainloop()


if __name__ == "__main__":
    main()
