# import modules
from tkinter import *
from converter import EngtoHindi

# object of tkinter
# and background set for grey
master = Tk()
master.title('English to Hindi Translator')
master.geometry("1540x200")
master.configure(bg='#AED6F1')

# Variable Classes in tkinter
result = StringVar()

e = Entry(master, width=90, font=("Arial", 25))
e.grid(row=0, column=1)

# Creating label for each information
# name using widget Label
Label(master, text="English Text : ", bg='#AED6F1', font=("Arial", 25)).grid(row=0, sticky=W)
Label(master, text="Hindi Text :", bg='#AED6F1', font=("Arial", 25)).grid(row=6, sticky=W)

# Creating label for class variable
# name using widget Entry
Label(master, text="", textvariable=result, bg="#FAD7A0", font=("Arial", 25)).grid(row=6,
                                                                                   column=1,
                                                                                   sticky=W)


# user define function
def eng_to_hindi():
    trans = EngtoHindi(str(e.get()))
    res = trans.convert
    result.set(res)


# creating a button using the widget
# Button that will call the submit function
b = Button(master, text="Translate", command=eng_to_hindi, bg="#1A5276",font=("Arial", 13))
b.grid(row=0, column=2, columnspan=2, rowspan=2, padx=2, pady=2, )

mainloop()
