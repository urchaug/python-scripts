from tkinter import *
def Temperature_conversion():
    temp = int((var.get() - 32) * 5/9)
    convert = str(temp) + " Celcius"
    label2.config(text = convert)

root =Tk()
root.title("Temperature Converter")
root.resizable(0,0)

var = DoubleVar()

label1 = Label(root, text = "Temperature Converter\nFahrenheit to Celcius",padx=16,pady=16,bd=16,
               fg="#000000",font=('arial',30,'bold'),bg="bisque1", relief= 'raise',
               width=20, height=3)
label1.pack()

slider = Scale(root, variable=var, from_=-40, to =300, length=500, tickinterval=20, orient=HORIZONTAL)
slider.pack(anchor = CENTER)



label2 = Label(root,padx=16,pady=16,bd=16,fg="#000000",font=('arial',30,'bold'),
               bg="bisque1", relief= 'sunk',
               width=20, height=3)
label2.pack()


label3 = Label(root, text = "  ")
label3.pack()

button = Button(root, text="convert to celsius",padx=16,pady=16,bd=16, width = 20,
                font=('arial',20, 'bold'),command=Temperature_conversion)


                
button.pack(anchor = CENTER)

root.mainloop()
