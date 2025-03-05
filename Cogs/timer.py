import time
import keyboard

def pomodoro_timer(minutes=25):
    print(f"Starting Pomodoro timer for {minutes} minutes...")
    seconds = minutes * 60
    while seconds > 0:
        mins, secs = divmod(seconds, 60)
        print(f"{mins:02d}:{secs:02d}", end="\r")
        if keyboard.is_pressed('s') and keyboard.is_pressed('t'):
            print("\nSkipping to break time!")
            break
        time.sleep(1)
        seconds -= 1
    else:
        print("\nBreak Time!")

def main():
    while True:
        pomodoro_timer()
        response = input("Press 's' to start again, 'q' to quit: ")
        if response.lower() == 'q':
            break

if __name__ == "__main__":
    main()