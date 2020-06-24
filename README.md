# reddit-instagram-bot
Bot built with UiPath and Python that scraps posts from reddit and uploads them automatically to instagram.
It is one of the very few ones that does not get detected by the anti-bot system.

*Important: you need to fill in the gaps in both scripts with the correct data (path to the script, path to download folder etc.). Use chrome browser to avoid potential errors.*

This bot calls a python script that uses PRAW API to get posts from a subreddit of your choice. It automatically filters out duplicates on multiple calls,
resizes the image for instagram standarts and autodeletes the image from your computer after posting.

UiPath will open instagram in your browser in mobile mode and post your picture, automatically like it and comments specified hashtags.
Also has follow/unfollow features.
