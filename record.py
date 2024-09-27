import mouse
import keyboard
import time
import pickle
import os

def record_actions():
    print("Recording started. Press the 'Stop Recording' button to stop.")
    
    actions = []
    start_time = time.time()  # Record the start time
    stop_flag = 'stop_flag.txt'

    # Function to record mouse events
    def on_mouse_event(event):
        if isinstance(event, mouse.MoveEvent):
            x, y = mouse.get_position()
            actions.append(('move', (x, y), time.time() - start_time))
        elif isinstance(event, mouse.ButtonEvent):
            actions.append((event.event_type, event.button, time.time() - start_time, mouse.get_position()))
    
    # Function to record keyboard events
    def on_keyboard_event(event):
        actions.append(('keyboard', event.name, event.event_type, time.time() - start_time))

    # Start recording mouse and keyboard events
    mouse.hook(on_mouse_event)
    keyboard.hook(on_keyboard_event)

    # Continuously record until the stop flag is found
    while not os.path.exists(stop_flag):
        time.sleep(0.1)  # Avoid consuming too much CPU

    # Stop the recording
    mouse.unhook(on_mouse_event)
    keyboard.unhook(on_keyboard_event)

    # Remove the stop flag file
    os.remove(stop_flag)

    # Save actions to file
    with open('actions.pkl', 'wb') as f:
        pickle.dump(actions, f)

    print("Recording stopped and saved.")

if __name__ == "__main__":
    record_actions()
