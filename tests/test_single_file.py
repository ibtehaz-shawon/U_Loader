import unittest

from single_file import Main


class TestMain(unittest.TestCase):
    test_url_one = 'https://www.youtube.com/watch?v=uVibq-Uvmvc'
    test_url_two = 'https://www.youtube.com/watch?v=q-raLKa0uxo'
    test_url_three = 'https://www.youtube.com/watch?v=nVhNCTH8pDs'

    def test_audio(self):
        self.assertEqual(Main(_filename='test_audio', _is_audio=True).start_download(self.test_url_one), True)

    def test_video_720(self):
        self.assertEqual(Main(_filename='test_720', _is_audio=True).start_download(self.test_url_two), True)

    def test_video_480(self):
        self.assertEqual(
            Main(_filename='test_480', _is_audio=True).start_download(self.test_url_three, res='480p'), True)


if __name__ == '__main__':
    unittest.main()
