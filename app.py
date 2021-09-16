from flask import Flask,render_template,request
from youtube_transcript_api import YouTubeTranscriptApi
import re
import pafy   

app = Flask(__name__)

@app.route('/')
def form():
    return render_template('form.html')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/result',methods = ['POST', 'GET'])
def result():
    if request.method == 'POST':
        result = request.form.get("yt_url")
        source_video_id = pafy.new(result)
        video_id = source_video_id.videoid
        title = source_video_id.title
        author = source_video_id.author
        #upload_date = source_video_id.published
        script = ""
        
        try:
            YouTubeTranscriptApi.get_transcript(video_id)
            transcript = YouTubeTranscriptApi.get_transcript(video_id)
            for text in transcript:
                t = text["text"]
                if t != '[Music]':
                    script += t + " "
            return render_template("result.html", script=script)

        except:
            return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)    
