import os
import subprocess

files=os.listdir("Dataset_Lectures")
for file in files: #each video file in the folder
   Chapter=(file.split(' -')[0])[-1] #Extracting the chapter number from the file name
   print(Chapter)
   file_name=(file.split(' -')[0].split(' Chapter ')[0]) #Extracting the file name without the chapter
   subprocess.run(["ffmpeg","-i",f"Dataset_Lectures/{file}",f"Dataset_Audios/{Chapter}_{file_name}.mp3"]) #Converting the video to audio and saving it in the Dataset_Audios folder with the name format "ChapterNumber_FileName.mp3"