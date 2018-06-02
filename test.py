import sys

from pytube import YouTube
import os.path
import glob


def stream_call(_url, x):
    yt = YouTube(str(_url))
    # x.append(yt.streams.first.default_filename)
    # print()
    # print(yt.streams.first.default_filename)
    z = yt.streams.all()

    for y in z:
        print(y.default_filename + " --- "+y.mime_type)
    sys.exit()


file = open('request_url.txt', 'r')
x = []
stream_call('https://www.youtube.com/watch?v=8mCCMhuKEYw', x)
# for line in file:
#     stream_call(line, x)

for filename in x:
    if glob.glob(os.path.realpath(filename+".*")):
        print("found "+str(filename))
    else:
        print("Not found "+str(filename))
        print("Complete file path "+str(os.path.realpath(filename+".*")))

