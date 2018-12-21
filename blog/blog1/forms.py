from django.db import models
from django import forms
from .models import Posts

class PostForm(forms.ModelForm):
    class Meta:
        model=Posts
        fields={"title","content","image"}
