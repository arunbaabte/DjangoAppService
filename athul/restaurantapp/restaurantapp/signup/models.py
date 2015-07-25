from django.db import models
from django import forms

class Document(models.Model):
    docfile = models.FileField(upload_to='documents/%Y/%m/%d')

class DocumentForm(forms.Form):
    docfile = forms.FileField(
        label='Select a file'
    )