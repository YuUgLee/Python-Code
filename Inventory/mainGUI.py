import InventoryGUI
from tkinter import *
from tkinter import ttk
from ctypes import windll

windll.shcore.SetProcessDpiAwareness(1)
root = Tk()
root.geometry("500x600")
root.title("Inventory Menu")

root.iconbitmap(default='tsl_logo_side_TMl_icon.ico')
lab = Label(root)
lab.pack()
img=PhotoImage(file='TSL_Logo-SIDE.png')
Label(root,image=img). pack()

# e = Entry(root, width = 120,)
# e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
# label = Label(root, text="", font=('Calibri 15'))
# label.grid(row=1, column=0, columnspan=3, padx=10, pady=10)
def findPartWindow():
    new = Toplevel(root)
    new.title("Part Number Search")
    new.geometry("1300x500")


    label1 = Label(new, text="Enter Part Number:", font=('Calibri 15'))
    label1.pack(pady=20)
    partnum = Entry(new, width=70)
    partnum.pack(pady=20)

    label2 = Label(new, text="",font=("Lucida Console", 10))
    label2.pack(pady=30)

    search = Button(new, text="Search", padx=40, pady=20, command=lambda: findPart(partnum, label2))
    search.pack(pady=10)

#     new.bind('<Return>',lambda: findPart(partnum,new,label2))
#
# def handler(event):
#     label1 = Label(new, text="Enter Part Number:", font=('Calibri 15'))
#     label1.pack(pady=20)

def findPart(partnum, partlabel):

    try:
        number = str(partnum.get())
        number = InventoryGUI.df.iloc[InventoryGUI.findPartNumber(number)]
        number = number.to_string()
    except:
        number = "Part number could not be found. Please try again."
    partlabel.configure(text=number)

button1= Button(root, text="1. Find Part", padx=40, pady=20, command= lambda: findPartWindow())
button1.pack(pady=10)

def addProductWindow():
    new = Toplevel(root)
    new.title("Add Product")
    new.geometry("800x900")

    mainframe = Frame(new)
    mainframe.pack(fill=BOTH, expand=1)
    canvas = Canvas(mainframe)
    canvas.pack(side=LEFT,fill=BOTH,expand=1)

    scrollbar = Scrollbar(mainframe, orient=VERTICAL, command=canvas.yview)
    scrollbar.pack(side=RIGHT, fill=Y)

    canvas.configure(yscrollcommand=scrollbar.set)

    # update scrollregion after starting 'mainloop'
    # when all widgets are in canvas
    canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    # --- put frame in canvas ---

    frame = Frame(canvas)
    canvas.create_window((400,400), window=frame, anchor=CENTER)

    label1 = Label(frame, text="Enter Name:", font=('Calibri 12'))
    label1.pack(pady=10)
    name = Entry(frame, width=50)
    name.pack(pady=10)
    label2 = Label(frame, text="Enter Location:", font=('Calibri 12'))
    label2.pack(pady=10)
    location = Entry(frame, width=50)
    location.pack(pady=10)
    label3 = Label(frame, text="Enter Part Number:", font=('Calibri 12'))
    label3.pack(pady=10)
    partnum = Entry(frame, width=50)
    partnum.pack(pady=10)
    label5 = Label(frame, text="Enter Decryption:", font=('Calibri 12'))
    label5.pack(pady=10)
    decrypt = Entry(frame, width=50)
    decrypt.pack(pady=10)
    label8 = Label(frame, text="Enter Serial Number:", font=('Calibri 12'))
    label8.pack(pady=10)
    serial = Entry(frame, width=50)
    serial.pack(pady=10)
    label4 = Label(frame, text="Enter Quantity:", font=('Calibri 12'))
    label4.pack(pady=10)
    quantity = Entry(frame, width=50)
    quantity.pack(pady=10)

    label6 = Label(frame, text="Enter Note:", font=('Calibri 12'))
    label6.pack(pady=10)
    note = Text(frame, width=50, height=5)
    note.pack(pady=10)
    label7 = Label(frame, text="", font=('Calibri 12'))
    label7.pack(pady=10)
    add = Button(frame, text="Add Product", padx=40, pady=20, command=lambda: addProduct(name,location,partnum,quantity,decrypt,note,label7,serial))
    add.pack(pady=10)

def addProduct(name,location,partnum,quantity,decrypt,note,label7,serial):
    try:
        name1 = str(name.get())
        loc = str(location.get())
        part = str(partnum.get()).upper()
        qty = int(quantity.get())
        decrypt1 = str(decrypt.get())
        serial1 = str(serial.get()).upper()
        note1 = str(note.get("1.0",END))
        name.delete(0,END)
        location.delete(0,END)
        partnum.delete(0,END)
        quantity.delete(0,END)
        decrypt.delete(0,END)
        serial.delete(0,END)
        note.delete("1.0",END)
        InventoryGUI.addProduct(name1, loc, part, qty, decrypt1, note1,serial1,label7)
    except:
        label7.configure(text="Unable to add product!")


button2= Button(root, text="2. Add Product", padx=40, pady=20, command= lambda: addProductWindow())
button2.pack(pady=10)


def deleteProductWindow():
    new = Toplevel(root)
    new.title("Delete Product")
    new.geometry("1000x500")
    label1 = Label(new, text="Enter Part Number:", font=('Calibri 15'))
    label1.pack(pady=10)
    partnum = Entry(new, width=70)
    partnum.pack(pady=10)
    label2 = Label(new, text="", font=("Lucida Console", 10))
    label2.pack(pady=10)
    search = Button(new, text="Search", padx=40, pady=20, command=lambda: findPart(partnum,label2))
    search.pack(pady=10)
    delete = Button(new, text="Delete", padx=40, pady=20, command=lambda: InventoryGUI.deleteProduct((partnum.get()),new,label2))
    delete.pack(pady=10)


def deleteProduct(partnum,new, partlabel):

    try:
        number = str(partnum.get())
        number = InventoryGUI.df.loc[InventoryGUI.findPartNumber(number)]

        number = str(number)
    except:
        number = "Part number could not be found. Please try again."
    partlabel.configure(text=number)

button3= Button(root, text="3. Delete Product", padx=40, pady=20, command= lambda: deleteProductWindow())
button3.pack(pady=10)

def editProductWindow():
    new = Toplevel(root)
    new.title("Edit Product")
    new.geometry("800x1050")

    mainframe = Frame(new)
    mainframe.pack(fill=BOTH, expand=1)
    canvas = Canvas(mainframe)
    canvas.pack(side=LEFT, fill=BOTH, expand=1)

    scrollbar = Scrollbar(mainframe, orient=VERTICAL, command=canvas.yview)
    scrollbar.pack(side=RIGHT, fill=Y)

    canvas.configure(yscrollcommand=scrollbar.set)

    # update scrollregion after starting 'mainloop'
    # when all widgets are in canvas
    canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    # --- put frame in canvas ---

    frame = Frame(canvas)
    canvas.create_window((400, 400), window=frame, anchor=CENTER)

    l1 = Label(frame, text="Enter Part Number:", font=('Calibri 15'))
    l1.pack(pady=20)
    partnum = Entry(frame, width=70)
    partnum.pack(pady=20)

    l2 = Label(frame, text="", font=("Lucida Console", 10))
    l2.pack(pady=10)

    l3 = Label(frame, text="", font=("Lucida Console", 10))
    l3.pack(pady=10)
    search = Button(frame, text="Search", padx=40, pady=20, command=lambda: findPartEdit(partnum,name,location,pn,quantity,decrypt,note,l2,l3,new,serial,edit,label1,label2,label3,label4,label5,label6,label8))
    search.pack(pady=10)

    label1 = Label(frame, text="Edit Name:", font=('Calibri 12'))
    label1.pack(pady=10)
    name = Entry(frame, width=50)
    name.pack(pady=10)
    label2 = Label(frame, text="Edit Location:", font=('Calibri 12'))
    label2.pack(pady=10)
    location = Entry(frame, width=50)
    location.pack(pady=10)
    label3 = Label(frame, text="Edit Part Number:", font=('Calibri 12'))
    label3.pack(pady=10)
    pn = Entry(frame, width=50)
    pn.pack(pady=10)
    label5 = Label(frame, text="Edit Decryption:", font=('Calibri 12'))
    label5.pack(pady=10)
    decrypt = Entry(frame, width=50)
    decrypt.pack(pady=10)
    label8 = Label(frame, text="Edit Serial Number:", font=('Calibri 12'))
    label8.pack(pady=10)
    serial = Entry(frame, width=50)
    serial.pack(pady=10)
    label4 = Label(frame, text="Edit Quantity:", font=('Calibri 12'))
    label4.pack(pady=10)
    quantity = Entry(frame, width=50)
    quantity.pack(pady=10)

    label6 = Label(frame, text="Edit Note:", font=('Calibri 12'))
    label6.pack(pady=10)
    note = Text(frame, width=50, height=5)
    note.pack(pady=10)
    # label7 = Label(frame, text="", font=('Calibri 12'))
    # label7.pack(pady=10)
    edit = Button(frame, text="Edit Product", padx=40, pady=20, command=lambda: editValues(partnum, l2, l3, name, location, pn, quantity, decrypt, note, edit, serial))
    edit.pack(pady=10)

    label1.pack_forget()
    label2.pack_forget()
    label3.pack_forget()
    label5.pack_forget()
    label8.pack_forget()
    label4.pack_forget()
    label6.pack_forget()
    name.pack_forget()
    location.pack_forget()
    pn.pack_forget()
    decrypt.pack_forget()
    serial.pack_forget()
    quantity.pack_forget()
    note.pack_forget()
    edit.pack_forget()

def editValues(partnum, l2, l3, name, loc, pn, qty, decrypt, note,edit,serial):

    float(qty.get())
    InventoryGUI.changeName(str(partnum.get()).upper(),str(name.get()))
    InventoryGUI.changeLocation(str(partnum.get()).upper(),str(loc.get()))

    InventoryGUI.changeQuantity(str(partnum.get()).upper(),float(qty.get()))
    InventoryGUI.changeDecryption(str(partnum.get()).upper(),str(decrypt.get()))
    InventoryGUI.changeSerial(str(partnum.get()).upper(), str(serial.get()).upper())
    InventoryGUI.changeNote(str(partnum.get()).upper(),str(note.get("1.0",END)).rstrip("\n"))
    InventoryGUI.changePartNumber(str(partnum.get()).upper(),str(pn.get()).upper())
    l2.configure(text = "Part Number: %s has been edited and saved!" % str(partnum.get()).upper())
    l3.configure(text ="")
    editProductEntries(name,loc,pn,qty,decrypt,note, partnum,serial)
    edit.pack_forget()


def findPartEdit(partnum,name,location,pn,quantity,decrypt,note,l2,l3,new,serial,edit,label1,label2,label3,label4,label5,label6,label8):
    verify = True
    name.delete(0, END)
    location.delete(0, END)
    pn.delete(0, END)
    decrypt.delete(0, END)
    serial.delete(0, END)
    quantity.delete(0, END)
    note.delete('1.0', END)

    number = str(partnum.get()).upper()
    number = InventoryGUI.findPartNumber(number)
    # If Part number does not exist
    if number == False:
        verify = False
        number = "Part number could not be found. Please try again."
        l2.configure(text = number)

    # If Part number exists
    # Show all edit entries and edit button
    # Auto fill with Part number information
    if verify == True:

        label1.pack(pady=3)
        name.pack(pady=3)
        label2.pack(pady=3)
        location.pack(pady=3)
        label3.pack(pady=3)
        pn.pack(pady=3)
        label5.pack(pady=3)
        decrypt.pack(pady=3)
        label8.pack(pady=3)
        serial.pack(pady=3)
        label4.pack(pady=3)
        quantity.pack(pady=3)
        label6.pack(pady=3)
        note.pack(pady=3)

        name.insert(0, str(InventoryGUI.df.iat[number[0], 0]))
        location.insert(0, str(InventoryGUI.df.iat[number[0], 1]))
        pn.insert(0, str(InventoryGUI.df.iat[number[0], 2]).upper())
        decrypt.insert(0, str(InventoryGUI.df.iat[number[0], 3]))
        serial.insert(0, str(InventoryGUI.df.iat[number[0], 4]).upper())
        quantity.insert(0, str(InventoryGUI.df.iat[number[0], 5]))
        note.insert(END, str(InventoryGUI.df.iat[number[0], 6]))
        number = InventoryGUI.df.iloc[number]

        l2.configure(text = number)
        l3.configure(text="Please change the following to edit Part Number: %s" %str(partnum.get()).upper())
        edit.pack()


def editProductEntries(name,location,pn,quantity,decrypt,note,partnum,serial):
    partnum.delete(0, END)
    name.delete(0,END)
    location.delete(0,END)
    pn.delete(0, END)
    quantity.delete(0,END)
    decrypt.delete(0,END)
    serial.delete(0,END)
    note.delete("1.0",END)


button4= Button(root, text="4. Edit Product", padx=40, pady=20, command= lambda: editProductWindow())
button4.pack(pady=10)

def viewWindow():
    new = Toplevel(root)
    new.title("View Items")
    new.geometry("1100x700")

    mainframe = Frame(new)
    mainframe.pack(fill=BOTH, expand=1)
    canvas = Canvas(mainframe)
    canvas.pack(side=LEFT, fill=BOTH, expand=1)

    scrollbar = Scrollbar(mainframe, orient=VERTICAL, command=canvas.yview)
    scrollbar.pack(side=RIGHT, fill=Y)

    canvas.configure(yscrollcommand=scrollbar.set)

    # update scrollregion after starting 'mainloop'
    # when all widgets are in canvas
    canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    # --- put frame in canvas ---

    frame = Frame(canvas)
    canvas.create_window((550, 0), window=frame, anchor=CENTER)

    text_box = Text(frame,height=20,width=80,wrap=NONE,font=("Lucida Console", 15))
    text_box.grid(row=0, column=0)
    sb = Scrollbar(frame,orient=VERTICAL)
    sb.grid(row=0, column=1, sticky=NS)

    sb.config(command=text_box.yview)

    sb1 = Scrollbar(frame, orient=HORIZONTAL)
    sb1.grid(row=1, column=0, sticky=EW)
    sb1.config(command=text_box.xview)

    text_box.config(bg='#D9D8D7',xscrollcommand=sb1.set, yscrollcommand=sb.set)
    text_box.insert(END,InventoryGUI.df.to_string())

    refresh1 = Button(frame, text="Refresh Dataframe", padx=40, pady=20, command=lambda: refresh(text_box))
    refresh1.grid(row = 2, column = 0)

def refresh(text):
    text.delete('1.0', END)
    InventoryGUI.refreshDataFrame()
    text.insert(END,InventoryGUI.df.to_string())

button5= Button(root, text="5. View Items", padx=40, pady=20, command= lambda: viewWindow())
button5.pack(pady=10)

root.mainloop()