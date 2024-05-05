import tkinter as tk
from tkinter import messagebox


class GUI:

    def __init__(self):
        self.root = tk.Tk()

        self.mainFrame = tk.Frame(self.root)
        self.buttonsFrame = tk.Frame(self.root)
        self.historyFrame = tk.Frame(self.root)

        self.root.title("Calculator")
        self.root.geometry("800x500")

        self.label = tk.Label(self.mainFrame, text="Your calculation:")
        self.calculation = tk.Text(self.mainFrame, height=1)
        self.calculation.bind("<KeyPress>", self.shortcut)

        self.button = tk.Button(self.buttonsFrame, text="enter", command=self.calcLogic)
        self.answer = tk.Button(self.buttonsFrame, text="ans", command=self.getAns)

        self.history = tk.Label(self.historyFrame, text="history:")

        self.mainFrame.pack(padx=15, pady=10)
        self.buttonsFrame.pack(padx=15, pady=10)
        self.historyFrame.pack(side=tk.LEFT)

        self.label.grid(row=0, pady=5)
        self.calculation.grid(row=1, pady=5)

        self.button.grid(row=0, column=0, padx=25)
        self.answer.grid(row=0, column=1, padx=25)

        self.history.pack()

        self.root.mainloop()

    def calcLogic(self):
        self.calc = self.calculation.get('1.0', tk.END)
        self.str = ""

        for i in self.calc:

            if i == " ":
                continue
            elif i == "+":
                self.value1 = float(self.str)
                self.cm = "+"
                self.str = ""
                continue
            elif i == "*":
                self.value1 = float(self.str)
                self.cm = "*"
                self.str = ""
                continue
            elif i == "-":
                self.value1 = float(self.str)
                self.cm = "-"
                self.str = ""
                continue
            elif i == "/":
                self.value1 = float(self.str)
                self.cm = "/"
                self.str = ""
                continue

            self.str += i

        self.value2 = float(self.str)

        if self.cm == "/":
            messagebox.showinfo(title="result", message=f"{self.value1 / self.value2}")
            self.answ = self.value1 / self.value2
        elif self.cm == "*":
            messagebox.showinfo(title="result", message=f"{self.value1 * self.value2}")
            self.answ = self.value1 * self.value2
        elif self.cm == "-":
            messagebox.showinfo(title="result", message=f"{self.value1 - self.value2}")
            self.answ = self.value1 - self.value2
        elif self.cm == "+":
            messagebox.showinfo(title="result", message=f"{self.value1 + self.value2}")
            self.answ = self.value1 + self.value2

        self.calculation.delete("1.0", tk.END)
        self.calculation_history = tk.Label(self.historyFrame, text=f'{self.value1} {self.cm} {self.value2} = {self.answ}')
        self.calculation_history.pack(padx=10, pady=10)

    def getAns(self):
        self.calculation.insert(tk.END, str(self.answ))

    def shortcut(self, event):
        if event.keysym == 'Return' and event.state == 4:
            self.calcLogic()
        elif event.keysym == 'A' and event.state == 5:
            self.getAns()


GUI()
