from tkinter.font import BOLD
import pandas as pd
from tkinter import *
from tkinter import ttk
df = pd.read_excel('tradevalue.xlsx', header=0, index_col=0)
print(df)
def calcValue(*args):
    global t1
    t1 = t1.get().split(", ")
    global t2
    t2 = t2.get().split(", ")
    print(t1, t2)
    t1val = 0
    t2val = 0
    for i in t1:
        try:
            a = df.loc[i, 'Value']
            t1val += a
        except KeyError:
            newWindow1 = Toplevel(root)
            newWindow1.title("Error!")
            err1 = ttk.Label(newWindow1, text="Error! Player not found!\n(check your 'giving away' entry for spelling)")
            err1.grid(column=1,row=1)
            return
    for j in t2:
        try:
            b = df.loc[j, 'Value']
            t2val += b
        except KeyError:
            newWindow2 = Toplevel(root)
            newWindow2.title("Error!")
            err2 = ttk.Label(newWindow2, text="Error! Player not found!\n(check your 'receiving' entry for spelling)")
            err2.grid(column=1,row=1)
            return
    if t1val == t2val:
        res = ttk.Label(mainframe, text='Giving Up: ' + str(t1val) + '\nReceiving: ' + str(t2val) + "\nThis trade is fair!")
        res.grid(column=1,row=7)
    elif t1val > t2val:
        res = ttk.Label(mainframe, text='Giving Up: ' + str(t1val) + '\nReceiving: ' + str(t2val) + "\nYou're losing this trade!")
        res.grid(column=1,row=7)
    else: 
        res = ttk.Label(mainframe, text='Giving Up: ' + str(t1val) + '\nReceiving: ' + str(t2val) + "\nYou're winning this trade!")
        res.grid(column=1,row=7)
root = Tk()
root.title("Trade Evaluator")
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
t1 = StringVar()
welcome = ttk.Label(mainframe, text="Welcome to my trade evaluator!", font=(BOLD)
welcome.grid(column = 1, row = 1)
t1label = ttk.Label(mainframe, text="Enter players to trade away...\n(use commas to seperate multiple players)")
t1label.grid(column = 1, row = 2)
t1entry = ttk.Entry(mainframe, textvariable = t1)
t1entry.grid(column=1,row=3)
t2 = StringVar()
t2label = ttk.Label(mainframe, text="Enter players to receive...\n(use commas to seperate multiple players)")
t2label.grid(column = 1, row = 4)
t2entry = ttk.Entry(mainframe, textvariable = t2)
t2entry.grid(column=1,row=5)
submit = ttk.Button(mainframe, text="Submit", command=calcValue)
submit.grid(column=1,row=6)
credits = ttk.Label(mainframe, text="Created by Alexander Leitzke | github.com/ajleitzke")
credits.grid(column=1,row=8)
mainloop()
