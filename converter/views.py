from django.shortcuts import render
from django.core.mail import send_mail
from .forms import DataForm
from .models import Data
from django.conf import settings
import youtube_dl
from .tasks import convert_mp3

# Create your views here.


def converter(request):
    form = DataForm(request.POST or None)
    if form.is_valid():
        url = form.cleaned_data.get('url')
        email = form.cleaned_data.get('email')
        convert_mp3.delay(url, email)
        return render(request, 'converter/download.html', {'form': form, 'success': 'Check your email {}'. format(email)})
    return render(request, 'converter/download.html', {'form': form})



