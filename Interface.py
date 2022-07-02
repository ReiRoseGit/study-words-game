import tkinter as tk
from tkinter import *
from Vocabulary import *
from random import randint
import tkinter.messagebox as mb


class Interface(tk.Tk):
    def __init__(self):
        self.dictionary = Vocabulary()
        self.learned_words = []
        super().__init__()
        self.geometry("600x600")
        self.resizable(False, False)
        self.title("English Game...")
        self.background_image = PhotoImage(file=("bg.png"))
        self.start_label = Label(self, text="Welcome!",  bg="white", fg="black",
                                 font="Arial 18", width="30")
        self.start_label.place(relx=0.5, rely=0.25, anchor=CENTER)
        self.start_btn = Button(self, text="Click here to start game!",
                                command=self.start_game, bg="white", fg="black", font="Arial 16", bd=4)
        self.start_btn.place(relx=0.5, rely=0.55, anchor=CENTER)
        self.word_label = Label(self, text="Here will be a word.", bg="white", fg="black",
                                font="Arial 18", width="30")

        self.translation_label = Label(self, text="Here will be a translation.", bg="white", fg="black",
                                       font="Arial 18", width="30")

        self.next_word_btn = Button(self, text="Next word",
                                    command=self.next_word, bg="white", fg="black", font="Arial 16", bd=4)

        self.stop_game_btn = Button(self, text="Stop learning",
                                    command=self.stop_game, bg="white", fg="black", font="Arial 16", bd=4)

    def start_game(self):
        self.start_btn.destroy()
        self.start_label.destroy()
        self.word_label.place(relx=0.5, rely=0.25, anchor=CENTER)
        self.translation_label.place(relx=0.5, rely=0.35, anchor=CENTER)
        self.next_word_btn.place(relx=0.5, rely=0.55, anchor=CENTER)
        self.stop_game_btn.place(relx=0.5, rely=0.75, anchor=CENTER)

    def next_word(self):
        item = self.dictionary.get_random_item()
        self.learned_words.append(item)
        self.word_label.config(text=item[0])
        self.translation_label.config(text=item[1])

    def stop_game(self):
        self.word_label.destroy()
        self.translation_label.destroy()
        self.next_word_btn.destroy()
        self.stop_game_btn.destroy()
        self.learned_words_label = Label(self, bg="white", fg="black",
                                         font="Arial 14", width="55")
        self.repeat_words_btn = Button(self, text="Да",
                                       command=self.repeat_words, bg="white", fg="black", font="Arial 16", bd=4)
        self.learned_words_label["text"] = f"Вы изучили {len(self.learned_words)} слов. Желаете ли повторить изученный материал?"
        self.learned_words_label.place(relx=0.5, rely=0.35, anchor=CENTER)
        self.repeat_words_btn.place(relx=0.5, rely=0.55, anchor=CENTER)

    def repeat_words(self):
        self.learned_words_label.destroy()
        self.repeat_words_btn.destroy()
        self.word_label = Label(self, text="Here will be a word.", bg="white", fg="black",
                                font="Arial 18", width="30")

        # self.translation_label = Label(self, text="Entry here a translation of word.", bg="white", fg="black",
        #                               font="Arial 18", width="30")
        self.next_word_btn = Button(self, text="Next word",
                                    command=self.next_word_repeat, bg="white", fg="black", font="Arial 16", bd=4)
        self.word_label.place(relx=0.5, rely=0.25, anchor=CENTER)
        #self.translation_label.place(relx=0.5, rely=0.35, anchor=CENTER)
        self.next_word_btn.place(relx=0.5, rely=0.55, anchor=CENTER)

    def next_word_repeat(self):
        l = len(self.learned_words)
        if l > 0:
            item = self.learned_words.pop(randint(0, l - 1))
            if "," in item[1]:
                self.translation = item[1].split(", ")[0]
            elif "(" in item[1]:
                self.translation = item[1].split(") ")[0]
            elif " или " in item[1]:
                self.translation = item[1].split(" или ")[0]
            else:
                self.translation = item[1]
            self.word_label.config(text=item[0])
            self.message = StringVar()
            self.entry_word = Entry(
                bg="white", fg="black", font="Arial 18", width="35", textvariable=self.message)
            self.entry_word.place(relx=0.5, rely=0.35, anchor=CENTER)
            self.check_translation_btn = Button(self, text="Check",
                                                command=self.check_translation, bg="white", fg="black", font="Arial 16", bd=4)
            self.check_translation_btn.place(
                relx=0.5, rely=0.85, anchor=CENTER)
        else:
            self.word_label.destroy()
            self.next_word_btn.destroy()
            self.entry_word.destroy()
            self.check_translation_btn.destroy()
            self.end_of_game_label = Label(self, text="The end of Game!", bg="white", fg="black",
                                           font="Arial 18", width="30")
            self.end_of_game_label.place(relx=0.5, rely=0.5, anchor=CENTER)

    def check_translation(self):
        if self.message.get().lower() == self.translation.lower():
            self.show_info()
        else:
            self.show_warning()

    def show_info(self):
        msg = "Успешно, можете продолжать!"
        mb.showinfo("Success", msg)

    def show_warning(self):
        msg = "Попробуйте еще раз!"
        mb.showinfo("Error", msg)
