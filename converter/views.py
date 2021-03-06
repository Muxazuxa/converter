from django.shortcuts import render
from .forms import DataForm
from .tasks import convert_mp3
from video_converter import settings
import os
from django.conf import settings
from django.http import HttpResponse, Http404

# Create your views here.


def converter(request):
    form = DataForm(request.POST or None)
    if form.is_valid():
        protocol = request.scheme
        host = request.META['HTTP_HOST']
        url = form.cleaned_data.get('url')
        email = form.cleaned_data.get('email')
        form.save()
        convert_mp3.delay(url, email, protocol, host)
        return render(request, 'converter/download.html', {'form': form, 'success': 'Check your email {}'. format(email)})
    return render(request, 'converter/download.html', {'form': form})


def download(request, name):
    file_path = os.path.join(settings.MEDIA_ROOT, name)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/force-download")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    raise Http404