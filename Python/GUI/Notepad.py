from tkinter import *
import os #open and close file meaning 
from tkinter import filedialog
from pathlib import Path 

filename = "*.txt"

root = Tk()
root.title(f"HANNAH NOTEPAD -{filename}")
root.geometry("640x480")
root.resizable(TRUE, TRUE)

def open_file():
    global filename 
    filename = filedialog.askopenfilename(title="Open txt file", 
                                          filetypes=(("Text File", "*.txt"), ("All files", "*.*")),
                                          initialdir="C:\\Users\\user\\Documents\\Python\\GUI")
    if os.path.isfile(filename):
        with open(filename, "r", encoding="utf-8") as file: 
            txt.delete("1.0", END)
            txt.insert(END, file.read())
    filename = Path(filename).stem 
    root.title(f"HANNAH NOTEPAD -{filename}")

def browse_dest_path(): 
    filesave = filedialog.asksaveasfilename(title="Open txt file", 
                                            defaultextension= '.txt',
                                            filetypes=(("Text File", "*.txt"), ("All files", "*.*")),
                                            initialdir="C:\\Users\\user\\Documents\\Python\\GUI")
    if filesave == "": 
        return 
    return filesave 

def save_file(): 
    global filename 
    file_path = browse_dest_path()
    filename = filename = Path(file_path).stem 
    root.title(f"HANNAH NOTEPAD -{filename}")
    with open(file_path, "w", encoding="utf-8") as file: 
            file.write(txt.get("1.0", END))


#Menu Section 
menu = Menu(root)

mymenu_file = Menu(menu, tearoff=0)
mymenu_file.add_command(label="Open", command=open_file)
mymenu_file.add_command(label="Save", command=save_file)
mymenu_file.add_separator()
mymenu_file.add_command(label="Exit", command=root.quit)
menu.add_cascade(label="File", menu=mymenu_file)



#Scrollbar section 
scr = Scrollbar(root)
scr.pack(side="right", fill="y")

# Text Section 
txt = Text(root, yscrollcommand=scr.set)         
txt.pack(fill ="both", expand=True)
txt.insert(END, "Write Text")
scr.config(command=txt.yview)







root.config(menu=menu)
root.mainloop()