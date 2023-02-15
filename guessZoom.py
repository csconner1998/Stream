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
image = None
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
image_label = tk.Label(master=window,height=700,width=1200)
image_label.pack()

# Create a label to display the points
points_label = tk.Label(master=window, text="")
points_label.pack()

filenames = os.listdir("./zoomImages")
filename = ""
correctGuess = 0
alreadyGuessed = []

# Set the initial zoom level
zoom_level = 7
 
# Zoom out when the user presses the enter key
def zoom_out(event):
    global zoom_level
    zoom_level = max(1, zoom_level - 1)
    update_image()

def full_zoom_out(event):
    global zoom_level
    zoom_level = 1
    update_image()

window.bind("<space>", zoom_out)
window.bind("<Shift_L>", full_zoom_out)

# Update the image with the current zoom level
def update_image():
    global image
    # Create a copy of the image
    zoomed_image = image.copy()

    # Zoom out by reducing the size of the image
    width, height = image.width() * zoom_level, image.height() * zoom_level
    zoomed_image = zoomed_image.zoom(zoom_level, zoom_level)

    # Display the zoomed-out image in the label
    image_label.configure(image=zoomed_image)
    image_label.image = zoomed_image
# Display a random image from the directory when the window is first opened
def display_random_image():
    global filenames,filename,correctGuess, alreadyGuessed, image, zoom_level
    # Get a list of all the image filenames in the directory

    # Choose a random image from the list
    dir = "./zoomImages/"
    if len(filenames) > 0:
        filename = random.choice(filenames)
        filenames.remove(filename)
        correctGuess = 0
        alreadyGuessed = []
        zoom_level = 7 
    else:
        dir = ""
        zoom_level = 1
        filename = "TheEnd.png"

    # Load the image and display it in the label
    image = tk.PhotoImage(file=dir + filename)
    image_label.configure(image=image)
    image_label.image = image
    update_image()
    print(filename)

display_random_image()
update_image()

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
                correctAnswer = filename.split("_")[0]
                print(author + " Said " + clensedChatMsg)
                print(correctAnswer)
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