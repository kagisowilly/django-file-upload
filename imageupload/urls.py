from django.urls import path
from .views import upload_image, image_list, image_detail

urlpatterns = [
    path('', upload_image, name='upload'), 
    path('images/', image_list, name='images'), 
    path('images/<int:image_id>/', image_detail, name='image_detail'),
]
