import praw
import requests
import urllib.request
import time
import keyboard
from PIL import Image
import math

# PRAW credentials (lookup on reddit if you dont know and fill the arguments below)
reddit = praw.Reddit(client_id='',
                     client_secret='',
                     username='',
                     password='',
                     user_agent='')


def DLimage(url, filePath, fileName):
    fullPath = filePath + fileName + '.jpg'
    urllib.request.urlretrieve(url, fullPath)


# folder path to store downloaded images (enter below)
filePath = "C:/....."

subreddit = reddit.subreddit('')# subreddit to take images from

numPics = 0
new_meme_found = False
photoAlbum = []
fileName = ""
DLname = ""

while not new_meme_found:
    numPics = numPics + 10
    new_memes = subreddit.hot(limit=numPics)  # .hot/.rising/.new
    for submission in new_memes:
        if submission.is_self:  # checking if post is only text.
            print("Post was text, skip.")
            continue

        url = submission.url
        fileName = submission.title
        ##dlname for windows file naming convention
        DLname = submission.title
        DLname = DLname.replace("?", "qestion")
        DLname = DLname.replace("*", "astriks")
        DLname = DLname.replace(".", "pointo")


        # if already posted once, go to next one
        meme_file = open("memes.txt", "r")
        content = meme_file.readlines()
        if fileName + "\n" in content:
            print(fileName + " : has already been posted")
            meme_file.close()
            continue
        else:
            meme_file.close()
            try:
                DLimage(url, filePath, DLname)
            except:
                print("scratch that, next post.")
                continue

            new_meme_found = True
            break


meme_file = open("memes.txt", "a")
print(fileName + " : is a new meme yay ")
meme_file.write(fileName + "\n")
meme_file.close()

fullPath = filePath + DLname + '.jpg'

img = Image.open(fullPath)
width, height = img.size
img = img.resize((1000, 1020), Image.NEAREST)  # image resize. width/height
img = img.convert("RGB")
img.save(fullPath)
photoAlbum.append({
    'type': 'photo',
    'file': fullPath,
})

print(photoAlbum)


