from django import forms
from .models import contact

class ContactForm(forms.ModelForm):

    class Meta:
        model = contact
        fields = '__all__'

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
        placeholders = {
            'email': 'Email',
            'subject': 'Subject',
            'message': 'Message' ,
        }

        self.fields['email'].widget.attrs['autofocus'] = True