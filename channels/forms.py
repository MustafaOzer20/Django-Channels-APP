from django import forms
from channels.models import Channels

class CreateChannelForm(forms.ModelForm):
    class Meta:
        model = Channels
        fields = ['title', 'is_private']
