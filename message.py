import fbchat 
from getpass import getpass 

username = input('username: ')
client = fbchat.Client(username, getpass()) 

print("success")
target = input("user to message: ")
users = client.searchForUsers(target)

with open ("cars.txt", "r") as file:
    a = file.read()
    x = a.split()
    for i in x:
        
        message = fbchat.Message(text=i)
        client.send(message, thread_id=users[0].uid, thread_type=fbchat.ThreadType.USER)

        