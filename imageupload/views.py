from django.shortcuts import render, redirect, get_object_or_404
from .models import ImageColor
from .forms import ImageColorForm

def upload_image(request):
    if request.method == 'POST':
        form = ImageColorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('images')
        else:
            return render(request, 'image_upload.html', {'form': form})
    else:
        form = ImageColorForm()
    return render(request, 'image_upload.html', {'form': form})


def image_list(request):
    images = ImageColor.objects.all()
    return render(request, 'image_lists.html', {'images': images})

def image_detail(request, image_id):
    image = get_object_or_404(ImageColor, id=image_id)
    return render(request, 'image_details.html', {'image': image})