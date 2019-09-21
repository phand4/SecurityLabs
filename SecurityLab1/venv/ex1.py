from tkinter import*

clcltr = Tk()
clcltr.title("Calculator")
operator=""
text_Input =StringVar()

def btnClick(numbers):
    global operator
    operator = operator + str(numbers)
    text_Input.set(operator)

def btnClear():
    global operator
    operator=""
    text_Input.set("")

def btnEquals():
    global operator
    result=str(eval(operator))
    text_Input.set(result)
    operator=""



txtDisplay = Entry(clcltr,
                   font=('Calibri', 20, 'bold'),
                   textvariable=text_Input,
                   bd=30,
                   insertwidth=4,
                   bg="LightGoldenrod1",
                   justify='right').grid(columnspan=4)

btn7 = Button(clcltr,
              padx=10,
              bd=8,
              fg="black",
              font=('Calibri',18, 'bold'),
              text="7",
              command=lambda:btnClick(7)
              ).grid(row=1,column=0)

btn8 = Button(clcltr,
              padx=10,
              bd=8,
              fg="black",
              font=('Calibri',18, 'bold'),
              text="8",
              command=lambda:btnClick(8)
              ).grid(row=1,column=1)

btn9 = Button(clcltr,
              padx=10,
              bd=8,
              fg="black",
              font=('Calibri',18, 'bold'),
              text="9",
              command=lambda:btnClick(9)
              ).grid(row=1,column=2)

btn4 = Button(clcltr,
              padx=10,
              bd=8,
              fg="black",
              font=('Calibri',18, 'bold'),
              text="4",
              command=lambda: btnClick(4)
              ).grid(row=2,column=0)

btn5 = Button(clcltr,
              padx=10,
              bd=8,
              fg="black",
              font=('Calibri',18, 'bold'),
              text="5",
              command=lambda: btnClick(5)
              ).grid(row=2,column=1)

btn6 = Button(clcltr,
              padx=10,
              bd=8,
              fg="black",
              font=('Calibri',18, 'bold'),
              text="6",
              command=lambda: btnClick(6)
              ).grid(row=2,column=2)

btn1 = Button(clcltr,
              padx=10,
              bd=8,
              fg="black",
              font=('Calibri',18, 'bold'),
              text="1",
              command=lambda: btnClick(1)
              ).grid(row=3,column=0)

btn2 = Button(clcltr,
              padx=10,
              bd=8,
              fg="black",
              font=('Calibri',18, 'bold'),
              text="2",
              command=lambda: btnClick(2)
              ).grid(row=3,column=1)

btn3 = Button(clcltr,
              padx=10,
              bd=8,
              fg="black",
              font=('Calibri',18, 'bold'),
              text="3",
              command=lambda: btnClick(3)
              ).grid(row=3,column=2)

btn0 = Button(clcltr,
              padx=10,
              bd=8,
              fg="black",
              font=('Calibri',18, 'bold'),
              text="0",
              command=lambda: btnClick(0)
              ).grid(row=4,column=1)

btncc = Button(clcltr,
              padx=10,
              bd=8,
              fg="black",
              font=('Calibri',18, 'bold'),
              text="Cc",
              command= btnClear
              ).grid(row=4,column=0)

btnequal = Button(clcltr,
              padx=10,
              bd=8,
              fg="black",
              font=('Calibri',18, 'bold'),
              text="=",
              command= btnEquals
              ).grid(row=4,column=2)

btndiv = Button(clcltr,
              padx=10,
              bd=8,
              fg="black",
              font=('Calibri',18, 'bold'),
              text="÷",
              command=lambda: btnClick("/")
              ).grid(row=1,column=3)

btnmult = Button(clcltr,
              padx=10,
              bd=8,
              fg="black",
              font=('Calibri',18, 'bold'),
              text="x",
              command=lambda: btnClick("*")
              ).grid(row=2,column=3)

btnmin = Button(clcltr,
              padx=10,
              bd=8,
              fg="black",
              font=('Calibri',18, 'bold'),
              text="-",
              command=lambda: btnClick("-")
              ).grid(row=3,column=3)

btnplus = Button(clcltr,
              padx=10,
              bd=8,
              fg="black",
              font=('Calibri',18, 'bold'),
              text="+",
            command=lambda: btnClick("+")
              ).grid(row=4,column=3)





clcltr.mainloop()