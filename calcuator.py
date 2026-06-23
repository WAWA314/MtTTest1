import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("320x500")
        self.root.resizable(False, False)
        self.root.configure(bg="#f3f3f3")

        self.expression = ""
        self.input_var = tk.StringVar()
        self.input_var.set("0")

        self.build_ui()

    def build_ui(self):
        # ---- Display ----
        display = tk.Entry(self.root,
                           textvariable=self.input_var,
                           font=("Segoe UI", 36),
                           bg="#f3f3f3", fg="#000000",
                           borderwidth=0,
                           justify="right",
                           state="readonly")
        display.pack(fill="both", padx=10, pady=(20, 10), ipady=10)

        # ---- ปุ่ม ----
        btn_frame = tk.Frame(self.root, bg="#f3f3f3", padx=5, pady=5)
        btn_frame.pack(fill="both", expand=True)

        buttons = [
            ["%",  "CE", "C",  "⌫"],
            ["1/x","x²", "√x", "÷"],
            ["7",  "8",  "9",  "×"],
            ["4",  "5",  "6",  "−"],
            ["1",  "2",  "3",  "+"],
            ["+/-","0",  ".",  "="],
        ]

        for r, row in enumerate(buttons):
            for c, text in enumerate(row):
                self.make_button(btn_frame, text, r, c)

    def make_button(self, frame, text, row, col):
        if text == "=":
            bg, fg = "#0078d7", "#ffffff"
        elif text in ["÷", "×", "−", "+"]:
            bg, fg = "#e0e0e0", "#000000"
        elif text in ["%", "CE", "C", "⌫", "1/x", "x²", "√x"]:
            bg, fg = "#e0e0e0", "#000000"
        else:
            bg, fg = "#ffffff", "#000000"

        btn = tk.Button(frame, text=text,
                        font=("Segoe UI", 16),
                        bg=bg, fg=fg,
                        activebackground="#c0c0c0",
                        borderwidth=1,
                        relief="flat",
                        cursor="hand2",
                        command=lambda t=text: self.on_click(t))

        btn.grid(row=row, column=col,
                 padx=2, pady=2,
                 sticky="nsew",
                 ipadx=5, ipady=12)

        frame.grid_rowconfigure(row, weight=1)
        frame.grid_columnconfigure(col, weight=1)

    def on_click(self, text):
        if text == "C" or text == "CE":
            self.expression = ""
            self.input_var.set("0")

        elif text == "⌫":
            self.expression = self.expression[:-1]
            self.input_var.set(self.expression if self.expression else "0")

        elif text == "=":
            try:
                expr = self.expression.replace("÷", "/").replace("×", "*").replace("−", "-")
                result = eval(expr)
                if isinstance(result, float) and result.is_integer():
                    result = int(result)
                self.input_var.set(str(result))
                self.expression = str(result)
            except:
                self.input_var.set("Error")
                self.expression = ""

        elif text == "+/-":
            try:
                val = float(self.expression)
                val = -val
                if float(val).is_integer():
                    val = int(val)
                self.expression = str(val)
                self.input_var.set(self.expression)
            except:
                pass

        elif text == "%":
            try:
                val = float(self.expression) / 100
                if float(val).is_integer():
                    val = int(val)
                self.expression = str(val)
                self.input_var.set(self.expression)
            except:
                pass

        elif text == "x²":
            try:
                val = float(self.expression) ** 2
                if float(val).is_integer():
                    val = int(val)
                self.expression = str(val)
                self.input_var.set(self.expression)
            except:
                pass

        elif text == "√x":
            try:
                val = float(self.expression) ** 0.5
                if float(val).is_integer():
                    val = int(val)
                self.expression = str(val)
                self.input_var.set(self.expression)
            except:
                pass

        elif text == "1/x":
            try:
                val = 1 / float(self.expression)
                self.expression = str(val)
                self.input_var.set(self.expression)
            except:
                self.input_var.set("Error")
                self.expression = ""

        else:
            if self.input_var.get() in ("0", "Error") and text not in [".", "÷", "×", "−", "+"]:
                self.expression = text
            else:
                self.expression += text
            self.input_var.set(self.expression)

if __name__ == "__main__":
    root = tk.Tk()
    app = Calculator(root)
    root.mainloop()