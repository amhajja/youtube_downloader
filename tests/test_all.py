import unittest
import os
from yt_common.download_handler import (download_video)


class DownloadHandler_tests(unittest.TestCase):
    def test_download_video(self):
        result = download_video("https://www.youtube.com/watch?v=zvv8iFupg9M")
        self.assertTrue(result)

        result = os.path.exists(os.path.join("downloaded_videos",
                                             "Malcolm Gladwell Explains Where His Ideas Come From  The New Yorker.mp4"))
        self.assertTrue(result)