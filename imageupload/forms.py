from django import forms
from .models import ImageColor
from django.core.exceptions import ValidationError
from PIL import Image

class ImageColorForm(forms.ModelForm):
    class Meta:
        model = ImageColor
        fields = ['title', 'image']

    def validate_if_image(self):
        image = self.cleaned_data.get('image')
        if not image:
            raise ValidationError("No image uploaded!")

        try:
            img = Image.open(image)
            img.verify() 
        except Exception:
            raise ValidationError("The uploaded file is not a valid image!")    