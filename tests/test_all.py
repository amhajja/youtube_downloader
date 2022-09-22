import unittest
import os
from yt_common.download_handler import (download_video)


class DownloadHandler_tests(unittest.TestCase):
    def test_download_video(self):
        result = download_video("https://www.youtube.com/watch?v=zvv8iFupg9M")
        self.assertTrue(result)

        output_folder = "downloaded_videos"
        file_name = "Malcolm Gladwell Explains Where His Ideas Come From  The New Yorker.mp4"
        result = os.path.exists(os.path.join(output_folder, file_name))
        self.assertTrue(result)
        os.remove(os.path.join(output_folder, file_name))