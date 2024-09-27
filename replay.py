import mouse
import keyboard
import time
import pickle

def replay_actions():
    # Load recorded actions from the file
    with open('actions.pkl', 'rb') as f:
        actions = pickle.load(f)
    
    start_time = time.time()  # Get the current time for reference

    for action in actions:
        try:
            # Determine the timestamp based on the action type
            if action[0] == 'move':
                timestamp = float(action[-1])  # Last element is the timestamp
            elif action[0] in ['down', 'up']:
                timestamp = float(action[2])  # Third element is the timestamp for mouse actions
            elif action[0] == 'keyboard':
                timestamp = float(action[-1])  # Last element is the timestamp for keyboard actions
            
            delay = timestamp - (time.time() - start_time)
            if delay > 0:
                time.sleep(delay)  # Sleep until it's time for the next event

            # Replay the action based on its type
            if action[0] == 'move':  # Mouse move event
                mouse.move(action[1][0], action[1][1], absolute=True)
            
            elif action[0] in ['down', 'up']:  # Mouse click event
                mouse.click(button=action[1])

            elif action[0] == 'keyboard':  # Keyboard event
                if action[2] == 'down':
                    keyboard.press(action[1])  # Simulate key press
                elif action[2] == 'up':
                    keyboard.release(action[1])  # Simulate key release

        except ValueError as e:
            print(f"Error processing action: {action} - {e}")
        except TypeError as e:
            print(f"Type error processing action: {action} - {e}")

if __name__ == "__main__":
    replay_actions()
