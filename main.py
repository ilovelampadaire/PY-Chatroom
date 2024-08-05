"""Main program of lamp's chatroom. Handles tkinter windows, chatroom connectivity, etc."""

import tkinter
from tkinter import scrolledtext, messagebox
import random
import string
import lib.handler

# import tkinter.messagebox

# -Code for handling the txt file error-
def handling_txt_not_found():
    """Shows an error saying the handling text file does not exist."""
    messagebox.showerror(
        "File Not Found",
        "handling.txt was not found and needs to be redownloaded or recovered."
    )

def main():
    """Main function. Calls the handler library to check if handling.txt exists."""
    lib.handler.check(exists, handling_txt_not_found)

if __name__ == "__main__":
    main()

def exists():
    """Starts the main window and chatroom when called."""
    start_program()

def start_program():
    """Starts the chatroom. Makes an username by itself and makes a new window."""
    def generate_username():
        return ''.join(random.choices(string.ascii_letters + string.digits, k=8))

    # -Function to send a message-
    def send_message():
        message = message_entry.get()
        if message.strip():
            chatroom.config(state=tkinter.NORMAL)
            chatroom.insert(tkinter.END, f"{username}: {message}\n")
            chatroom.config(state=tkinter.DISABLED)
            message_entry.delete(0, tkinter.END)

    # -Create the main window-
    root = tkinter.Tk()
    root.title("Chatroom")

    # -Generate a random username-
    username = generate_username()

    # -Create a scrolled text widget for the chatroom-
    chatroom = scrolledtext.ScrolledText(root,
        state=tkinter.DISABLED,
        wrap=tkinter.WORD,
        width=50,
        height=20)
    chatroom.pack(padx=10, pady=10)

    # -Create a frame for the message entry and send button-
    input_frame = tkinter.Frame(root)
    input_frame.pack(padx=10, pady=10, fill=tkinter.X)

    # -Create an entry widget for typing messages-
    message_entry = tkinter.Entry(input_frame, width=40)
    message_entry.pack(side=tkinter.LEFT, padx=(0, 10), fill=tkinter.X, expand=True)
    message_entry.bind("<Return>", send_message)

    # -Create a button to send messages-
    send_button = tkinter.Button(input_frame, text="Send", command=send_message)
    send_button.pack(side=tkinter.RIGHT)

    # -Start the tkinterinter event loop-
    root.mainloop()
