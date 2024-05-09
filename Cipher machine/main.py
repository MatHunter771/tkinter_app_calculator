import string

import customtkinter as ctk
from tkinter import messagebox


class GUI:
    def __init__(self):
        self.root = ctk.CTk()
        self.root.title('Cipher Machine')
        self.root.geometry('800x500')

        ctk.set_default_color_theme('dark-blue')
        ctk.set_appearance_mode('dark')

        self.mainFrame = ctk.CTkFrame(self.root)
        self.buttonsFrame = ctk.CTkFrame(self.root)

        self.text = ctk.CTkLabel(self.mainFrame, text='Enter text:')
        self.entry = ctk.CTkEntry(self.mainFrame, width=600)
        self.enter = ctk.CTkButton(self.buttonsFrame, text='Enter', command=self.cypherCeasar)

        self.mainFrame.pack(padx=25, pady=20)
        self.buttonsFrame.pack(pady=5)

        self.text.grid(row=0)
        self.entry.grid(row=1)

        self.enter.grid()

        self.root.protocol('WM_DELETE_WINDOW', self.shut_down)

        self.root.mainloop()

    def cypherCeasar(self):
        signs = list(string.ascii_letters)
        inputSentence = self.entry.get()
        outputSentence = ''

        for i in range(len(inputSentence)):
            p = signs.index(inputSentence[i])
            if p + 3 < len(signs):
                outputSentence += str(signs[p+3])
            else:
                outputSentence += str(signs[p+3-(len(signs)-1)])

        messagebox.showinfo(message=outputSentence, title='Output')

    def shut_down(self):
        if messagebox.askyesno(title="Quit", message="Do you want to quit?"):
            self.root.destroy()


GUI()