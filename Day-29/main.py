from tkinter import *
from tkinter import messagebox as mg
from random import randint, choice, shuffle
import pyperclip
FONT_NAME = "Times New Roman"
Grey_black = "#000000"
# =========================PASSWORD MECHANISM==================
def generate_password():
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k',
                'l','m','n','o','p','q','r','s','t','u','v',
                'w','x','y','z']
    numbers = ['1','2','3','4','5','6','7','8','9','0']
    symbols = ['!','#','$','%','&','(',')','*','+']

    number = [choice(numbers) for num in range(randint(2, 4))]
    letters = [choice(alphabet) for char in range(randint(8, 10))]
    symb = [choice(symbols) for sym in range(randint(2, 4))]

    password_list = number + letters + symb
    shuffle(password_list)

    password = "".join(password_list)
    password_input.insert(0,password)
    pyperclip.copy(password)

# =======================SAVE DATA=========================
def save_data():
    website = website_input.get()
    username = user_email_input.get()
    password = password_input.get()
    if len(website) != 0 :
        if len(username) != 0 :
            if len(password) != 0:
                is_ok = mg.askokcancel(title="Check the details below before proceeding",
                                       message=f"website : {website}\n"
                                               f"username : {username}\n"
                                               f"password : {password}")
                if is_ok:
                    details = f"{website}  |  {username}  |  {password}\n"
                    with open("details_info.txt", mode="a") as data:
                        data.write(details)
                        website_input.delete(0,END)
                        password_input.delete(0, END)
            else:
                mg.showwarning(title="Error", message="password shouldn't be empty")
        else:
            mg.showwarning(title="Error", message="username/Email shouldn't be empty")
    else:
        mg.showwarning(title="Error", message="website shouldn't be empty")

# =================UI INTERFACE==================
page = Tk()
page.title("PASSWORD MANAGER")
page.config(padx=50, pady=50, bg=Grey_black)

# IMAGE PART
canvas = Canvas(width=200, height=200, bg=Grey_black, highlightthickness=0)
image = PhotoImage(file="lock.png")
canvas.create_image(100, 100, image=image)
canvas.grid(column=1, row=0)

# LABELS PART
email_text = Label(text="Email/Username",fg="white", bg=Grey_black, font=(FONT_NAME, 10, "bold"))
password_text = Label(text="Password",fg="white", bg=Grey_black, font=(FONT_NAME, 10, "bold"))
website_text = Label(text="website",fg="white", bg=Grey_black, font=(FONT_NAME, 10, "bold"))
website_text.grid(row=1, column=0)
email_text.grid(row=2, column=0)
password_text.grid(row=3, column=0)

# BUTTONS PART
generate_button = Button(text="Generate Password", font=(FONT_NAME, 8, "bold"), command=generate_password)
generate_button.grid(column=2, row=3)
add_button = Button(text="Add",width=33, height=1, font=(FONT_NAME, 8, "bold"), command=save_data)
add_button.grid(column=1, row=4, columnspan=2)

# ENTRY PART
website_input = Entry(width=39)
website_input.grid(column=1, row=1, columnspan=2)
user_email_input = Entry(width=39)
user_email_input.insert(0,"vijay@gmail.com")
user_email_input.grid(column=1, row=2, columnspan=2)
password_input = Entry(width=21)
password_input.grid(column=1, row=3)

page.mainloop()