from socket import EBADF
from pytube import YouTube

link = input('insert your YouTube link: ')

yt = YouTube(link)

videos = yt.streams.all()

video = list(enumerate(videos))

for v in video:
    print(v)

print('Enter the desired option to download the format')

dn_option = int(input(' enter the option: '))

dn_video = videos[dn_option]
dn_video.download()

print('Download successfully!')