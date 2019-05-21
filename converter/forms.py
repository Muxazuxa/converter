from django import forms
from .models import Data


class DataForm(forms.ModelForm):
    url = forms.RegexField(regex=r'^(http(s)?:\/\/)?((w){3}.)?youtu(be|.be)?(\.com)?\/.+')

    class Meta:
        model = Data
        fields = ('url', 'email')