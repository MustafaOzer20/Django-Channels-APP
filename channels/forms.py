from django import forms
from channels.models import Channels, ChannelMessages

class CreateChannelForm(forms.ModelForm):
    class Meta:
        model = Channels
        fields = ['title', 'is_private']


class MessageForm(forms.ModelForm):
    class Meta:
        model = ChannelMessages
        fields = ['message']
        widgets = {
            'message': forms.Textarea(attrs={
                'placeholder': 'Type your message here',
                'rows': '5',
            }),
        }
        labels = {
            'message': '',
        }
