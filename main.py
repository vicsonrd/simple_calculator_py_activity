import tkinter as tk

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple App Calculator")
        self.root.geometry("300x350")

        # Result Display
        self.result_var = tk.StringVar(value="Result: 0")
        tk.Label(root, textvariable=self.result_var, font=("Arial", 14, "bold"), pady=10).pack()

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()