pyclient.py
#import socket and tkinter library
import socket
import tkinter
#exit function
def exitfn():
csock.close()
exit(1)
#msg sending function
def msgsendfn():
#get message from textfield or entry
msg = msgentry.get()
# converting msg string to bytes using encode utf-8
msg = msg.encode('utf-8')
csock.sendall(encryptedmsg)
print('\n',cname,'->',msg)
#msg receiving function
def msgreceivefn():
#receive the encrypted msg
msg = csock.recv(3000)
#print msg by decoding it
print('\n', sname, '->', msg.decode('utf-8'))
#sock_family = IPv4 & sock_type = TCP are two params
csock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#connecting to server ip and port 5000
print('connecting to server...')
csock.connect(('127.0.0.1',5000))
#input client name
cname = input('enter your name : ')
#send client name to server
csock.sendall(cname.encode('utf-8'))
#receive server name
sname = csock.recv(1024).decode('utf-8')
print('you are now connected to',sname,'...')
#create the message-sending box
print('creating message chat-box...')
root = tkinter.Tk()
wtitle = cname + ' window'
root.title(wtitle)
root.geometry('300x300')
msgentry = tkinter.Entry(root)
radiochoice = tkinter.IntVar()
sendbtn = tkinter.Button(root,text='Send Message',command=msgsendfn)
refreshbtn = tkinter.Button(root,text='Refresh',command=msgreceivefn)
exitbtn = tkinter.Button(root,text='Exit',command=exitfn)
msgentry.pack()
sendbtn.pack()
refreshbtn.pack()
exitbtn.pack()
root.mainloop()