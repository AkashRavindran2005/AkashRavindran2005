#pip install secure-smtplib
import tkinter
import smtplib
from email.message import EmailMessage

def sending_email():
    root=tkinter.Tk()
    root.geometry('225x100')
    root.title('E-Mail')
    sub_label = tkinter.Label(root, text='Subject', font=('calibre', 10, 'bold'))
    sub = tkinter.Entry(root, font=('calibre', 10, 'normal'))
    body_label = tkinter.Label(root, text='Body', font=('calibre', 10, 'bold'))
    body = tkinter.Entry(root, font=('calibre', 10, 'normal'))
    to_label = tkinter.Label(root, text='To', font=('calibre', 10, 'bold'))
    to = tkinter.Entry(root, font=('calibre', 10, 'normal'))
    sub_label.grid(row=0, column=0)
    sub.grid(row=0, column=1)
    body_label.grid(row=1, column=0)
    body.grid(row=1, column=1)
    to_label.grid(row=2,column=0)
    to.grid(row=2,column=1)
    def notification():
        message=EmailMessage()
        message.set_content(body.get())
        message['subject']=sub.get()
        message['to']=to.get()
        user='ironmanak0205@gmail.com'
        message['from']=user
        password='fwwhmtyuompeihdn'
        server=smtplib.SMTP('smtp.gmail.com',587)
        server.starttls()
        server.login(user,password)
        server.send_message(message)
        server.quit()

    send=tkinter.Button(root,text='Send',command=notification)
    send.grid(row=3,column=1)
    quit=tkinter.Button(root,text='Quit',command=root.quit)
    quit.grid(row=3,column=0)
    root.mainloop()
sending_email()
