#Install pytube module using pip install pytube command
import pytube

# Replace VIDEO_URL with the URL of the YouTube video you want to play
VIDEO_URL = "https://www.youtube.com/watch?v=w_Pz-t41S5w&list=OLAK5uy_koDf8VIkAyw2iyMTdFzwy27CGqGYZtWto&index=2"

# Use pytube to download the video
video = pytube.YouTube(VIDEO_URL).streams.first().download()

# Play the video using the default media player
import os
os.startfile(video)
