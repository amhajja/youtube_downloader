from pytube import YouTube


def download_video(link):
    try:
        yt = YouTube(link)
    except:
        print("Connection Error")
        return False

    try:
        print("Started downloading video")
        stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution')[-2]
        stream.download('downloaded_videos')
    except:
        print("Some Error!")
        return False

    print('Task Completed!')
    return True