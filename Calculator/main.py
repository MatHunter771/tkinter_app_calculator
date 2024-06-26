import subprocess
import tkinter as tk
from tkinter import messagebox
import appSettings as set


def extractNumber(str):
    output = ''
    for i in str:
        try:
            int(i)
        except:
            continue
        else:
            output += i
    return output


class GUI:

    def __init__(self):
        self.size = 40
        self.root = tk.Tk()

        self.root.title("Calculator")
        self.root.geometry("800x500")

        self.mainFrame = tk.Frame(self.root)
        self.buttonsFrame = tk.Frame(self.root)
        self.historyFrame = tk.Frame(self.root, height=100)

        self.menubar = tk.Menu(self.root)
        self.fileMenu = tk.Menu(self.menubar, tearoff=0)
        self.equalityMenu = tk.Menu(self.menubar, tearoff=0)

        self.label = tk.Label(self.mainFrame, text="Your calculation:", font={'Arial',self.size})
        self.calculation = tk.Text(self.mainFrame, height=1)
        self.calculation.bind("<KeyPress>", self.shortcut)

        self.button = tk.Button(self.buttonsFrame, text="enter", command=self.calcLogic)
        self.answer = tk.Button(self.buttonsFrame, text="ans", command=self.getAns)
        self.clear = tk.Button(self.buttonsFrame, text="clear", command=self.clearCalc)

        self.history = tk.Label(self.historyFrame, text="history:")
        self.t = 1

        self.menubar.add_cascade(menu=self.fileMenu, label="File")
        self.menubar.add_cascade(menu=self.equalityMenu, label="Equality")

        self.fileMenu.add_command(label='Settings', command=self.settings)
        self.fileMenu.add_command(label="Close", command=self.shut_down)

        self.equalityMenu.add_command(label="Plot", command=self.plotting)

        self.root.config(menu=self.menubar)

        self.mainFrame.pack(padx=15, pady=10)
        self.buttonsFrame.pack(padx=15, pady=10)
        self.historyFrame.pack(side=tk.LEFT)

        self.label.grid(row=0, pady=5)
        self.calculation.grid(row=1, pady=5)

        self.button.grid(row=0, column=0, padx=25)
        self.answer.grid(row=0, column=1, padx=25)
        self.clear.grid(row=0, column=2, padx=25)

        self.history.grid()

        self.root.protocol("WM_DELETE_WINDOW", self.shut_down)

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
        self.t += 1
        if self.t > 4:
            self.t = 1
        self.calculation_history.grid(row=self.t, pady=5)

    def getAns(self):
        self.calculation.insert(tk.END, str(self.answ))

    def shortcut(self, event):
        if event.keysym == 'Return' and event.state == 4:
            self.calcLogic()
        elif event.keysym == 'A' and event.state == 5:
            self.getAns()

    def shut_down(self):
        if messagebox.askyesno(title="Quit", message="Do you want to quit?"):
            self.root.destroy()

    def plotting(self):
        subprocess.Popen(['python', 'plot_input.py'])

    def clearCalc(self):
        self.calculation.delete("1.0", tk.END)

    def settings(self):
#        subprocess.Popen(['python', 'appSettings.py'])
        set.GUI()
        pd = open('calculatorSettings0001', 'r')
        sizeStr = pd.readline()
        checkStr = pd.readline()
        self.size = extractNumber(sizeStr)
        self.check = extractNumber(checkStr)
        pd.close()


GUI()
