#import socket and tkinter library
import socket
import tkinter
#exit function
def exitfn():
#close all open socket connections
csock.close()
ssock.close()
#exit the program
exit(1)
#msg sending function
def msgsendfn():
#get message from textfield or entry
msg = msgentry.get()
# converting msg string to bytes using encode utf-8
msg = msg.encode('utf-8')
#send the msg & print the msg
csock.sendall(encryptedmsg)
print('\n', sname, '->', msg)
#msg receiving function
def msgreceivefn():
#receive the encrypted msg
msg = csock.recv(2048)
#print the msg by decoding it and keys
print('\n', cname, '->', msg.decode('utf-8'))
#sock_family = IPv4 & sock_type = TCP are two params
ssock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#host = '' to enable outside connections & port no = 1234
ssock.bind(('',5000))
#sock is in listening mode
ssock.listen()
print('listening for client connection...')
#forever loop for client connection
while True:
#connect to client & store its address
csock, caddr = ssock.accept()
#receive client name
cname = csock.recv(1024).decode('utf-8')
#input server name
sname = input('enter your name : ')
#send server name to client
csock.sendall(sname.encode('utf-8'))
print('you are now connected to',cname,'...')
#create the message-sending box
print('creating message chat-box...')
root = tkinter.Tk()
wtitle = sname + ' window'
root.title(wtitle)
root.geometry('300x300')
msgentry = tkinter.Entry(root)
sendbtn = tkinter.Button(root, text='Send Message',command=msgsendfn)
refreshbtn = tkinter.Button(root,text='Refresh',command=msgreceivefn)
exitbtn = tkinter.Button(root,text='Exit',command=exitfn)
msgentry.pack()
sendbtn.pack()
refreshbtn.pack()
exitbtn.pack()
root.mainloop()