from pytube.cli import on_progress
from pytube import YouTube
from tqdm import tqdm


class YouTubeDownloader():
    #https://youtu.be/BCSlZIUj18Y
    
    link = input('Enter the link of youtube video you want: ')
    yt = YouTube(link, on_progress_callback=on_progress)
    ys = yt.streams.get_highest_resolution()

    
    
    
    def __init__(self, Author):
        self.Author = Author
    
    def video_Title(self):
      Title = self.yt.title 
      print('Title: {}'.format(Title))
      
    def VIEWS(self):
        views = self.yt.views
        print('Number of Views: {}'.format(views))
        
    def Length(self):
        length = self.yt.length
        print('Length of Videos: {}'.format(length))
        
    def Ratings(self):
        v_rating = self.yt.rating
        print('Rating of Video: {}'.format(v_rating))
    
    def Download(self):
        target = self.ys
        print('Downloading...')
        path = 'C:/Users/USER/Desktop/youtube scrabe'
        with tqdm(total=target.filesize, desc='Status',unit='B') as p:
            target.download(path)
            
        print('Download Completed!')

MyYoutubeDownloader = YouTubeDownloader('DANIEL EKWERE')

MyYoutubeDownloader.video_Title()
MyYoutubeDownloader.Length()
MyYoutubeDownloader.VIEWS()
MyYoutubeDownloader.Ratings()
MyYoutubeDownloader.Download()

