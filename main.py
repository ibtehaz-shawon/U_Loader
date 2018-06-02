import asyncio
import glob
import os
import os.path
import sys

from aiomultiprocess import Pool
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

    async def start_download(self, _url):
        try:
            yt = YouTube(str(_url))
            await self.start_stream(yt.streams.filter(file_extension='mp4', progressive=True).first())
        except KeyboardInterrupt as error:
            sys.exit(str(error))

    async def start_stream(self, stream):
        try:
            title = stream.player_config_args['title']
            _filename = safe_filename(title)
            _filename = _filename + '.' + stream.subtype

            if glob.glob('~/Music/' + _filename):
                print("File already available [[ {} ]] ".format(str(os.path.realpath(_filename))))
            else:
                print("Downloading....{}".format('~/Music/' + _filename))
                stream.register_on_progress_callback(self.on_progress)
                stream.register_on_complete_callback(self.on_complete)
                await stream.download(output_path='~/Music/', filename=_filename)
        except KeyboardInterrupt as error:
            sys.exit(str(error))
        finally:
            return

    async def process_pool(self, urls):
        async with Pool(maxtasksperchild=5, childconcurrency=10) as pool:
            result = await pool.map(self.start_download, urls)
            index = 0
            for query in result:
                index += 1
                if query is not None:
                    print("Error in {} -- {}".format(index, str(query)))


if __name__ == '__main__':
    file = open('request_url.txt', 'r')
    loopie = asyncio.new_event_loop()
    asyncio.set_event_loop(loopie)
    tasks = []
    for url in file:
        tasks.append(url)

    loopie.run_until_complete(asyncio.gather(asyncio.ensure_future(Main().process_pool(tasks))))

    # for url in file:
    #     index += 1
    #     tasks.append(asyncio.ensure_future(Main().start_download(url, index)))
    # loopie.run_until_complete(asyncio.gather(*tasks))
