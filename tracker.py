import tkinter as tk
from tkinter import messagebox
from collections import defaultdict
import json
import matplotlib.pyplot as plt

# Function to add an expense
def add_expense():
    date = date_entry.get()
    category = category_entry.get()
    amount = float(amount_entry.get())
    if date.strip() and category.strip() and amount > 0:
        expenses[date][category] += amount
        messagebox.showinfo("Success", "Expense added successfully!")
        date_entry.delete(0, tk.END)
        category_entry.delete(0, tk.END)
        amount_entry.delete(0, tk.END)
    else:
        messagebox.showerror("Error", "Please enter valid inputs!")

# Function to display summary
def display_summary():
    summary_text.delete(1.0, tk.END)
    total_expenses = 0
    summary_text.insert(tk.END, "Expense Summary:\n")
    for date, category_expenses in expenses.items():
        summary_text.insert(tk.END, f"On {date}:\n")
        for category, amount in category_expenses.items():
            summary_text.insert(tk.END, f"  {category}: ${amount:.2f}\n")
            total_expenses += amount
    summary_text.insert(tk.END, f"\nTotal Expenses: ${total_expenses:.2f}")

# Function to save expenses to a file
def save_expenses_to_file():
    filename = filename_entry.get()
    if filename.strip():
        with open(filename, 'w') as file:
            json.dump(expenses, file)
        messagebox.showinfo("Success", "Expenses saved to file successfully!")
        filename_entry.delete(0, tk.END)
    else:
        messagebox.showerror("Error", "Please enter a valid filename!")

# Function to visualize expenses
def visualize_expenses():
    categories = defaultdict(float)
    for date_expenses in expenses.values():
        for category, amount in date_expenses.items():
            categories[category] += amount
    
    plt.bar(categories.keys(), categories.values(), color='skyblue')
    plt.xlabel('Categories')
    plt.ylabel('Amount ($)')
    plt.title('Expense Visualization')
    plt.xticks(rotation=45)
    plt.show()

# Create main window
root = tk.Tk()
root.title("Expense Tracker")
root.geometry("450x650")
root.configure(bg="#2c3e50")

# Configure styles
label_font = ("Helvetica", 12, "bold")
entry_font = ("Helvetica", 12)
button_font = ("Helvetica", 12, "bold")
text_font = ("Helvetica", 12)
button_bg = "#3498db"
button_fg = "#ecf0f1"
label_fg = "#ecf0f1"
entry_bg = "#ecf0f1"
entry_fg = "#2c3e50"
text_bg = "#34495e"
text_fg = "#ecf0f1"

# Create expense entry fields
date_label = tk.Label(root, text="Date (YYYY-MM-DD):", font=label_font, bg="#2c3e50", fg=label_fg)
date_label.grid(row=0, column=0, padx=10, pady=10, sticky="W")
date_entry = tk.Entry(root, font=entry_font, bg=entry_bg, fg=entry_fg)
date_entry.grid(row=0, column=1, padx=10, pady=10, sticky="E")

category_label = tk.Label(root, text="Category:", font=label_font, bg="#2c3e50", fg=label_fg)
category_label.grid(row=1, column=0, padx=10, pady=10, sticky="W")
category_entry = tk.Entry(root, font=entry_font, bg=entry_bg, fg=entry_fg)
category_entry.grid(row=1, column=1, padx=10, pady=10, sticky="E")

amount_label = tk.Label(root, text="Amount ($):", font=label_font, bg="#2c3e50", fg=label_fg)
amount_label.grid(row=2, column=0, padx=10, pady=10, sticky="W")
amount_entry = tk.Entry(root, font=entry_font, bg=entry_bg, fg=entry_fg)
amount_entry.grid(row=2, column=1, padx=10, pady=10, sticky="E")

# Create buttons
add_button = tk.Button(root, text="Add Expense", font=button_font, bg=button_bg, fg=button_fg, command=add_expense)
add_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10, sticky="WE")

display_button = tk.Button(root, text="Display Summary", font=button_font, bg=button_bg, fg=button_fg, command=display_summary)
display_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10, sticky="WE")

# Create text box for summary
summary_text = tk.Text(root, height=10, width=40, font=text_font, bg=text_bg, fg=text_fg)
summary_text.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

# Create save expenses to file entry fields and button
filename_label = tk.Label(root, text="Filename:", font=label_font, bg="#2c3e50", fg=label_fg)
filename_label.grid(row=6, column=0, padx=10, pady=10, sticky="W")
filename_entry = tk.Entry(root, font=entry_font, bg=entry_bg, fg=entry_fg)
filename_entry.grid(row=6, column=1, padx=10, pady=10, sticky="E")

save_button = tk.Button(root, text="Save Expenses to File", font=button_font, bg=button_bg, fg=button_fg, command=save_expenses_to_file)
save_button.grid(row=7, column=0, columnspan=2, padx=10, pady=10, sticky="WE")

# Create visualize expenses button
visualize_button = tk.Button(root, text="Visualize Expenses", font=button_font, bg=button_bg, fg=button_fg, command=visualize_expenses)
visualize_button.grid(row=8, column=0, columnspan=2, padx=10, pady=10, sticky="WE")

# Initialize expenses dictionary
expenses = defaultdict(lambda: defaultdict(float))

root.mainloop()
