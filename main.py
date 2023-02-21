import tkinter as tk
import tkinter.ttk as ttk
from tkinter import filedialog, messagebox
import os

def login():
    username = username_entry.get()
    password = password_entry.get()
    if username == "admin" and password == "password":
        # successful login, show main window
        root.destroy()
        show_main_window()
    else:
        # failed login, show error message
        error_label.config(text="Invalid username or password")

def show_main_window():
    # create the main window
    main_window = tk.Tk()
    main_window.title("Main Window")
    main_window.geometry("600x400")

    # create the style for modern-looking widgets
    style = ttk.Style()
    style.theme_use("clam")
    style.configure("TButton", foreground="#333", background="#ccc", font=("Helvetica", 12), padding=10)
    style.configure("Red.TButton", foreground="#fff", background="#f00")

    # add the three buttons for "Folder", "Marker", and "Other" actions
    folder_button = ttk.Button(main_window, text="Folder Marker", command=create_folders, style="Red.TButton")
    folder_button.pack(pady=10)
    marker_button = ttk.Button(main_window, text="Soon", command=coming_soon, style="TButton")
    marker_button.pack(pady=10)
    other_button = ttk.Button(main_window, text="Soon", command=coming_soon, style="TButton")
    other_button.pack(pady=10)

    # start the GUI main loop
    main_window.mainloop()

def create_folders():
    # ask the user to select a directory
    directory = filedialog.askdirectory()
    if not directory:
        return
    # ask the user how many folders to create and what to name them
    num_folders = tk.simpledialog.askinteger("Create Folders", "How many folders do you want to create?")
    if not num_folders:
        return
    folder_name = tk.simpledialog.askstring("Create Folders", "What should the folder name be?")
    if not folder_name:
        return
    # create the folders with the given name and number
    for i in range(num_folders):
        folder_path = f"{directory}/{folder_name}{i+1}"
        try:
            os.mkdir(folder_path)
        except Exception as e:
            messagebox.showerror("Error", f"Could not create folder '{folder_path}': {e}")
            return
    # show success message
    messagebox.showinfo("Success", f"Created {num_folders} folders named '{folder_name}' in '{directory}'")

def coming_soon():
    messagebox.showinfo("Coming Soon", "This feature is coming soon.")

# create the login window
root = tk.Tk()
root.title("Login")
root.geometry("600x400")

# add username and password input fields
username_label = ttk.Label(root, text="Username")
username_label.pack(pady=10)
username_entry = ttk.Entry(root)
username_entry.pack(pady=10)
password_label = ttk.Label(root, text="Password")
password_label.pack(pady=10)
password_entry = ttk.Entry(root, show="*")
password_entry.pack(pady=10)

# add login button and error message label
login_button = ttk.Button(root, text="Login", command=login)
login_button.pack(pady=10)
error_label = ttk.Label(root, text="", foreground="red")
error_label.pack(pady=10)

# hide the console window when running the .exe file
# by creating a hidden console
# you can remove this line to show the console for debugging
# or use the "windowed" option to create a completely windowed application
# instead of a console application
# (see PyInstaller documentation for more information)
import ctypes
ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)

# start the GUI main loop
root.mainloop()

