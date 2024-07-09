# src/admin_mode.py
from tkinter import Tk, Label, Entry, Button, StringVar, messagebox

# Admin credentials (for simplicity, hardcoded)
ADMIN_PASSWORD = "admin123"
# Use your Own Password 

# Function to activate admin mode
def activate_admin_mode():
    def check_password():
        if password_var.get() == ADMIN_PASSWORD:
            messagebox.showinfo("Admin Mode", "Admin mode activated!")
            root.destroy()
            admin_features()
        else:
            messagebox.showerror("Admin Mode", "Incorrect password. Try again.")

    root = Tk()
    root.title("Admin Mode")

    label = Label(root, text="Enter Admin Password:")
    label.pack()

    password_var = StringVar()
    password_entry = Entry(root, textvariable=password_var, show="*")
    password_entry.pack()

    submit_button = Button(root, text="Submit", command=check_password)
    submit_button.pack()

    root.mainloop()

# Function to provide admin features
def admin_features():
    admin_root = Tk()
    admin_root.title("Admin Features")

    def add_feature():
        messagebox.showinfo("Admin Feature", "Feature added!")

    def delete_feature():
        messagebox.showinfo("Admin Feature", "Feature deleted!")

    add_button = Button(admin_root, text="Add Feature", command=add_feature)
    add_button.pack()

    delete_button = Button(admin_root, text="Delete Feature", command=delete_feature)
    delete_button.pack()

    admin_root.mainloop()

# Test the admin mode function
if __name__ == "__main__":
    activate_admin_mode()
