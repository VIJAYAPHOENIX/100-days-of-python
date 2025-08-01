# # import  tkinter
# #
# # window = tkinter.Tk()
# #
# # window.title("my first Gui")
# # window.minsize(width=500,height=300)
# #
# # # ABOUT LABELS
# # my_label = tkinter.Label(text="it is a label",font=("Arial",24,"bold"))
# # my_label.pack()
# #
# # # ABOUT BUTTON
# # def button_click():
# #     print("an action occurred")
# #     print(input1.get())
# #     my_label.config(text="Button got clicked")
# #
# # button = tkinter.Button(text="click here",command= button_click)
# # button.pack(side="bottom")
# #
# # # ABOUT ENTRY OR INPUT SPACE
# # input1 = tkinter.Entry(width=10)
# # input1.insert("end",string="input please")
# # print(input1.get())
# # input1.pack()
# #
# # # ABOUT TEXTBOX
# # text = tkinter.Text(height=5, width=30)
# # #PUTS CURSOR IN TEXTBOX
# # text.focus()
# # #ADD SOME TEXT TO BEGIN WITH.
# # text.insert("end","enter some text or content in multiple lines")
# # #Gets current value in textbox at line "1" character "0"
# # print(text.get("1.0","end"))
# # text.pack()
# #
# # #ABOUT SPINBOX
# # def spinbox_used():
# #     print(spinbox.get())
# #
# # spinbox = tkinter.Spinbox(from_=0, to=10, width=5,command=spinbox_used)
# # spinbox.pack()
# #
# # # ABOUT RADIOBUTTON
# # def radio_used():
# #     print(radio_state.get())
# # # Variable to hold on to which radio button value is checked
# # radio_state = tkinter.IntVar()
# # radiobutton1 = tkinter.Radiobutton(text= "option1",value=1,variable=radio_state,command=radio_used)
# # radiobutton2 = tkinter.Radiobutton(text= "option2",value=2,variable=radio_state,command=radio_used)
# # radiobutton1.pack()
# # radiobutton2.pack()
# #
# #
# # # ABOUT LISTBOX
# # def listbox_used(event):
# #     #Gets current selection from listbox
# #     print(listbox.get(listbox.curselection()))
# #
# # listbox = tkinter.Listbox(height=4)
# # cars = ["Tata","Bmw","Tesla","Ferrari"]
# # for model in cars:
# #     listbox.insert(cars.index(model),model)
# # listbox.bind("<<ListboxSelect>>",listbox_used)
# # listbox.pack()
# # window.mainloop()
# #
# # # # HERE WE ARE DISCUSSING  *args
# # # # def multiply(*args):
# # # #     mul = 1
# # # #     for n in args:
# # # #         mul *= n
# # # #
# # # #     return mul
# # # #
# # # # print(multiply(1,2,3,4))
# # #
# # # # # HERE WE DISCUSSING **kwargs
# # # # def show_profile(**kwargs):
# # # #     for key, value in kwargs.items():
# # # #         print(f"{key} : {value}")
# # # #
# # # #
# # # # show_profile(name = "vijay",age = 23,mood = "focused")
# # #
# # # # # COMBINATION OF BOTH *args AND **kwargs
# # # # def order_summary(*args, **kwargs):
# # # #     total_orders = 0
# # # #     information = " "
# # # #     for n in args:
# # # #         total_orders += n
# # # #
# # # #     for key, value in kwargs.items():
# # # #          information += f"{key} : {value}\n"
# # # #
# # # #     return (f"Total items ordered : {total_orders}\n"
# # # #             f"Customer info:\n"
# # # #             f"{information}")
# # # #
# # # # print(order_summary(2,3,4, name="vijay",address = "Andhra pradesh"))
# # # def order_summary(*args, **kwargs):
# # #     total_orders = ""
# # #     information = " "
# # #     for n in args:
# # #         total_orders += f"{n},"
# # #     total_orders = total_orders.strip(", ")
# # #
# # #     for key, value in kwargs.items():
# # #          information += f"{key} : {value}\n"
# # #
# # #     return (f"Items ordered : {total_orders}\n"
# # #             f"{information}")
# # #
# # # print(order_summary("Shirt","Shoes",total_price = 1200, delivery_method ="Express",payment_method = "UPI"))
#
#
#
# from tkinter import *
# # HERE WE LEARN ABOUT "PLACE", "GRID" AND "PACK".
# # PACK is usually arranges the widgets side by side.
# window = Tk()
# window.title("something")
# window.minsize(width=500, height=300)
#
# #label
# label1 = Label(text="Hello all")
# # label1.pack(side="left")
# # label1.place(x=250, y=150)
# label1.grid(row=0, column=0)
#
# #button
# button1 = Button(text="Click here")
# button2 = Button(text="new button")
# button1.grid(row=1, column=1)
# button2.grid(row=0, column=2)
#
# #entry
# text = Entry(width=10)
# text.grid(row=2, column=3)
#
# window.mainloop()


# MINI PROJECT MLE TO KILOMETER CONVERTER

from tkinter import *

window = Tk()
window.title("Mile to Km converter")
window.config(padx=20, pady=20)

def miles_to_km_converter():
    miles = float(text.get())
    result = miles * 1.609
    label2.config(text=f"is equal to {result} Km")

#Entry
text = Entry(width=10)
text.grid(column=1, row=0)

# Label
label1 = Label(text="Miles")
label2 = Label(text="is equal to 0 Km")
label1.grid(column=2, row=0)
label2.grid(column=1,row=1)

#Button
button = Button(text="Calculate", command= miles_to_km_converter)
button.grid(column=1, row=2)



window .mainloop()