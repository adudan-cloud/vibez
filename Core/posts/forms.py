from django import forms
from .models import Post, Event, Message

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["content", "image"]
        widgets = {
            "content": forms.Textarea(attrs={
                "rows": 3,
                "class": "form-control",
                "placeholder": "What's on your mind?"
            }),
            "image": forms.ClearableFileInput(attrs={
                "class": "form-control-file"
            }),
        }
        labels = {
            "content": "Post Content",
            "image": "Upload Image",
        }
        help_texts = {
            "content": "Share your thoughts or updates.",
            "image": "Optional: Add an image to your post.",
        }

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'description', 'date', 'location', 'image']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Event title'
            }),
            'description': forms.Textarea(attrs={
                'rows': 5,
                'class': 'form-control',
                'placeholder': 'Describe the event'
            }),
            'date': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control'
            }),
            'location': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Event location'
            }),
            'image': forms.ClearableFileInput(attrs={
                'class': 'form-control-file'
            }),
        }
        labels = {
            'title': 'Event Title',
            'description': 'Event Description',
            'date': 'Event Date',
            'location': 'Location',
            'image': 'Event Image',
        }
        help_texts = {
            'date': 'Select the date of the event.',
        }

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={
                'rows': 3,
                'class': 'form-control',
                'placeholder': 'Share your thoughts...'
            }),
        }
        labels = {
            'content': 'Message',
        }