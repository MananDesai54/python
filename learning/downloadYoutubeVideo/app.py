import pytube;

link = input('Enter the link');

video = pytube.YouTube(link);

downloads = video.streams.all();

# print(download);
# for download in downloads:
#     print(download);

downloads[1].download();

print('downloaded');