import speech_recognition as sr
import moviepy.editor as mp
# import sys
import os


# filename='WhatsApp Audio 2021-01-17 at 22.13.42 (1).wav'
r=sr.Recognizer()




def convert(file_name):
    r=sr.Recognizer()

    
    
    clip=mp.VideoFileClip(file_name)
    conv_file="audio"
    clip.audio.write_audiofile("audio.wav")
    with sr.AudioFile("audio.wav") as file:
        audio_data=r.record(file)
        
        text=r.recognize_google(audio_data)
        return text
    

