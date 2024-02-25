from pytube import YouTube
import tkinter as tk
import os

app = tk.Tk()

user_input = tk.StringVar(app)
url = ""

def parse_link():
    global url, l_prompt, l_entry, l_confirm, o_prompt, o_mp3, o_mp4, user_input
    
    l_prompt.destroy()
    l_entry.destroy()
    l_confirm.destroy()

    o_prompt.pack()
    o_mp3.pack()
    o_mp4.pack()

    url = user_input.get()

def mp3(link):
    video = YouTube(link)
    video = video.streams.filter(only_audio=True).first()
    video.download(output_path=os.path.expanduser('~\Music\'))

def mp4(link):
    video = YouTube(link)
    video = video.streams.get_highest_resolution()
    video.download(output_path=os.path.expanduser('~\Videos\'))

#Create Widgets
l_prompt = tk.Label(app, text='Geben sie den link ein')
l_entry = tk.Entry(app, textvariable=user_input)
l_confirm = tk.Button(app, text='Weiter', command=lambda: parse_link())

o_prompt = tk.Label(app, text='Wähle eine Option aus')
o_mp3 = tk.Button(app, text='.MP3', command=lambda: mp3(url))
o_mp4 = tk.Button(app, text='.MP4', command=lambda: mp4(url))

#Pack Widgets
l_prompt.pack()
l_entry.pack()
l_confirm.pack()

app.title('Youtube Downloader')
app.geometry('600x480')
app.mainloop()
