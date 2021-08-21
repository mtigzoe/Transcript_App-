from flask import Flask,render_template,request
from youtube_transcript_api import YouTubeTranscriptApi
import re
import pafy   


app = Flask(__name__)


@app.route('/')
def form():
    return render_template('form.html')


@app.route('/result',methods = ['POST', 'GET'])
def result():
    if request.method == 'POST':
        #result = request.form
        result = request.form.get("yt_url")
      
        source_video_id = pafy.new(result)
        video_id = source_video_id.videoid
        srt = YouTubeTranscriptApi.get_transcript(video_id)
        lines = []
        for i in srt:
            lines.append(i)
        return render_template("result.html", len = len(lines), lines= lines)


if __name__ == '__main__':
    app.run(debug=True)    
