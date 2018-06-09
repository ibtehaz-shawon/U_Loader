import asyncio
import glob
import os
import os.path
import sys

from pytube import YouTube
from util import safe_filename


class Main:

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

    def start_download(self, _url, is_audio=False):
        try:
            yt = YouTube(str(_url))
            yt.register_on_progress_callback(self.on_progress)
            yt.register_on_complete_callback(self.on_complete)
            _ = yt.streams.filter(file_extension='mp4', progressive=True).first()
            _filename = safe_filename(_.player_config_args['title'])

            print(yt
                  .streams
                  .filter(only_audio=True)
                  .all())
            if glob.glob(_filename):
                print("File already available [[ {} ]] ".format(str(os.path.realpath(_filename))))
                return False
            else:
                # print(yt
                #       .streams
                #       .filter(file_extension='mp4', progressive=True)
                #       .first().parse_codecs())
                if is_audio:
                    yt.streams.filter(only_audio=True).first().download()
                    os.rename(_filename + '.mp4', _filename + '.mp3')
                else:
                    yt.streams.filter(file_extension='mp4', progressive=True).first().download()
                return True
        except KeyboardInterrupt as error:
            sys.exit(str(error))
        except BaseException as error:
            sys.exit((str(error)))
        finally:
            return True


if __name__ == '__main__':
    file = open('request_url.txt', 'r')
    loopie = asyncio.new_event_loop()
    asyncio.set_event_loop(loopie)
    tasks = []
    for url in file:
        if Main().start_download(url, is_audio=True):
            break
