import threading
import tkinter as tk
import random
import os
from dotenv import load_dotenv
import socket
import emoji

load_dotenv()

# Connect to a channel
server = os.getenv('server')
port = os.getenv('port')
nickname = os.getenv('nickname')
token = os.getenv('token')
channel = os.getenv('channel')

# Create a dictionary to track the points for each user
points = {}

# Set up a listener for new messages in the chat
def givePoints(user):
    global correctGuess
    if correctGuess == 0:
        # Give the user 5 points if they have already guessed the image
        if user not in points:
            points[user] = 10
        else:
            points[user] += 10
        correctGuess += 1
    elif correctGuess == 1:
        # Give the user 10 points if they are the first to guess the image
        if user not in points:
            points[user] = 5
        else:
            points[user] += 5
            correctGuess += 1

# Create the main window
window = tk.Tk()
window.title("Image Guessing Game")

# Create a label to display the image
image_label = tk.Label(master=window,height=512,width=512)
image_label.pack()

# Create a label to display the points
points_label = tk.Label(master=window, text="")
points_label.pack()

filenames = os.listdir("./icons")
filename = ""
correctGuess = 0
alreadyGuessed = []

# Display a random image from the directory when the window is first opened
def display_random_image():
    global filenames,filename,correctGuess, alreadyGuessed
    # Get a list of all the image filenames in the directory

    # Choose a random image from the list
    dir = "./icons/"
    if len(filenames) > 0:
        filename = random.choice(filenames)
        filenames.remove(filename)
        correctGuess = 0
        alreadyGuessed = []
    else:
        dir = ""
        filename = "TheEnd.png"

    # Load the image and display it in the label
    image = tk.PhotoImage(file=dir + filename)
    image_label.configure(image=image)
    image_label.image = image
    print(filename)

display_random_image()

# Change the image when the user presses the space bar
def change_image(event):
    display_random_image()

def popText(author):
    pop_label = tk.Label(master=window,text=author + " got it")
    pop_label.pack()
    window.update()
    window.after(3000, pop_label.destroy)

# Update the points display
def update_points():
    # Get the points for the top 3 users as a list of tuples (username, points)
    leaderboard = [(username, points[username]) for username in points]
    # Sort the leaderboard by points
    leaderboard.sort(key=lambda x: x[1], reverse=True)
    # Get the top 3 scores
    leaderboard = leaderboard[:3]

    # Format the points as a string
    text = "\n".join(f"{username}: {points}" for username, points in leaderboard)

    # Update the label with the new points
    points_label.configure(text=text)

def stopThread():
    global stopped
    stopped = True
    window.destroy()
def thread_function():
    global filename, alreadyGuessed, stopped
    sock = socket.socket()
    sock.connect((server, int(port)))
    sock.send(f"PASS {token}\n".encode('utf-8'))
    sock.send(f"NICK {nickname}\n".encode('utf-8'))
    sock.send(f"JOIN {channel}\n".encode('utf-8'))
    while True and not stopped:
        resp = sock.recv(2048).decode('utf-8')

        if resp.startswith('PING'):
            sock.send("PONG\n".encode('utf-8'))
        
        elif len(resp) > 0:
            chatMsg = resp.split("l :")
            if len(chatMsg) > 1:
                clensedChatMsg = emoji.demojize(chatMsg[1].rstrip("\n\r"))
                author = resp.split("!")[0][1:]
                correctAnswer = filename[:-6] + " " + filename[-5]
                print(correctAnswer)
                print(author + " Said " + clensedChatMsg)
                if str.lower(correctAnswer) == str.lower(clensedChatMsg) and author not in alreadyGuessed:
                    givePoints(author)
                    popText(author)
                    update_points()
                    alreadyGuessed.append(author)


window.bind("<Return>", change_image)
thread = threading.Thread(target=thread_function)
thread.start()
stopped = False
# Start the tkinter event loop
window.protocol("WM_DELETE_WINDOW",stopThread)
window.mainloop()