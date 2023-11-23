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
        self.text = tk.Text(root, wrap='word', height=30,
                            width=160, font=("Arial", 12))  # Setting height and width
        self.text.pack()
        self.text.bind("<Tab>", self.autocomplete)

    def autocomplete(self, event):
        current_text = self.text.get("1.0", tk.END)[:-1]  # Get text content
        words_list = current_text.split()  # Split input into individual words
        if len(words_list) >= 1:
            # Get the last word for autocompletion
            last_word_to_complete = words_list[-1]
            suggestions = self.get_word_suggestions(last_word_to_complete)
            if suggestions:
                suggested_word = suggestions[0]  # Use the first suggestion
                # Check if the original word starts with a capital letter
                if last_word_to_complete and last_word_to_complete[0].isupper():
                    suggested_word = suggested_word.capitalize()  # Capitalize the suggested word
                completed_text = " ".join(words_list[:-1] + [suggested_word])
                self.text.delete("1.0", tk.END)  # Clear existing text
                self.text.insert(tk.END, completed_text)
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
