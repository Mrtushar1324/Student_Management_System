import tkinter as tk
from tkinter import ttk, messagebox

class StudentManagement:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Management System")
        self.root.geometry("1350x700+0+0")

        # Title
        title = tk.Label(self.root, text="Student Management System", bd=10, relief=tk.GROOVE, 
                         font=("times new roman", 40, "bold"), bg="yellow", fg="red")
        title.pack(side=tk.TOP, fill=tk.X)

        # --- Manage Frame (Left Side for Inputs) ---
        Manage_Frame = tk.Frame(self.root, bd=4, relief=tk.RIDGE, bg="crimson")
        Manage_Frame.place(x=20, y=100, width=450, height=580)

        m_title = tk.Label(Manage_Frame, text="Manage Students", bg="crimson", fg="white", 
                           font=("times new roman", 30, "bold"))
        m_title.grid(row=0, columnspan=2, pady=20)

        # Labels aur Entry Fields
        lbl_roll = tk.Label(Manage_Frame, text="Roll No.", bg="crimson", fg="white", font=("times new roman", 20, "bold"))
        lbl_roll.grid(row=1, column=0, pady=10, padx=20, sticky="w")
        txt_roll = tk.Entry(Manage_Frame, font=("times new roman", 15, "bold"), bd=5, relief=tk.GROOVE)
        txt_roll.grid(row=1, column=1, pady=10, padx=20, sticky="w")

        lbl_name = tk.Label(Manage_Frame, text="Name", bg="crimson", fg="white", font=("times new roman", 20, "bold"))
        lbl_name.grid(row=2, column=0, pady=10, padx=20, sticky="w")
        txt_name = tk.Entry(Manage_Frame, font=("times new roman", 15, "bold"), bd=5, relief=tk.GROOVE)
        txt_name.grid(row=2, column=1, pady=10, padx=20, sticky="w")

        # --- Button Frame ---
        btn_frame = tk.Frame(Manage_Frame, bd=4, relief=tk.RIDGE, bg="crimson")
        btn_frame.place(x=15, y=500, width=410)

        add_btn = tk.Button(btn_frame, text="Add", width=10).grid(row=0, column=0, padx=10, pady=10)
        update_btn = tk.Button(btn_frame, text="Update", width=10).grid(row=0, column=1, padx=10, pady=10)
        delete_btn = tk.Button(btn_frame, text="Delete", width=10).grid(row=0, column=2, padx=10, pady=10)
        clear_btn = tk.Button(btn_frame, text="Clear", width=10).grid(row=0, column=3, padx=10, pady=10)

        # --- Detail Frame (Right Side for Table) ---
        Detail_Frame = tk.Frame(self.root, bd=4, relief=tk.RIDGE, bg="crimson")
        Detail_Frame.place(x=500, y=100, width=800, height=580)

root = tk.Tk()
obj = StudentManagement(root)
root.mainloop()