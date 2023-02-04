import tkinter as tk
from tkinter import ttk

class MyFiler(tk.Frame):
    def __init__(self, master = None):
        super().__init__(master)

        self.master.geometry("600x400")

        ## toolbar of drives
        f_toolbar = tk.Frame(self.master)
        btn1 = tk.Button(f_toolbar, text="sample1")
        btn1.pack(side=tk.LEFT)

        f_toolbar.pack(fill = tk.X)

        ## left culumn
        left_frame = tk.Frame(self.master, relief = tk.SUNKEN)
        dir_tree = ttk.Treeview(left_frame)
        dir_tree.pack()
        left_frame.pack(side = tk.LEFT, fill = tk.Y)

# root = tk.Tk()

# root.title("my filer py")

# tree = ttk.Treeview(root)

# parent = tree.insert("", "end", text="parent")

# child = tree.insert(parent, "end", text="child")

# tree.pack()
# root.mainloop()

if __name__ == '__main__':
    root = tk.Tk()
    app = MyFiler(master = root)
    app.mainloop()
    
