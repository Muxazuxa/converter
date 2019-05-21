from django.core.mail  import send_mail
from video_converter.celery import app
import youtube_dl
from django.template import loader


@app.task
def convert_mp3(url, email):
    options = {
        'format': 'bestaudio/best',
        'outtmpl': '%(title)s.%(ext)s',
        'postprocessors': [{
         'key': 'FFmpegExtractAudio',
         'preferredcodec': 'mp3',
         'preferredquality': '192',
         }
        ]
    }

    with youtube_dl.YoutubeDL(options) as youtube:
        info = youtube.extract_info(url, download=False)
        url = info['url']
        title = info['title']
        send_email.delay(url, email, title)


@app.task
def send_email(url, email, title):
    html_message = loader.render_to_string(
        '/home/jenish/Desktop/video_converter/converter/templates/converter/message.html',
        {
            'url': url,
            'title': title,
        }
    )
    send_mail(
        'Youtube Video Converter',
        'The link is below',
        'mursidinovz@gmail.com',
        [email],
        fail_silently=True,
        html_message=html_message
    )