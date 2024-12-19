from django.db import models
from django.core.validators import RegexValidator
from .utils import extract_center_color


class ImageColor(models.Model):
    title = models.CharField(max_length=55)
    image = models.ImageField(upload_to='images/') 
    hex_color = models.CharField(max_length=7, null=True, blank=True)
    
    class Meta:
        app_label = 'imageupload'


    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  

        self.hex_color = extract_center_color(self.image.path)
        super().save(*args, **kwargs)  

    def __str__(self):
        return f"{self.image} - {self.hex_color}"
