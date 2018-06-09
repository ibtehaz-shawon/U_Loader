import os

from pytube import YouTube
from shutil import copyfile
from pathlib import Path


class Stream_Test:

    @staticmethod
    def start(_url):
        yt = YouTube(str(_url))
        # total_list = yt.streams.filter(only_audio=True).all()
        total_list = yt.streams.all()
        print(yt.thumbnail_url)

        for item in total_list:
            print(item)
            print("mime {} and res {}".format(item.mime_type, item.resolution))
            # item.download()
            # copyfile(item.default_filename, os.path.join(str(Path.home()) + '/Music/') + item.default_filename)
            break


if __name__ == '__main__':
    Stream_Test().start('https://www.youtube.com/watch?v=uVibq-Uvmvc')
