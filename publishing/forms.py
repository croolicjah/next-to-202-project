from django import forms

from .models import Photo
# from ckeditor.widgets import CKEditorWidget


class AddPhotoForm(forms.ModelForm):

    file_field = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
    class Meta:
        model = Photo
        fields = '__all__'

