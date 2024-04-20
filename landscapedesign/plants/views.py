from django.shortcuts import render, redirect
from .models import Plant, Image
from .forms import ImageForm


def plant_list(request):
    plants = Plant.objects.all()
    return render(request, 'plants/plant_list.html', {'plants': plants})

def gallery(request):
    images = Image.objects.all()
    return render(request, 'plants/gallery.html', {'images': images})

def add_gallery(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Get the current instance object to display in the template
            img_obj = form.instance
            return render(request, 'plants/add_gallery.html', {'form': form, 'img_obj': img_obj})
    else:
        form = ImageForm()
    return render(request, 'plants/add_gallery.html', {'form': form})



def add_plant(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        color = request.POST.get('color')
        height = request.POST.get('height')
        description = request.POST.get('description')
        date = request.POST.get('date')
        Plant.objects.create(name=name, color=color, height=height, description=description, date=date)
        return redirect('plant_list')

    return render(request, 'plants/add_plant.html', )

def delete_plant(request, pk):
    plant = Plant.objects.get(pk=pk)
    if request.method == 'POST':
        plant.delete()
        return redirect('plant_list')
    return render(request, 'plants/delete_plant.html', {'plant': plant})

def delete_gallery(request, pk):
    image = Image.objects.get(pk=pk)
    if request.method == 'POST':
        image.delete()
        return redirect('gallery')
    return render(request, 'plants/delete_gallery.html', {'image': image})


