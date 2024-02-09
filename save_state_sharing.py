#!/usr/bin/python3

# import necessary modules

# for implementing the HTTP Web servers
import http.server

# provides access to the BSD socket interface
import socket

# a framework for network servers
import socketserver

# to display a Web-based documents to users
import webbrowser


# to access operating system control
import os


# assigning the appropriate port value
PORT = 8010
# this finds the name of the computer user


# changing the directory to access the files desktop
# with the help of os module

folder_path = "/home/jshutler/.local/share/dolphin-emu/GC/USA/Card A"
desktop = os.path.join(folder_path)
os.chdir(desktop)


# creating a http request
Handler = http.server.SimpleHTTPRequestHandler
# returns, host name of the system under
# which Python interpreter is executed
hostname = socket.gethostname()


# finding the IP address of the PC
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
IP = "http://" + s.getsockname()[0] + ":" + str(PORT)
link = IP


# converting the IP address into the form of a QRcode
# with the help of pyqrcode module


# Creating the HTTP request and  serving the
# folder in the PORT 8010,and the pyqrcode is generated

# continuous stream of data between client and server
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    print("Type this in your Browser", IP)
    print("or Use the QRCode")
    httpd.serve_forever()
