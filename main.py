import tkinter as tk
from tkinter import messagebox
from nltk.corpus import words
import nltk
nltk.download("words")


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
        words_list = current_text.split()  # Split input into individual words
        if len(words_list) >= 1:
            # Get the last word for autocompletion
            last_word_to_complete = words_list[-1]
            suggestions = self.get_word_suggestions(last_word_to_complete)
            if suggestions:
                suggested_word = suggestions[0]  # Use the first suggestion
                completed_text = " ".join(words_list[:-1] + [suggested_word])
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, completed_text)
            else:
                messagebox.showinfo("Autocomplete", "No suggestion available")
            return 'break'

    def get_word_suggestions(self, current_text):
        return [word for word in self.words if word.startswith(current_text.lower())]


def main():
    root = tk.Tk()
    root.title("Autocomplete Textbox")
    app = AutocompleteTextbox(root)
    root.mainloop()


if __name__ == "__main__":
    main()
