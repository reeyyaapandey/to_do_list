import tkinter as tk
from tkinter import messagebox
import os

FILE_NAME = "tasks.txt"

# ---------------- Functions ---------------- #

def add_task():
    task = task_entry.get()
    if task == "":
        messagebox.showwarning("Warning", "Task cannot be empty!")
    else:
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
        save_tasks()

def delete_task():
    try:
        selected = task_listbox.curselection()
        task_listbox.delete(selected)
        save_tasks()
    except:
        messagebox.showwarning("Warning", "Please select a task!")

def edit_task():
    try:
        selected = task_listbox.curselection()
        new_task = task_entry.get()
        if new_task == "":
            messagebox.showwarning("Warning", "Enter updated task!")
        else:
            task_listbox.delete(selected)
            task_listbox.insert(selected, new_task)
            task_entry.delete(0, tk.END)
            save_tasks()
    except:
        messagebox.showwarning("Warning", "Select a task to edit!")

def mark_completed():
    try:
        selected = task_listbox.curselection()
        task = task_listbox.get(selected)
        task_listbox.delete(selected)
        task_listbox.insert(tk.END, f"✔ {task}")
        save_tasks()
    except:
        messagebox.showwarning("Warning", "Select a task to mark completed!")

def save_tasks():
    with open(FILE_NAME, "w") as file:
        tasks = task_listbox.get(0, tk.END)
        for task in tasks:
            file.write(task + "\n")

def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            for task in file:
                task_listbox.insert(tk.END, task.strip())

# ---------------- UI ---------------- #

root = tk.Tk()
root.title("Advanced To-Do List")
root.geometry("420x520")
root.resizable(False, False)

title = tk.Label(root, text="To-Do List App", font=("Arial", 18, "bold"))
title.pack(pady=10)

task_entry = tk.Entry(root, width=32, font=("Arial", 12))
task_entry.pack(pady=10)

button_frame = tk.Frame(root)
button_frame.pack(pady=10)

add_btn = tk.Button(button_frame, text="Add", width=10, command=add_task)
add_btn.grid(row=0, column=0, padx=5)

edit_btn = tk.Button(button_frame, text="Edit", width=10, command=edit_task)
edit_btn.grid(row=0, column=1, padx=5)

delete_btn = tk.Button(button_frame, text="Delete", width=10, command=delete_task)
delete_btn.grid(row=1, column=0, padx=5, pady=5)

complete_btn = tk.Button(button_frame, text="Completed", width=10, command=mark_completed)
complete_btn.grid(row=1, column=1, padx=5, pady=5)

task_listbox = tk.Listbox(
    root,
    width=45,
    height=15,
    font=("Arial", 12),
    selectbackground="lightblue"
)
task_listbox.pack(pady=10)

load_tasks()

root.mainloop()
