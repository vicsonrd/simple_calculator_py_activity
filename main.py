import tkinter as tk

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple App Calculator")
        self.root.geometry("300x350")

        # Result Display
        self.result_var = tk.StringVar(value="Result: 0")
        tk.Label(root, textvariable=self.result_var, font=("Arial", 14, "bold"), pady=10).pack()

        # Input Fields
        tk.Label(root, text="Number 1:").pack()
        self.entry1 = tk.Entry(root)
        self.entry1.pack()

        tk.Label(root, text="Number 2:").pack()
        self.entry2 = tk.Entry(root)
        self.entry2.pack()

        # Operation Buttons
        btn_frame = tk.Frame(root)
        btn_frame.pack(pady=15)

        ops = [("Add", "Addition"), ("Sub", "Subtraction"), 
               ("Mul", "Multiplication"), ("Div", "Division")]

        for text, op_type in ops:
            btn = tk.Button(btn_frame, text=text, width=8, 
                            command=lambda o=op_type: self.handle_click(o))
            btn.pack(side="left", padx=2)

    def handle_click(self, operation):
        pass # To be implemented

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()