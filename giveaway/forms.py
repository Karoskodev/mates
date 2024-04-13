from django import forms
from .models import giveaway


class GiveawayForm(forms.ModelForm):

    class Meta:
        model = giveaway
        fields = '__all__'

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
        placeholders = {
            'answer':'Answer',
            'rating':'Rating',
            'email': 'Email',
        }

        self.fields['email'].widget.attrs['autofocus'] = True
