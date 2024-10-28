import tkinter as tk
import tkinter.ttk as ttk


class CalcWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("CalcuNow")
        self.geometry("400x600")

        # Configuring resize weights for each grid item
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=2)
        self.rowconfigure(2, weight=4)
        self.columnconfigure((0,), weight=1)
        
        # Some styles :)
        style = ttk.Style()
        heading_style = 'Heading.Label'
        button_style = "Numbers.TButton"
        style.configure(heading_style, font='monospace 16')
        style.configure(button_style, font='monospace 12')

        # Heading
        head = ttk.Label(text="Calculator", style=heading_style);
        head.grid(row=0, column=0, sticky=tk.N,)

        # Input and output box
        self.string_var = tk.StringVar()
        io = ttk.Entry(textvariable=self.string_var)
        io.grid(row=1, column=0, sticky=tk.NSEW)

        # All the buttons are inside this frame
        input_frame = ttk.Frame()
        input_frame.rowconfigure(tuple(range(6)), weight=1)
        input_frame.columnconfigure(tuple(range(4)), weight=1)
                
        ac = ttk.Button(master=input_frame, text="AC", command=self.clear_text_box, style=button_style)
        ac.grid(row=0, column=0, columnspan=2, sticky=tk.NSEW)

        backspace = ttk.Button(master=input_frame, text="Backspace", command= self.backspace_text_box, style=button_style)
        backspace.grid(row=0, column=2, columnspan=2, sticky=tk.NSEW)

        divide = ttk.Button(master=input_frame, text="/", command=lambda : self.insert_into_box("/"), style=button_style)
        divide.grid(row=1, column=3, sticky=tk.NSEW)
        mult = ttk.Button(master=input_frame, text="*", command=lambda : self.insert_into_box("*"), style=button_style)
        mult.grid(row=2, column=3, sticky=tk.NSEW)
        minus = ttk.Button(master=input_frame, text="-", command=lambda : self.insert_into_box("-"), style=button_style)
        minus.grid(row=3, column=3, sticky=tk.NSEW)
        plus = ttk.Button(master=input_frame, text="+", command=lambda : self.insert_into_box("+"), style=button_style)
        plus.grid(row=4, column=3, sticky=tk.NSEW)

        equals = ttk.Button(master=input_frame, text="=", command=self.evaluate, style=button_style)
        equals.grid(row=5, column=0, columnspan=4, sticky=tk.NSEW)

        zero = ttk.Button(master=input_frame, text="0", style=button_style)
        zero.grid(row=4, column=0, columnspan=2, sticky=tk.NSEW)
        zero.configure(command=lambda: self.insert_into_box("0"))

        decimal = ttk.Button(master=input_frame, text=".", command=lambda : self.insert_into_box("."), style=button_style)
        decimal.grid(row=4, column=2, sticky=tk.NSEW)

        for i in range(1, 10):
            row = 3-((i-1)//3)
            col = (i-1)%3
            btn = ttk.Button(master=input_frame, text=str(i), command=lambda i=i: self.insert_into_box(str(i)), style=button_style)
            btn.grid(row=row, column=col, sticky=tk.NSEW)

        input_frame.grid(row=2, column=0, sticky=tk.NSEW)


    def insert_into_box(self, new_text: str):
        self.string_var.set(self.string_var.get().strip() + new_text);

    def clear_text_box(self):
        self.string_var.set("")

    def backspace_text_box(self):
        expr = self.string_var.get().strip()
        self.string_var.set(expr[0:len(expr)-1])

    def evaluate(self):
        expr = self.string_var.get().strip()
        try:
            evaluated_result = eval(expr)
        except:
            evaluated_result = "Error"
        self.string_var.set(evaluated_result)


window = CalcWindow()
window.mainloop()
