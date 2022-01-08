The link to transcript service is https://transcribe-2-braille.herokuapp.com/

Instructions 

1. Copy your video channel's URL in YouTube website.
2. Paste it into the text box in the web app on Heroku. 
3. Press the enter key or click the submit button.
4. Read a transcript.

Issues

1/8/2022

"pafy" module had issues with dislike counts in YouTube, because I was not able to retrieve a transcript. After commenting out "self._dislikes = self._ydl_info['dislike_count']" on line 54 in backend_youtube_dl.py, I was able to retrieve a transcript from YouTube.
