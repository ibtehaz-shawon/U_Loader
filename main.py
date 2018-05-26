import asyncio
import sys
from pytube import YouTube
from threading import Thread
import os


class Main:

    def __init__(self):
        self._thread = None

    def on_complete(self, stream, file_handle):
        file_name = os.path.basename(file_handle.name)
        print("Download complete {}".format(file_name))
        self._thread.join()
        return

    @staticmethod
    def on_progress(stream, chunk, file_handle, bytes_remaining):
        bytes_remaining = bytes_remaining / (1000 * 1000)
        file_name = os.path.basename(file_handle.name)
        print('Downloading {}, remaining {} mb'.format(file_name, bytes_remaining))
        return

    async def start_download(self, _url, running_thread):
        try:
            self._thread = running_thread
            print("Hitting url ... {}".format(_url))
            yt = YouTube(str(_url))
            yt.register_on_progress_callback(self.on_progress)
            yt.register_on_complete_callback(self.on_complete)
            yt.streams.first().download()
        except KeyboardInterrupt as error:
            sys.exit(str(error))


if __name__ == '__main__':
    urls = ['https://www.youtube.com/watch?v=76k991G0sJo',
            'https://www.youtube.com/watch?v=6ED9QP6P5rI']
    loopie = asyncio.new_event_loop()
    asyncio.set_event_loop(loopie)
    tasks = []
    for url in urls:
        thread = Thread()
        thread.start()
        tasks.append(asyncio.ensure_future(Main().start_download(url, thread)))
    loopie.run_until_complete(asyncio.gather(*tasks))
