import tkinter as tk
from tkinter import messagebox

class Library_Frame(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.root = master
        self.create_widgets()
        self.layout()


    def create_widgets(self):
        self.label = tk.Label(self, text='')
        self.add_button = tk.Button(self, text='Dodaj', command=self.add_book)
        self.check_button = tk.Button(self, text='Wyświetl', command=self.list_books)

    def layout(self):
        self.pack()
        self.label.pack()
        self.add_button.pack()
        self.check_button.pack()

    def add_book(self):
        dialog = Add_Book_Frame(self)
        self.root.wait_window(dialog)

    def list_books(self):
        pass


class Add_Book_Frame(tk.Toplevel):
    def __init__(self, master):
        tk.Toplevel.__init__(self, master)
        self.root = master
        self.create_widgets()
        self.layout()

    def create_widgets(self):
        self.label = tk.Label(self, text='')
        self.author_entry = tk.Entry(self)
        self.title_entry = tk.Entry(self)
        self.button = tk.Button(self, text='Gotowe', command=self.send_to_db)

    def layout(self):
        self.label.pack()
        self.author_entry.pack()
        self.title_entry.pack()
        self.button.pack()

    def send_to_db(self):
        pass

    def clear_entry(self):
        self.author_entry.delete(0, tk.END)  # czyszczenie entry
        self.title_entry.delete(0, tk.END)


window = tk.Tk()
window.title('Biblioteka')
frame = Library_Frame(window)
frame.mainloop()
