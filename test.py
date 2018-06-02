import re
import sys

from pytube import YouTube
import os.path
import glob


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


def stream_call(_url, x):
    yt = YouTube(str(_url))
    z = [yt.streams.filter(file_extension='mp4', progressive=True).first()]
    print(z)
    for y in z:
        title = y.player_config_args['title']
        _filename = safe_filename(title)
        final_filename = _filename + '.' + y.subtype
        if glob.glob(os.path.realpath(final_filename)):
            print("found " + str(final_filename))
        else:
            print("Not found " + str(final_filename))
            print("Complete file path " + str(os.path.realpath(final_filename)))
    sys.exit()


file = open('request_url.txt', 'r')
x = []
stream_call('https://www.youtube.com/watch?v=8mCCMhuKEYw', x)
# for line in file:
#     stream_call(line, x)

for filename in x:
    if glob.glob(os.path.realpath(filename + ".*")):
        print("found " + str(filename))
    else:
        print("Not found " + str(filename))
        print("Complete file path " + str(os.path.realpath(filename + ".*")))
