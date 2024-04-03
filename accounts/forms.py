from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile

class CreateUserForm(UserCreationForm):
    phone_number = forms.CharField(max_length=20, required=False)
    twitter_link = forms.URLField(required=False)  
    facebook_link = forms.URLField(required=False)
    instagram_link = forms.URLField(required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'phone_number', 'twitter_link', 'facebook_link', 'instagram_link']

    def save(self, commit=True):
        user = super(CreateUserForm, self).save(commit=False)
        if commit:
            user.save()
            UserProfile.objects.create(
                user=user,
                phone_number=self.cleaned_data['phone_number'],
                twitter_link=self.cleaned_data['twitter_link'],
                facebook_link=self.cleaned_data['facebook_link'],
                instagram_link=self.cleaned_data['instagram_link']
            )
        return user


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['user_img','first_name', 'last_name', 'other_names', 'phone_number','bio', 'twitter_link', 'facebook_link', 'instagram_link']

    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True
        self.fields['phone_number'].required = True