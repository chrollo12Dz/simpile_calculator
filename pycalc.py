import tkinter as tk

window = tk.Tk()
window.title("Simple Calculator")
window.geometry("320x400")
window.resizable(False, False)


entry = tk.Entry(window, width=16, font=("Arial", 24), borderwidth=2, relief="solid", justify="right")
entry.grid(row=0, column=0, columnspan=4, pady=10)


def click(symbol):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(symbol))

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
]


for (text, row, col) in buttons:
    if text == "=":
        btn = tk.Button(window, text=text, width=5, height=2, font=("Arial", 18), command=calculate)
    else:
        btn = tk.Button(window, text=text, width=5, height=2, font=("Arial", 18), command=lambda t=text: click(t))
    btn.grid(row=row, column=col, padx=5, pady=5)


clear_btn = tk.Button(window, text="C", width=22, height=2, font=("Arial", 18), command=clear)
clear_btn.grid(row=5, column=0, columnspan=4, pady=10)


window.mainloop()

