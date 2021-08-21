from flask import Flask,render_template,request
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import JSONFormatter
import re
import pafy   


app = Flask(__name__)


@app.route('/')
def form():
    return render_template('form.html')


@app.route('/result', methods = ['POST', 'GET'])
def result():
    if request.method == 'POST':

        result = request.form.get("yt_url")
      
        source_video_id = pafy.new(result)
        video_id = source_video_id.videoid
        title = source_video_id.title
        
        transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=['en'])

        formatter = JSONFormatter()

        data = formatter.format_transcript(transcript, indent=2)

        #lines = []
        #for item in data[""]:
        #    lines.append([item["text"]])
        #    return render_template("result.html", title=title, len=len(lines), lines=lines)

        return render_template("result.html", title=title, data=data)

        #srt = YouTubeTranscriptApi.get_transcript(video_id)
        #lines = []
        #for i in srt:
        #    lines.append(i)
        #return render_template("result.html", len = len(lines), lines= lines)


if __name__ == '__main__':
   
    app.run(debug=True)
  
  