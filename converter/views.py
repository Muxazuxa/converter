from django.shortcuts import render
from .forms import DataForm
from .models import Data
from .tasks import convert_mp3

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



