#Acknowledgement: A significant part of the code was taken from chatgpt 
import time
import subprocess
from colorama import init, Fore
from art import *

# Initialize colorama
init()

# Function to convert minutes and seconds to seconds
def convert_to_seconds(minutes, seconds):
    return minutes * 60 + seconds

# Function to format time as MM:SS
def format_time(total_seconds):
    minutes = total_seconds // 60
    seconds = total_seconds % 60
    return "{:02d}:{:02d}".format(minutes, seconds)

# Read the desired time in minutes and seconds
minutes = int(input("Enter the minutes: "))
seconds = int(input("Enter the seconds: "))

# Convert minutes and seconds to total seconds
total_seconds = convert_to_seconds(minutes, seconds)

# Countdown and ring the alarm
while total_seconds >= 0:  # Change the condition to include 00:00
    # Clear the terminal
    subprocess.run(["clear"])
    hash = Fore.RED + "\033[1m" + "####################################################################################################" + Fore.RESET  
    print(hash)

    # Generate ASCII art countdown
    countdown_text = format_time(total_seconds)
    countdown_ascii = text2art(countdown_text, font="block")

    countdown_colored = Fore.RED + "\033[1m" + countdown_ascii + Fore.RESET  # Add escape sequence for bold text

    # Display the countdown
    print(countdown_colored)
    print(hash)


    time.sleep(1)
    total_seconds -= 1
# Ring the alarm
print("\nALARM!")

# Play the VLC file
vlc_file = "path/to/your/vlc/file.mp3"  # Replace with the actual path to your VLC file
#subprocess.run(["vlc", vlc_file])