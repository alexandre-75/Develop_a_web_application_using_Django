from django import forms
from .models import Ticket

class NewTicketForm(forms.ModelForm):
    title = forms.CharField(
        label="Title",
        max_length=200,
        widget=forms.TextInput()
    )
    description = forms.CharField(
        label="Description",
        max_length=10000,
        widget=forms.Textarea(),
        required=False
    )
    image = forms.ImageField(
        label="Image",
        required=False
    )

    class Meta:
        model = Ticket
        fields = ['title', 'description', 'image']