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
            'email': 'Email',
            'rank': 'Rank',
        }

        self.fields['email'].widget.attrs['autofocus'] = True
