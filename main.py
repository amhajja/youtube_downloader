# importing the module
from pytube import YouTube


def download_video(link):
    try:
        yt = YouTube(link)
    except:
        print("Connection Error")  # to handle exception

    try:
        stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution')[-2]
        stream.download('downloaded_videos')
    except:
        print("Some Error!")
    print('Task Completed!')
