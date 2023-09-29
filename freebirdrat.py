import tkinter as tk
from PIL import Image, ImageTk
import pygame
import imageio

# Initialize speed variables
gif_speed = 100  # milliseconds
music_speed = 1.0  # default speed

def disable_close():
    pass

def play_music():
    pygame.mixer.init()
    pygame.mixer.music.load("freebirdsolo.mp3")
    pygame.mixer.music.set_volume(music_speed)  # Set initial volume
    pygame.mixer.music.play(-1)  # -1 makes it loop indefinitely

def update_gif(counter):
    img = frames[counter % len(frames)]
    label.configure(image=img)
    label.image = img
    counter += 1
    root.after(gif_speed, update_gif, counter)

def increase_speed():
    global gif_speed, music_speed
    gif_speed = max(10, gif_speed - 10)  # Decrease gif speed by 10 milliseconds (minimum speed of 10 ms)
    music_speed = min(1.0, music_speed + 0.1)  # Increase music speed by 0.1 (maximum speed of 1.0)
    pygame.mixer.music.set_volume(music_speed)  # Apply updated volume
    print(f"Updated Speeds - Gif: {gif_speed} ms, Music: {music_speed}")

def decrease_speed():
    global gif_speed, music_speed
    gif_speed = min(500, gif_speed + 10)  # Increase gif speed by 10 milliseconds (maximum speed of 500 ms)
    music_speed = max(0.1, music_speed - 0.1)  # Decrease music speed by 0.1 (minimum speed of 0.1)
    pygame.mixer.music.set_volume(music_speed)  # Apply updated volume
    print(f"Updated Speeds - Gif: {gif_speed} ms, Music: {music_speed}")

root = tk.Tk()
root.title("FreeBirdRat")
root.resizable(False, False)

# Automatically open in fullscreen mode
root.attributes('-fullscreen', True)

# Load the GIF frames and resize
gif = imageio.mimread("rat-spinning.gif")
frames = [ImageTk.PhotoImage(Image.fromarray(frame).resize((1920, 1080))) for frame in gif]

# Display the GIF
label = tk.Label(root)
label.pack()

# Start GIF update loop
update_gif(0)

# Disable window closing
root.protocol("WM_DELETE_WINDOW", disable_close)

# Play the music
play_music()

# Bind left and right arrow keys to speed functions
root.bind("<Left>", lambda event: decrease_speed())
root.bind("<Right>", lambda event: increase_speed())

# Run the GUI event loop
root.mainloop()
