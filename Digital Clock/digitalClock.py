from tkinter import *
import time

clk = Tk()
clk.title('Clock')
clk.geometry("1300x700+0+0")
clk.config(bg="#0C1E28")


def clock():
    hr = str(time.strftime("%H"))
    mn = str(time.strftime("%M"))
    sc = str(time.strftime("%S"))
    print(hr, mn, sc)
    if int(hr) > 12 and int(mn) > 0:
        lb_dn.config(text="PM")
    if int(hr) > 12:
        hr = str(int(int(hr) - 12))

    lb_hr.config(text=hr)
    lb_mn.config(text=mn)
    lb_sc.config(text=sc)

    lb_hr.after(200, clock)


lb_hr = Label(clk, text="12", font=("Times 20 bold", 75, 'bold'), bg="#087587", fg="white")
lb_hr.place(x=350, y=200, width=150, height=150)

lb_hr_txt = Label(clk, text="HOUR", font=("Times 20 bold", 20, 'bold'), bg="#087587", fg="white")
lb_hr_txt.place(x=350, y=360, width=150, height=50)

lb_mn = Label(clk, text="12", font=("Times 20 bold", 75, 'bold'), bg="#008EA4")
lb_mn.place(x=520, y=200, width=150, height=150)

lb_mn_txt = Label(clk, text="MINUTE", font=("Times 20 bold", 20, 'bold'), bg="#008EA4", fg="white")
lb_mn_txt.place(x=520, y=360, width=150, height=50)

lb_sc = Label(clk, text="12", font=("Times 20 bold", 75, 'bold'), bg="#0684BB")
lb_sc.place(x=690, y=200, width=150, height=150)

lb_sc_txt = Label(clk, text="SECOND", font=("Times 20 bold", 20, 'bold'), bg="#0684BB", fg="white")
lb_sc_txt.place(x=690, y=360, width=150, height=50)

lb_dn = Label(clk, text="AM", font=("Times 20 bold", 70, 'bold'), bg="#9F0646")
lb_dn.place(x=860, y=200, width=150, height=150)

lb_dn_txt = Label(clk, text="NOON", font=("Times 20 bold", 20, 'bold'), bg="#9F0646", fg="white")
lb_dn_txt.place(x=860, y=360, width=150, height=50)


clock()
clk.mainloop()
