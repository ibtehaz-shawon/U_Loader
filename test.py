import re
import sys

from pytube import YouTube
import os.path
import glob

from main import Main


def unicode(s):
    """No-op."""
    return s


def safe_filename(s, max_length=255):
    """Sanitize a string making it safe to use as a filename.

    This function was based off the limitations outlined here:
    https://en.wikipedia.org/wiki/Filename.

    :param str s:
        A string to make safe for use as a file name.
    :param int max_length:
        The maximum filename character length.
    :rtype: str
    :returns:
        A sanitized string.
    """
    # Characters in range 0-31 (0x00-0x1F) are not allowed in ntfs filenames.
    ntfs_chrs = [chr(i) for i in range(0, 31)]
    chrs = [
        '\"', '\#', '\$', '\%', '\'', '\*', '\,', '\.', '\/', '\:', '"',
        '\;', '\<', '\>', '\?', '\\', '\^', '\|', '\~', '\\\\',
    ]
    pattern = '|'.join(ntfs_chrs + chrs)
    regex = re.compile(pattern, re.UNICODE)
    filename = regex.sub('', s)
    return unicode(filename[:max_length].rsplit(' ', 0)[0])


def on_complete(stream, file_handle):
    file_name = os.path.basename(file_handle.name)
    print("Download complete {}".format(file_name))
    return


def on_progress(stream, chunk, file_handle, bytes_remaining):
    bytes_remaining = bytes_remaining / (1000 * 1000)
    file_name = os.path.basename(file_handle.name)
    print('Downloading {}, remaining {} mb'.format(file_name, bytes_remaining))
    return


def stream_call(_url, x):
    yt = YouTube(str(_url))
    stream = yt.streams.filter(file_extension='mp4', progressive=True).first()
    title = stream.player_config_args['title']
    _filename = safe_filename(title)
    final_filename = _filename + '.' + stream.subtype
    if glob.glob('~/Music/' + final_filename):
        print("found " + str(final_filename))
    else:
        print("Not found " + str(final_filename))
        print("Complete file path " + str('~/Music/' + final_filename))

        if not os.path.exists(_filename):
            with open(_filename, 'w'):
                pass
        # yt.register_on_progress_callback(on_progress) \
        #     .register_on_complete_callback(on_complete)
        yt.streams.filter(file_extension='mp4', progressive=True).first()\
            .download(filename=final_filename)
        # .register_on_progress_callback(Main().on_progress)\
        # .register_on_complete_callback(Main().on_complete)\
    print("Download complete!")
    sys.exit()


file = open('request_url.txt', 'r')
x = []
stream_call('https://www.youtube.com/watch?v=uVibq-Uvmvc', x)
# for line in file:
#     stream_call(line, x)

# for filename in x:
#     if glob.glob(os.path.realpath(filename + ".*")):
#         print("found " + str(filename))
#     else:
#         print("Not found " + str(filename))
#         print("Complete file path " + str(os.path.realpath(filename + ".*")))
