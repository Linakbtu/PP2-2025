import pygame
import os

pygame.mixer.init()

downloads_folder = os.path.join(os.path.expanduser("~"), "Downloads")
music_file = os.path.join(downloads_folder, "sounds.mp3")

pygame.mixer.music.load(music_file)

def play_music():
    pygame.mixer.music.play()
    print("▶Play music")

def stop_music():
    pygame.mixer.music.stop()
    print("⏹ Stop music")

def next_music():
    pygame.mixer.music.rewind()
    print("⏭ next")

def prev_music():
    pygame.mixer.music.rewind()
    print("⏮ prev")

print("Press 'P' to play, 'S' to stop, 'N' to fast forward, 'B' to rewind")
while True:
    event = input("Enter command (P/S/N/B): ").strip().upper()
    if event == "P":
        play_music()
    elif event == "S":
        stop_music()
    elif event == "N":
        next_music()
    elif event == "B":
        prev_music()
    elif event == "Q":
        print("Выход...")
        break