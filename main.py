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

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()