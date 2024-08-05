"""Main program of lamp's chatroom. Handles tkinter windows, chatroom connectivity, etc."""

import tkinter
from tkinter import scrolledtext, messagebox, simpledialog
import random
import string
import lib.handler

def string_dialog(prompt,default=None):
    """Uses tkinter's simpledialog submodule to ask for a string from the user."""
    return simpledialog.askstring(title="PY-ChatRoom",prompt=prompt,initialvalue=default)

def start_program():
    """Starts the chatroom. Makes an username by itself and makes a new window."""
    def generate_username():
        return ''.join(random.choices(string.ascii_letters + string.digits, k=8))

    def get_username():
        rand_username = generate_username()
        dialog = string_dialog("Enter your username...",rand_username)
        if dialog.replace(" ","")=="":
            return rand_username
        return dialog

    # -Function to send a message-
    def send_message():
        message = message_entry.get()
        if message.strip():
            chatroom.config(state=tkinter.NORMAL)
            chatroom.insert(tkinter.END, f"{username}: {message}\n")
            chatroom.config(state=tkinter.DISABLED)
            message_entry.delete(0, tkinter.END)

    # -Get an username-
    username = get_username()

    # -Create the main window-
    root = tkinter.Tk()
    root.title("Chatroom")

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

    def enter_key_event(data):
        if ["\r","\n","\r\n"] in data.char:
            send_message()

    # -Create an entry widget for typing messages-
    message_entry = tkinter.Entry(input_frame, width=40)
    message_entry.pack(side=tkinter.LEFT, padx=(0, 10), fill=tkinter.X, expand=True)
    message_entry.bind("<Return>", enter_key_event)

    # -Create a button to send messages-
    send_button = tkinter.Button(input_frame, text="Send", command=send_message)
    send_button.pack(side=tkinter.RIGHT)

    # -Start the tkinterinter event loop-
    root.mainloop()

def main():
    """Main function. Calls the handler library to check if handling.txt exists."""
    def handling_txt_not_found():
        messagebox.showerror(
            "File Not Found",
            "handling.txt was not found and needs to be redownloaded or recovered."
        )
    lib.handler.check(start_program, handling_txt_not_found)

if __name__ == "__main__":
    main()
