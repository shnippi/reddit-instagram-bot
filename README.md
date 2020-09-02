# Reddit to Instagram Bot (Memepage automation)

Scriptbot built with UiPath and Python that scraps posts from reddit and uploads them automatically to instagram.
This is one of the very few ones that does not get detected by the anti-bot system of instagram (to date).

This bot calls a python script that uses PRAW API to get posts from a subreddit of your choice. It automatically filters out duplicates on multiple calls,
resizes the image for instagram standarts, post the picture with the title as caption and autodeletes the image from your computer after posting.

accounts using this:
-@the_provider_of_sauce

## Implemented features include:
- Auto-post (from specified directory)
- Auto-like
- Auto-comment
- Auto-hashtag
- Auto-(un)follow


## Before Use
- fill in specified data in python script (PRAW credentials, directory, ...)
- fill in specified data in UiPath script (Instagram credentials, directory, ...)
- use chrome browser to avoid potential errors
- use UiPath Studio for best .xaml file handling





**Do not spam the bot or instagram will detect it and IP ban you!**
