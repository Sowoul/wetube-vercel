import os
import uuid
from pytubefix import YouTube
from flask import Flask, request, send_file,render_template,redirect,url_for

app = Flask(__name__)

@app.route('/home')
def hom():
    return render_template('home.html')
@app.route('/')
def strm():
    link = request.args.get('link')
    if link is None:
        return redirect(url_for('hom'))
    else: 
        pass
    try:
        obj = YouTube(link)
        yt = obj.streams.get_highest_resolution()

        unique_filename = str(uuid.uuid4()) + '.mp4'

        temp_directory = '/tmp'
        temp_file = os.path.join(temp_directory, unique_filename)

        yt.download(output_path=temp_directory, filename=unique_filename)

        return send_file(temp_file, as_attachment=True,download_name=f'{obj.title}.mp4')
    except Exception as e:
        return f'Error: {str(e)}'


if __name__ == '__main__':
    app.run(port=8080, debug=True)
