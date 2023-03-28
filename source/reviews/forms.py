from django import forms
from .models import Ticket, Review

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
    class Meta:
        model = Ticket
        fields = ['title', 'description']

STARS = (
    (0, "- 0"), 
    (1, "- 1"), 
    (2, "- 2"), 
    (3, "- 3"), 
    (4, "- 4"), 
    (5, '- 5'),
)

class NewReviewForm(forms.ModelForm):
    headline = forms.CharField(
        label="Title",
        max_length=200,
        widget=forms.TextInput()
    )
    rating = forms.ChoiceField(
        initial=0,
        label="Rating",
        widget=forms.RadioSelect(),
        choices = STARS
    )
    body = forms.CharField(
        label="Review",
        max_length=8000,
        widget=forms.Textarea(),
        required=False
    )
    class Meta:
        model = Review
        fields = ['headline', 'rating', 'body']