import tkinter as tk
from ques5 import add_book,view_book,issue_book,return_book
root=tk.Tk()
root.title("====library management system===")
root.geometry("400x350")
tk.Label(root,text="Library Management System",font=("arial",16,"bold")).pack(pady=20)
tk.Button(root,text="Add Book",width=20,command=add_book).pack(pady=5)
tk.Button(root,text="Issue Book",width=20,command=issue_book).pack(pady=5)
tk.Button(root,text="Return Book",width=20,command=return_book).pack(pady=5)
tk.Button(root,text="Views Book",width=20,command=view_book).pack(pady=5)
tk.Button(root,text="Exit",width=20,command=root.destroy).pack(pady=5)
root.mainloop()