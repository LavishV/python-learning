from itertools import cycle
from PIL import Image, ImageTk
import time
import tkinter as tk

root=tk.Tk()
root.title("Image slideshow Viewer")

#List of image path
image_paths = [
    r"C:\Lavi01\Wallpaper\73eb04196a11ef1173bd0782104588e5.jpg",
    r"C:\Lavi01\Wallpaper\7022fde301338644bca180ebce7d51a7.jpg",
    r"C:\Lavi01\Wallpaper\backiee-286745-landscape.jpg",
    r"C:\Lavi01\Wallpaper\backiee-295499-landscape.jpg"
]

#Resize images
image_size=(1920,1080)
image=[Image.open(path). resize(image_size) for path in image_paths]
photo_images=[ImageTk.PhotoImage(image) for image in image]

label = tk.Label(root)
label.pack()

def update_image():
    for photo_image in photo_images:
        label.config(image=photo_image)
        label.update()
        time.sleep(0.5)

#Slideshow  : we will use itertool cycle function        
slideshow = cycle(photo_images)

def start_slideshow():
    for _ in range(len(image_paths)):
        update_image()

play_button = tk.Button(root, text = 'PLay Slideshow', command=start_slideshow)        
play_button.pack()

root.mainloop()