__author__ = 'omojumiller'

from django import forms

TOPIC_CHOICES = (
           ('general', 'General enquiry'),
           ('bug', 'Bug report'),
           ('suggestion', 'Suggestion'),
                )

class ContactForm(forms.Form):
    topic = forms.ChoiceField(choices=TOPIC_CHOICES)
    message = forms.CharField(widget=forms.Textarea())
    sender = forms.EmailField(required=False)

def clean_message(self):
               message = self.clean_data.get('message', '')
               num_words = len(message.split())
               if num_words < 4:
                   raise forms.ValidationError("Not enough words!")
               return message