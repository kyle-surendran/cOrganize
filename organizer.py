import tkinter as tk
from tkinter import messagebox, filedialog, font
import os

class TaskManager:
    def __init__(self, root):
        self.root = root
        self.root.title("cOrganize")
        self.tasks = []

        # Main frame
        self.frame = tk.Frame(root)
        self.frame.pack(padx=10, pady=10)

        # Task list
        self.task_listbox = tk.Listbox(self.frame, width=40, height=15, selectmode=tk.SINGLE)
        self.task_listbox.pack(side=tk.LEFT, padx=5)

        # Scrollbar for the list
        self.scrollbar = tk.Scrollbar(self.frame, orient=tk.VERTICAL, command=self.task_listbox.yview)
        self.scrollbar.pack(side=tk.LEFT, fill=tk.Y)
        self.task_listbox.config(yscrollcommand=self.scrollbar.set)

        # Buttons frame
        self.button_frame = tk.Frame(root)
        self.button_frame.pack(pady=10)

        self.defaultFont = font.nametofont("TkDefaultFont") 
  
        # Overriding default-font with custom settings 
        # i.e changing font-family, size and weight 
        self.defaultFont.configure(family="Trebuchet MS",size=14, weight=font.BOLD) 
        
        # Entry for new tasks
        self.task_entry = tk.Entry(self.button_frame, width=30)
        self.task_entry.grid(row=0, column=0, padx=5)

        self.add_button = tk.Button(self.button_frame, text="Add Task", command=self.add_task)
        self.add_button.grid(row=0, column=1, padx=5)

        self.delete_button = tk.Button(self.button_frame, text="Delete Task", command=self.delete_task)
        self.delete_button.grid(row=1, column=0, pady=5)

        self.complete_button = tk.Button(self.button_frame, text="Mark as Done", command=self.mark_done)
        self.complete_button.grid(row=1, column=1, pady=5)

        self.save_button = tk.Button(self.button_frame, text="Save Tasks", command=self.save_tasks)
        self.save_button.grid(row=2, column=0, pady=5)

        self.load_button = tk.Button(self.button_frame, text="Load Tasks", command=self.load_tasks)
        self.load_button.grid(row=2, column=1, pady=5)

    def add_task(self):
        task = self.task_entry.get().strip()
        if task:
            self.tasks.append(task)
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Please enter a task!")

    def delete_task(self):
        selected = self.task_listbox.curselection()
        if selected:
            index = selected[0]
            self.tasks.pop(index)
            self.task_listbox.delete(index)
        else:
            messagebox.showwarning("Selection Error", "Please select a task to delete!")

    def mark_done(self):
        selected = self.task_listbox.curselection()
        if selected:
            index = selected[0]
            task = self.tasks[index]
            self.tasks[index] = f"{task} (Done)"
            self.task_listbox.delete(index)
            self.task_listbox.insert(index, self.tasks[index])
        else:
            messagebox.showwarning("Selection Error", "Please select a task to mark as done!")

    def save_tasks(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if file_path:
            with open(file_path, "w") as file:
                file.write("\n".join(self.tasks))
            messagebox.showinfo("Save Successful", f"Tasks saved to {file_path}!")

    def load_tasks(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if file_path and os.path.exists(file_path):
            with open(file_path, "r") as file:
                self.tasks = file.read().splitlines()
            self.task_listbox.delete(0, tk.END)
            for task in self.tasks:
                self.task_listbox.insert(tk.END, task)
            messagebox.showinfo("Load Successful", f"Tasks loaded from {file_path}!")

if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManager(root)
    root.mainloop()

