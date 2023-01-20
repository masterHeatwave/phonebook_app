from tkinter import *
from tkinter import ttk

# defining colors

white = "#ffffff"
black = "#000000"
blue = "#191970"
crimson = "#DC143C"

# creating a window

window = Tk()
window.title("")
window.geometry('600x450')
window.configure(background=white)
window.resizable(height=FALSE, width=FALSE)

# frames

frame_up = Frame(window, width=600, height=50, bg=blue)
frame_up.grid(row=0, column=0, padx=0, pady=1)

frame_down = Frame(window, width=600, height=150, bg=white)
frame_down.grid(row=1, column=0, padx=0, pady=1)

frame_table = Frame(window, width=600, height=100, bg=white)
frame_table.grid(row=2, column=0, columnspan=2, padx=0, pady=1, sticky=NW)


# creating a table to show the data
def show():

    global tree

    listheader = ['Name', 'Telephone', 'E-mail']

    demo_list = [['Someone', '1123581321', 'someones@gmail.com']]

    tree = ttk.Treeview(frame_table, selectmode="extended", columns=listheader, show="headings")

    vsb = ttk.Scrollbar(frame_table, orient="vertical", command=tree.yview)
    hsb = ttk.Scrollbar(frame_table, orient="horizontal", command=tree.xview)

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

    tree.grid(column=0, row=0, sticky='nsew')
    vsb.grid(column=1, row=0, sticky='ns')
    hsb.grid(column=0, row=1, sticky='ew')

    # tree head

    tree.heading(0, text='Name', anchor=NW)
    tree.heading(1, text='Telephone', anchor=NW)
    tree.heading(2, text='E-mail', anchor=NW)

    # tree column

    tree.column(0, width=120, anchor='nw')
    tree.column(1, width=120, anchor='nw')
    tree.column(2, width=160, anchor='nw')

    for item in demo_list:
        tree.insert('', 'end', values=item)


show()


# frame_up widgets

app_name = Label(frame_up, text="Phonebook", height=1, font='Trebuchet 14 bold', bg=blue, fg=white)
app_name.place(x=5, y=5)

# frame_down widgets

l_name = Label(frame_down, text="Name", width=20, height=1, font='Ivy 10', bg=white, anchor=NW)
l_name.place(x=10, y=20)
e_name = Entry(frame_down, width=25, justify='left', highlightthickness=1, relief="solid")
e_name.place(x=80, y=20)

l_telephone = Label(frame_down, text="Telephone", width=20, height=1, font='Ivy 10', bg=white, anchor=NW)
l_telephone.place(x=10, y=50)
e_telephone = Entry(frame_down, width=25, justify='left', highlightthickness=1, relief="solid")
e_telephone.place(x=80, y=50)

l_email = Label(frame_down, text="E-mail", width=20, height=1, font='Ivy 10', bg=white, anchor=NW)
l_email.place(x=10, y=80)
e_email = Entry(frame_down, width=25, justify='left', highlightthickness=1, relief="solid")
e_email.place(x=80, y=80)

b_search = Button(frame_down, text="Search", width=10, height=1, bg=white, font='Ivy 8 bold')
b_search.place(x=290, y=20)
e_search = Entry(frame_down, width=16, justify='left', highlightthickness=1, relief="solid")
e_search.place(x=390, y=20)

b_view = Button(frame_down, text="View", width=10, height=1, justify='left', bg=white, font='Ivy 8 bold')
b_view.place(x=290, y=50)

# creating add, delete update buttons

b_add = Button(frame_down, text="Add", width=10, height=1, justify='left', bg=blue, fg=white, font='Ivy 8 bold')
b_add.place(x=290, y=80)

b_delete = Button(frame_down, text="Delete", width=10, height=1, justify='left', fg=white, bg=blue, font='Ivy 8 bold')
b_delete.place(x=380, y=80)

b_update = Button(frame_down, text="Update", width=10, height=1, justify='left', fg=white, bg=blue, font='Ivy 8 bold')
b_update.place(x=470, y=80)

window.mainloop()
