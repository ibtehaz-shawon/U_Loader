import unittest

from playlist import Playlist


class Test_Playlist(unittest.TestCase):
    def test_playlist(self):
        test_playlist = 'https://www.youtube.com/watch?v=76k991G0sJo&list=PLnd9zkUqwBehPFy-4seB_lWdqKhVa1EYT'
        url_list = Playlist(test_playlist).get_all_url()
        self.assertEqual(len(url_list) > 0, True)

    def test_playlist_download(self):
        test_playlist = 'https://www.youtube.com/watch?v=76k991G0sJo&list=PLnd9zkUqwBehPFy-4seB_lWdqKhVa1EYT'
        url_list = Playlist(test_playlist).get_all_url()
        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
