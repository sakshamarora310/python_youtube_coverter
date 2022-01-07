'''
Author: Saksham Arora
Date: 07/01/2022
Summary: This script will download youtube videos in numerous formats.
'''

try:
    import pytube
except ImportError:
    print("Pytube didn't import correctly.")
    print("Please make sure it is installed \
        Run 'pip3 install pytube.' ")
    exit(1)

try:
    url = input("Enter the URL:")
    output_path = input("Enter the output_path:")
    yt = pytube.YouTube(url=url)
except Exception:
    print("Exception Occured...\n")
except KeyboardInterrupt:
    print("\nExiting..\n")
else:

    print(f'Downloading video: {url}')
    yt.streams.filter(progressive=True).get_by_itag(22).download(output_path=output_path)

    '''
    Progressive method is used to download the video in legacy method which includes audio and video in one file
    we use the itag 22 which provides us with the following things:
    
    Stream: itag="22" mime_type="video/mp4" res="720p" fps="25fps" vcodec="avc1.64001F" acodec="mp4a.40.2" progressive="True" type="video"

    Since we are using progessive method, we are limited to 720p, for greater resoutions, we'd have to use adaptive method which includes downloading 
    video and audio seperately and then combining them.
    '''

    '''
    For SSL Issues,
    For MAC:
    1. Open terminal
    2. Run: pip3 install certifi
    3. Run: python3 -m certifi; certifi.where() # The output should be a path to a pem file
    4. Head Over to Application's Folder from within the finder, then Python3 and double click on Install.Certificates.command
    5. Once thats done, this script will not give you any more errors.
    '''
