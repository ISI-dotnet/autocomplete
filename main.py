import tkinter as tk
from nltk.corpus import words
from nltk.probability import FreqDist
import nltk
nltk.download("words")

class AutocompleteTextbox:
    def __init__(self, root):
        self.root = root
        self.words = set(words.words())
        self.word_freq = FreqDist(words.words())
        
        self.text_area = tk.Text(root, wrap='word', height=30, width=160, font=("Arial", 12))
        self.text_area.pack()
        self.text_area.bind("<KeyRelease>", self.autocomplete)
        self.text_area.bind("<Tab>", self.apply_suggestion)

        self.suggestion_listbox = tk.Listbox(root, width=160, height=3, font=("Arial", 12))
        self.suggestion_listbox.pack()

    def autocomplete(self, event):
        current_text = self.text_area.get("1.0", tk.END)[:-1]
        words_list = current_text.split()
        if len(words_list) >= 1:
            last_word_to_complete = words_list[-1]
            suggestions = self.get_word_suggestions(last_word_to_complete)[:3]
            if current_text[-1] == " ":
                self.update_suggestions([])
            else:
                self.update_suggestions(suggestions)

    def get_word_suggestions(self, current_text):
        suggestions = [word for word in self.words if word.startswith(current_text.lower())]
        suggestions.sort(key=lambda word: -self.word_freq[word])
        return suggestions

    def update_suggestions(self, suggestions):
        self.suggestion_listbox.delete(0, tk.END)
        current_text = self.text_area.get("1.0", tk.END)[:-1]
        words_list = current_text.split()
        for suggestion in suggestions:
            if len(words_list) == 1:
                suggestion = suggestion.capitalize()
            self.suggestion_listbox.insert(tk.END, suggestion)

    def apply_suggestion(self, event):
        selected_word = self.suggestion_listbox.get(0)
        if selected_word:
            current_text = self.text_area.get("1.0", tk.END)[:-1]
            words_list = current_text.split()
            if len(words_list) >= 1:
                last_word_index = current_text.rfind(words_list[-1])
                updated_text = current_text[:last_word_index] + selected_word + " "
                self.text_area.delete("1.0", tk.END)
                self.text_area.insert(tk.END, updated_text)
                return 'break'

def main():
    root = tk.Tk()
    root.title("Autocomplete Text Area")
    app = AutocompleteTextbox(root)
    root.mainloop()

if __name__ == "__main__":
    main()
