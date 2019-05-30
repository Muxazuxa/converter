from django.core.mail  import send_mail
from video_converter.celery import app
import youtube_dl
from django.template import loader
from video_converter.settings import EMAIL_HOST_USER, BASE_DIR


@app.task
def convert_mp3(url, email, protocol, host):
    options = {
        'format': 'bestaudio',
        'outtmpl': 'media/%(id)s.%(ext)s',
        'postprocessors': [{
         'key': 'FFmpegExtractAudio',
         'preferredcodec': 'mp3',
         'preferredquality': '192',
         }
        ]
    }

    with youtube_dl.YoutubeDL(options) as youtube:
        info = youtube.extract_info(url)
        id = info['id']
        title = info['title']
        url = protocol + '://' + host + '/media/' + id + '.mp3'
        send_email.delay(url, email, title)


@app.task
def send_email(url, email, title):
    html_message = loader.render_to_string(
        BASE_DIR + '/converter/templates/converter/message.html',
        {
            'url': url,
            'title': title,
        }
    )
    send_mail(
        'Youtube Video Converter',
        'The link is below',
        EMAIL_HOST_USER,
        [email],
        fail_silently=True,
        html_message=html_message
    )