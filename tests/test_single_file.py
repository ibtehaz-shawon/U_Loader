import unittest

from single_file import Main


class TestMain(unittest.TestCase):
    test_url_one = 'https://www.youtube.com/watch?v=uVibq-Uvmvc'
    test_url_two = 'https://www.youtube.com/watch?v=q-raLKa0uxo'
    test_url_three = 'https://www.youtube.com/watch?v=nVhNCTH8pDs'

    def test_audio(self):
        self.assertEqual(Main(_filename='test_audio').start_download(self.test_url_one, is_audio=True), True)

    def test_video_720(self):
        self.assertEqual(Main(_filename='test_720').start_download(self.test_url_two, is_audio=False), True)

    def test_video_480(self):
        self.assertEqual(
            Main(_filename='test_480').start_download(self.test_url_three, is_audio=False, res='480p'), True)


if __name__ == '__main__':
    unittest.main()
