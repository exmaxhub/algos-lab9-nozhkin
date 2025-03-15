# import tkinter as tk
# buttonFrame = tk.Frame(root)
# buttonFrame.columnconfigure(0, weight=1)
# buttonFrame.columnconfigure(1, weight=1)
# btn1 = tk.Button(buttonFrame, text="1", font=("Arial", 18))
# btn1.grid(row=0, column=0, sticky="we")
# buttonFrame.pack(fill="x")
# import tkinter as tk


root = tk.Tk()
root.title("Калькулятор")
root.geometry("300x300")
entry = tk.Entry(root, width=35, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, str(current) + str(number))

def button_clear():
    entry.delete(0, tk.END)

def button_equal():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Ошибка")


button_7 = tk.Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
button_8 = tk.Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
button_9 = tk.Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))
button_div = tk.Button(root, text="/", padx=40, pady=20, command=lambda: button_click("/"))

button_4 = tk.Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
button_5 = tk.Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
button_6 = tk.Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))
button_mul = tk.Button(root, text="*", padx=40, pady=20, command=lambda: button_click("*"))

button_1 = tk.Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
button_2 = tk.Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
button_3 = tk.Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))
button_sub = tk.Button(root, text="-", padx=40, pady=20, command=lambda: button_click("-"))

button_0 = tk.Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0))
button_dot = tk.Button(root, text=".", padx=40, pady=20, command=lambda: button_click("."))
button_equal = tk.Button(root, text="=", padx=40, pady=20, command=button_equal)
button_add = tk.Button(root, text="+", padx=40, pady=20, command=lambda: button_click("+"))

button_clear = tk.Button(root, text="C", padx=29, pady=20, command=button_clear)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)
button_div.grid(row=1, column=3)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_mul.grid(row=2, column=3)

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_sub.grid(row=3, column=3)

button_0.grid(row=4, column=0)
button_dot.grid(row=4, column=1)
button_equal.grid(row=4, column=2)
button_add.grid(row=4, column=3)

button_clear.grid(row=5, column=0, columnspan=4)

root.mainloop()