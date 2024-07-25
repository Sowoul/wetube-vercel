from flask import Flask, request, render_template
from pytube import YouTube

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        link = request.form['link']
        try:
            print(link)
            obj = YouTube(link)
            yt = obj.streams.get_lowest_resolution()
            yt.download()
            return f'<b>Successfully downloaded:</b> {obj.title}'
        except Exception as e:
            return f'Error: {str(e)}'

    return render_template('index.html')

if __name__ == '__main__':
    app.run(port=8080)


if __name__ == '__main__':
    app.run(port=8080)
    pass
