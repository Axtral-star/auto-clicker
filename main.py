import customtkinter as ctk
from pynput.mouse import Button, Controller
import time
import threading

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.geometry("425x300")
app.title("Autoclicker")
app.resizable(False, False)

mouse = Controller()
running = False
total_seconds = 0

# autoclicker function
def start_autoclicker():
    global running
    global total_seconds
    running = True
    status_label.configure(text="Status: Running")
    print("Auto-clicker started. Press F6 to stop.")

    while running:
        mouse.click(Button.left, 1)

        # break sleep into small parts
        elapsed = 0
        while elapsed < total_seconds and running:
            time.sleep(0.01)
            elapsed += 0.01

    status_label.configure(text="Status: Stopped")
    print("Autoclicker stopped.")

# stop function
def stop_autoclicker(event=None):
    global running
    running = False
    print("stop pressed")

# save inputs and start
def save_inputs():
    global total_seconds
    ms_input = left_box.get("1.0", "end-1c").strip()
    s_input = middle_box.get("1.0", "end-1c").strip()
    m_input = right_box.get("1.0", "end-1c").strip()

    ms = float(ms_input) if ms_input else 0
    s = float(s_input) if s_input else 0
    m = float(m_input) if m_input else 0

    total_seconds = ms / 1000 + s + m * 60
    print("Total seconds:", total_seconds)

    threading.Thread(target=start_autoclicker, daemon=True).start()

# labels
left_label = ctk.CTkLabel(app, text="Milliseconds")
middle_label = ctk.CTkLabel(app, text="Seconds")
right_label = ctk.CTkLabel(app, text="Minutes")

left_label.grid(row=0, column=0, padx=20, pady=(20, 5))
middle_label.grid(row=0, column=1, padx=20, pady=(20, 5))
right_label.grid(row=0, column=2, padx=20, pady=(20, 5))

# textboxes
left_box = ctk.CTkTextbox(app, width=100, height=30)
middle_box = ctk.CTkTextbox(app, width=100, height=30)
right_box = ctk.CTkTextbox(app, width=100, height=30)

left_box.grid(row=1, column=0, padx=20, sticky="w")
middle_box.grid(row=1, column=1, padx=20)
right_box.grid(row=1, column=2, padx=20, sticky="e")

# start
save_button = ctk.CTkButton(app, text="Start Auto Clicker", command=save_inputs)
save_button.grid(row=2, column=1, pady=10)

# status label
status_label = ctk.CTkLabel(app, text="Status: Stopped")
status_label.grid(row=3, column=1, pady=10)

# F6 to stop auto-clicker
app.bind("<F6>", stop_autoclicker)

app.mainloop()
