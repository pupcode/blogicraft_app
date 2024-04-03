from django import forms
from .models import Announcement, Blog, Tag, Comment

class AnnouncementForm(forms.ModelForm):
    class Meta:
        model = Announcement
        fields = ['message']
        widgets = {
            'message': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Enter your announcement here...'}),
        }



class BlogForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(queryset=Tag.objects.all(), widget=forms.CheckboxSelectMultiple)
    
    class Meta:
        model = Blog
        fields = ['title', 'teaser' , 'paragraph1', 'paragraph2', 'paragraph3', 'quote','image1', 'image2','tags' ]

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'id': 'title', 'placeholder': 'Enter title'}),
            'teaser': forms.TextInput(attrs={'class': 'form-control', 'id': 'teaser', 'placeholder': 'Enter teaser'}),
            'paragraph1': forms.Textarea(attrs={'class': 'form-control', 'id': 'paragraph1', 'rows': '5', 'placeholder': 'Enter first paragraph'}),
            'paragraph2': forms.Textarea(attrs={'class': 'form-control', 'id': 'paragraph2', 'rows': '5', 'placeholder': 'Enter second paragraph'}),
            'paragraph3': forms.Textarea(attrs={'class': 'form-control', 'id': 'paragraph3', 'rows': '5', 'placeholder': 'Enter third paragraph'}),
            'quote': forms.Textarea(attrs={'class': 'form-control quote-field', 'id': 'quote', 'rows': '3', 'placeholder': 'Enter Quote'}),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter your comment here'}),
        }