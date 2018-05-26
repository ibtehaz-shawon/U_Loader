import asyncio
from pytube import YouTube
import os


class Main:
    @staticmethod
    def show_progress_bar(stream, chunk, file_handle, bytes_remaining):
        bytes_remaining = bytes_remaining / (1000 * 1000)
        file_name = os.path.basename(file_handle.name)
        print('Downloading {}, remaining {} mb'.format(file_name, bytes_remaining))
        return

    @staticmethod
    async def start_download(_url):
        print("Hitting url ... {}".format(_url))
        yt = YouTube(str(_url))
        yt.register_on_progress_callback(Main().show_progress_bar)
        yt.streams.first().download()


if __name__ == '__main__':
    urls = ['https://www.youtube.com/watch?v=76k991G0sJo',
            'https://www.youtube.com/watch?v=6ED9QP6P5rI']
    loopie = asyncio.new_event_loop()
    asyncio.set_event_loop(loopie)

    tasks = [asyncio.ensure_future(Main().start_download(urls[0])),
             asyncio.ensure_future(Main().start_download(urls[1]))]
    loopie.run_until_complete(asyncio.gather(*tasks))
