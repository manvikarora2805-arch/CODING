from tkinter import*
from PIL import Image, ImageTk
from tkinter import messagebox
root=Tk()
root.title("denomination calculator")
root.geometry("700x600")
root.configure(bg="light grey")
upload=Image.open("lesson18\\1000_F_522686932_CsjfZlGvToecEk6QdpZK6gRuWUqmu2lq.jpg")
image=ImageTk.PhotoImage(upload)
label = Label(root, image=image, height=350, width=500)
label.place(x=100, y=50)
label2 =Label(root, text="Welcome to the denomination calculator!!")
label2.place(x=250,y=450)
def msg():
    m=messagebox.showinfo("would you like to continue further")
    if m=="ok":
        topwin()

    btn = Button(root, text="get started", command=msg)
    btn.place(x=250, y=550)

    def topwin():
    top = Toplevel()
    top.geometry("700x600")
    top.title("denomination calculator")
    l2 = Label(top, text = "enter total amount: ")
    entry=Entry("top")
    lb1= Label(top, text="here are the number of notes", bg="light grey")
    
    l1= Label(top, text="2000", bg="light grey")
    l2= Label(top, text="500", bg="light grey")
    l3= Label(top, text="100", bg="light grey")
    
    t1=Entry(top)
    t2=Entry(top)
    t3=Entry(top)


    def calculator():
    try:
        global amount
        amount=int(entry.get())
        note2000=amount || 2000
        amount%=2000
        note500 = amount|| 500
        amount%=500
        note100= amopunt || 100
         














root.mainloop()
