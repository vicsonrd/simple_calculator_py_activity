# main.py
import tkinter as tk
from tkinter import messagebox
# Import the logic function from our separate file
from calculator_logic import perform_calculation

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
        try:
            num1 = self.entry1.get()
            num2 = self.entry2.get()
            
            # Call the function from the logic file
            res = perform_calculation(num1, num2, operation)
            self.result_var.set(f"Result: {res}")
            
            # --- NEW CODE: Save to history file ---
            with open("calculator_history.txt", "a") as history_file:
                # Format a readable string, e.g., "5 Addition 10 = 15"
                history_file.write(f"{num1} {operation} {num2} = {res}\n")
            # --------------------------------------
            
            # Ask to try again
            self.check_try_again()

        except Exception as e:
            messagebox.showerror("Error", str(e))

    def check_try_again(self):
        answer = messagebox.askyesno("Try Again?", "Would you like to perform another calculation?")
        if answer:
            self.entry1.delete(0, tk.END)
            self.entry2.delete(0, tk.END)
            self.result_var.set("Result: 0")
        else:
            messagebox.showinfo("Exit", "Thank you!")
            self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()