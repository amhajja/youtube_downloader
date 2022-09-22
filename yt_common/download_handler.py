from pytube import YouTube
from pytube.cli import on_progress


def download_video(link: str, output_dir: str = 'downloaded_videos'):
    try:
        yt = YouTube(link, on_progress_callback=on_progress)
    except:
        print("Connection Error")
        return False

    try:
        print("Started downloading video")
        stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution')[-1]
        stream.download(output_dir)
    except:
        print("Some Error!")
        return False

    print('Task Completed!')
    return True
