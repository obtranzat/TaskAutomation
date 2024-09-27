import tkinter as tk
from tkinter import messagebox
import subprocess
import os

process = None

# Function to launch the record executable
def record():
    global process
    exe_path = os.path.join(os.getcwd(), 'record.exe')
    stop_flag = 'stop_flag.txt'

    # Ensure any previous stop flag is removed
    if os.path.exists(stop_flag):
        os.remove(stop_flag)

    if os.path.exists(exe_path):
        process = subprocess.Popen(exe_path)
        messagebox.showinfo("Recording", "Recording has started. Press 'Stop Recording' to stop.")
    else:
        messagebox.showerror("Error", f"File not found: {exe_path}")

# Function to stop the recording by creating the stop flag
def stop_recording():
    stop_flag = 'stop_flag.txt'

    if process is not None:
        # Create the stop flag file to stop the recording process
        with open(stop_flag, 'w') as f:
            f.write('stop')

        messagebox.showinfo("Recording", "Recording will stop shortly.")
    else:
        messagebox.showerror("Error", "No recording in progress.")

# Function to launch the replay executable
def replay():
    exe_path = os.path.join(os.getcwd(), 'replay.exe')

    if os.path.exists(exe_path):
        subprocess.Popen(exe_path)
        #messagebox.showinfo("Replay", "Replaying recorded actions.")
    else:
        messagebox.showerror("Error", f"File not found: {exe_path}")

# Create the main window
root = tk.Tk()
root.title("Tehtävien automatisointi")
root.geometry("300x250")

# Create buttons
replay_button = tk.Button(root, text="Avoin tehtävä", command=replay, width=20, height=2, fg="blue", bg="white")
stop_button = tk.Button(root, text="", command=stop_recording, width=20, height=2, fg="red", bg="white")
record_button = tk.Button(root, text="", command=record, width=20, height=2, fg="green", bg="white")




# Pack the buttons into the window
replay_button.pack(pady=10)
stop_button.pack(pady=10)
record_button.pack(pady=10)


# Add a footer with the company name
footer_label = tk.Label(root, text="© https://obtranzat.42web.io", bd=1, relief=tk.SUNKEN, anchor=tk.W, font=('Helvetica', 10, 'italic'), fg="black")

footer_label.pack(side="bottom", fill="x")

# Start the Tkinter event loop
root.mainloop()
