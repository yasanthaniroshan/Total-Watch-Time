import os
from moviepy.editor import VideoFileClip

def get_video_duration(file_path):
    try:
        video = VideoFileClip(file_path)
        return video.duration
    except Exception as e:
        return 0

def calculate_total_watch_time(folder_path):
    total_watch_time = 0
    for root, _, files in os.walk(folder_path):
        for file in files:
            print(f"Processing file:  {file.lower()}")
            file_path = os.path.join(root, file)
            if file_path.lower().endswith(('.mp4', '.avi', '.mkv', '.mov', '.wmv', '.flv')):
                duration = get_video_duration(file_path)
                total_watch_time += duration

    return total_watch_time


main_folder = input("Enter the path of the main folder: ")
total_watch_time = calculate_total_watch_time(main_folder)

print(f"Total watch time in the main folder: {total_watch_time / 60} minutes")
