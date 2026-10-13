import time
import sys
from color_utils import get_color_code

def countdown(seconds):
    """
    Countdown function that displays the remaining time in the terminal with color changes.

    Args:
        seconds (int): The total number of seconds for the countdown.
    """
    while seconds >= 0:
        # Calculate minutes and seconds
        mins, secs = divmod(seconds, 60)
        time_format = f"{mins:02d}:{secs:02d}"

        # Determine the color based on the remaining time
        if seconds > 30:
            color_code = get_color_code('green')
        elif seconds > 10:
            color_code = get_color_code('yellow')
        else:
            color_code = get_color_code('red')

        # Print the remaining time with the appropriate color
        sys.stdout.write(f"\r{color_code}{time_format}{get_color_code('reset')}")
        sys.stdout.flush()

        # Wait for one second
        time.sleep(1)

        # Decrement the remaining time
        seconds -= 1

    # Print a newline after the countdown is complete
    print("\nCountdown complete!")

def main():
    """
    Main function to handle user input and start the countdown.
    """
    try:
        # Get the countdown duration from the user
        seconds = int(input("Enter the countdown duration in seconds: "))
        if seconds <= 0:
            print("Please enter a positive integer.")
            return

        # Start the countdown
        countdown(seconds)
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    main()