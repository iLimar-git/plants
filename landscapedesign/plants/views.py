from django.shortcuts import render, redirect
from .models import Plant


def plant_list(request):
    plants = Plant.objects.all()
    return render(request, 'plants/plant_list.html', {'plants': plants})

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