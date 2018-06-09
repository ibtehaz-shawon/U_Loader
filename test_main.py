import datetime
import unittest

from main import Main


class TestMain(unittest.TestCase):
    test_url_one = 'https://www.youtube.com/watch?v=uVibq-Uvmvc'
    test_url_two = 'https://www.youtube.com/watch?v=q-raLKa0uxo'

    def test_audio(self):
        self.assertEqual(Main(_filename='mp3_' +
                           str(datetime.datetime.now())).start_download(self.test_url_one, is_audio=True), True)

    def test_video(self):
        self.assertEqual(Main(_filename='mp4_1_' +
                           str(datetime.datetime.now())).start_download(self.test_url_two, is_audio=False), True)
        self.assertEqual(
            Main(_filename='mp4_2_' +
                           str(datetime.datetime.now()))
                .start_download(self.test_url_two, is_audio=False, res='480p'), True)


if __name__ == '__main__':
    unittest.main()
