import random
from tkinter import *

root = Tk()
root.geometry("400x450")
root.title("Welcome To Your Password Generator")

#
# print('Welcome To Your Password Generator')
#
# chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*().,?0123456789'
#
# number = input('Amount of passwords to generate: ')
# number = int(number)
#
# length = input('Input your password length: ')
# length = int(length)
#
# print('\nHere are your passwords: ')
# for pwd in range(number):
#     passwords = ''
#     for c in range(length):
#         passwords += random.choice(chars)
#     print(passwords)

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*().,?0123456789'


def amount_info():
    number = input_amount.get("1.0", "end-1c")
    return number


def length_info():
    length = input_length.get("1.0", "end-1c")
    return length


def generate_pass():
    number = amount_info()
    length = length_info()

    p = '\n'
    temp = "Please write a valid digit!\n"

    if number == "" or length == "":
        Output.insert(END, temp)
    else:
        number = int(number)
        length = int(length)

        if ((isinstance(number, int) != True) or (isinstance(length, int) != True)):
            Output.insert(END, temp)

        else:

            for pwd in range(number):
                passwords = ''
                for c in range(length):
                    passwords += random.choice(chars)

                Output.insert(END, passwords + p)


l1 = Label(text="Amount of passwords to generate:")
input_amount = Text(root, height=2,
                    width=25,
                    bg="light yellow")

l1.pack()
input_amount.pack()

l2 = Label(text="Input your password length: ")
input_length = Text(root, height=2,
                    width=25,
                    bg="light blue")

l2.pack()
input_length.pack()

Output = Text(root, height=15,
              width=30,
              bg="light cyan")

Display = Button(root, height=2,
                 width=20,
                 text="Generate",
                 command=lambda: generate_pass())

Display.pack()
Output.pack()

mainloop()
