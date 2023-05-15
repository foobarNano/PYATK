import tkinter as tk
from screeninfo import get_monitors
root = tk.Tk()

width = get_monitors()[0].width
height = get_monitors()[0].height

root.title("whatever")
# root.geometry((str)((int)(width/2)) + "x" + (str)((int)(height/2)))
# root.iconbitmap("./bookshelf.ico")

left_frame = tk.Frame(root, borderwidth=4, relief="ridge", width=width/9, height=height/5)
left_frame.pack(side="left", padx=3, pady=3)
left_frame.pack_propagate(0)

right_frame = tk.Frame(root, borderwidth=4, relief="ridge", width=width/5, height=left_frame["height"])
right_frame.pack(side="right", padx=3, pady=3)
right_frame.pack_propagate(0)

label = tk.Label(right_frame, text = "Something interesting")
label.pack()

entry = tk.Entry(left_frame)
entry.pack(anchor="w", padx=5, pady=5)

def change_text():
    e = entry.get()
    job=radio_var.get()
    label.config(text=e+'\n'+job)
    pass

radio_var = tk.StringVar(value=" ")
radio_1 = tk.Radiobutton(left_frame, text="Tester", value="Tester", variable=radio_var)
radio_1.pack(anchor="w", padx=5, pady=5)
radio_2 = tk.Radiobutton(left_frame, text="Programista", value="Programista", variable=radio_var)
radio_2.pack(anchor="w", padx=5, pady=5)

button = tk.Button(left_frame, text = "Ok", command = change_text)
button.pack(anchor="w", padx=5, pady=5)

root.mainloop()