import datetime
import os
import sys
import os.path
from pathlib import Path
from shutil import copyfile

from pytube import YouTube
from util import safe_filename


class Main:

    def __init__(self, _filename=None, _thumbnail_url=None, _is_audio=False):
        self._filename = _filename
        self.thumbnail_url = _thumbnail_url
        self.is_audio = _is_audio

    @staticmethod
    def on_complete(stream, file_handle):
        file_name = os.path.basename(file_handle.name)
        print("Download complete {}".format(file_name))
        return

    @staticmethod
    def on_progress(stream, chunk, file_handle, bytes_remaining):
        bytes_remaining = bytes_remaining / (1000 * 1000)
        file_name = os.path.basename(file_handle.name)
        print('Downloading {}, remaining {} mb'.format(file_name, bytes_remaining))
        return

    def clean_up(self, default_directory):
        """
        cleans up the directory and removes file, copy to directory specified
        :param default_directory: UNIX directory currently
        :return: None
        """
        if self.is_audio:
            os.rename(self._filename + '.mp4', self._filename + '.mp3')
            # TODO : add thumbnail in mp3 here
            # if self.thumbnail_url is not None:
            #     tag = eyeD3.Tag()
            #     tag.addImage(0x08, artwork_file_name)
            #     tag.setArtist(artist)
            #     tag.setDate(localtime().tm_year)
            #     tag.setTitle(item_title)
            #     tag.setGenre("Trance")
            #     tag.update()
            copyfile(self._filename + '.mp3', default_directory + self._filename + '.mp3')
            os.remove(self._filename + '.mp3')
        else:
            if self._filename is not None:
                copyfile(self._filename + '.mp4', default_directory + self._filename + '.mp4')
                os.remove(self._filename + '.mp4')
        return

    """
    --------------------------------------------------
    --------------------------------------------------
    --------------------------------------------------
    """

    def start_download(self, _url, res='720p',
                       default_directory=os.path.join(str(Path.home()) + '/Music/')):
        """
        Main downloader to download files in the current directory.
        TODO: I can get the download url from the pytube and download it via
        TODO: urllib2 or something else. May be later.
        :param _url: str
        :param res: str
        :param default_directory: UNIX directory currently
        :return: bool | success or not
        """
        try:
            yt = YouTube(str(_url))
            yt.register_on_progress_callback(self.on_progress)
            yt.register_on_complete_callback(self.on_complete)
            if self.thumbnail_url is None:
                self.thumbnail_url = yt.thumbnail_url

            if self.is_audio:
                stream = yt.streams.filter(only_audio=True).first()
                if self._filename is None:
                    self._filename = safe_filename(stream.player_config_args['title'])
                stream.download(filename=self._filename)
            else:
                all_streams = yt.streams.filter(file_extension='mp4', progressive=True).all()
                is_download = False
                if self._filename is None:
                    self._filename = safe_filename(all_streams[0].player_config_args['title'])
                for stream in all_streams:
                    if stream.resolution == res:
                        stream.download(filename=self._filename)
                        is_download = True
                        break

                if not is_download:
                    print("[[ {} ]] video isn't available on the given resolution: {}".format(self._filename, res))
                    return False
            self.clean_up(default_directory)
            return True
        except KeyboardInterrupt as error:
            print(str(error))
            self.remove_errr_file()
            return False
        except BaseException as error:
            print(str(error))
            self.remove_errr_file()
            return False

    def remove_errr_file(self):
        if self.is_audio:
            os.remove(self._filename + '.mp3')
        else:
            os.remove(self._filename + '.mp4')


if __name__ == '__main__':
    file = open('request_url.txt', 'r')
    if len(sys.argv) > 1:
        is_audio = True if sys.argv[1] == 'mp3' else False
    else:
        is_audio = False
    for url in file:
        Main(_is_audio=is_audio).start_download(url, res='720p')
    print("Goodbye :)")
