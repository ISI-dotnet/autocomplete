import tkinter as tk
from tkinter import messagebox
from nltk.corpus import words
import nltk
nltk.download("words")


class AutocompleteTextbox:
    def __init__(self, root):
        self.root = root
        self.words = set(words.words())
        
        self.text_area = tk.Text(root, wrap='word', height=30, width=160, font=("Arial", 12))
        self.text_area.pack()
        self.text_area.bind("<KeyRelease>", self.autocomplete)
        self.text_area.bind("<Tab>", self.apply_suggestion)

        self.suggestion_listbox = tk.Listbox(root, width=160, height=3, font=("Arial", 12))
        self.suggestion_listbox.pack()
        self.suggestion_listbox.bind("<Double-Button-1>", self.on_select)
        self.suggestion_listbox.bind("<Return>", self.apply_suggestion)

    def autocomplete(self, event):
        current_text = self.text_area.get("1.0", tk.END)[:-1]  # Get text content
        words_list = current_text.split()  # Split input into individual words
        if len(words_list) >= 1:
            last_word_to_complete = words_list[-1]
            suggestions = self.get_word_suggestions(last_word_to_complete)[:3]  # Limit to 3 suggestions
            self.update_suggestions(suggestions)

    def get_word_suggestions(self, current_text):
        return [word for word in self.words if word.startswith(current_text.lower())]

    def update_suggestions(self, suggestions):
        self.suggestion_listbox.delete(0, tk.END)
        for suggestion in suggestions:
            self.suggestion_listbox.insert(tk.END, suggestion)

    def apply_suggestion(self, event):
        selected_word = self.suggestion_listbox.get(0)
        if selected_word:
            current_text = self.text_area.get("1.0", tk.END)[:-1]  # Get text content
            words_list = current_text.split()
            if len(words_list) >= 1:
                last_word_index = current_text.rfind(words_list[-1])
                updated_text = current_text[:last_word_index] + selected_word
                self.text_area.delete("1.0", tk.END)  # Clear existing text
                self.text_area.insert(tk.END, updated_text)
                return 'break'  # Prevent default behavior

    def on_select(self, event):
        selected_word = self.suggestion_listbox.get(0)
        if selected_word:
            current_text = self.text_area.get("1.0", tk.END)[:-1]  # Get text content
            words_list = current_text.split()
            if len(words_list) >= 1:
                last_word_index = current_text.rfind(words_list[-1])
                updated_text = current_text[:last_word_index] + selected_word
                self.text_area.delete("1.0", tk.END)  # Clear existing text
                self.text_area.insert(tk.END, updated_text)

def main():
    root = tk.Tk()
    root.title("Autocomplete Text Area")
    app = AutocompleteTextbox(root)
    root.mainloop()

if __name__ == "__main__":
    main()
