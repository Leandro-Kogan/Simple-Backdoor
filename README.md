# Simple-Backdoor
A simple python 2 server-client command control backdoor

A couple of things to take into consideration:
-When you use the UPLOAD option to pass a file from the server to the remote host the file must be in the same folder as the script we are runnin, AKA the server itself.**
-The server is meant to be runned in Linux systems, you can modify it to use it on Windows.
-The client.py should be compiled to run on windows if there is no python 2 interpreter installed (depends in how you are going to use it). Taking in consideration that this is a "reverse shell", and you will probably want to embed it with another file... For the compiling you can use pyinstaller.
-Do not forget to change the IP and the PORT in both client and server.
-It has a timer that until we get a connection it will try to get to us every 30 seconds. Be patient...
-Feel free to modify it as you wish to meet your needs :)
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------DISCLAIMER:
This scripts are meant to be used for improving network security, security auditories, AV efficiency testing, CTF's and other legal actions that include the permission of those you are using it against. 
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
A few commands:
-upload , to upload a file to the remote host **
-download , to download a file from the remote host
- -q , to quit (once you quit you will not be able to connect back)

