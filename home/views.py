from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import AnonymousUser
from django.core.paginator import Paginator
from django.shortcuts import render, redirect

from home.forms import UploadCarForm, CarUpdateForm
from home.models import CarCategory, Car


def home_page(request):
    return render(request, 'home/index.html')


def cars_list(request):
    car_category = CarCategory.objects.all()
    cars = Car.objects.all()
    context = {
        "cars": cars,
        "car_category": car_category
    }
    return render(request, 'home/listing.html', context)


def read_more(request, pk):
    owner = None
    car = Car.objects.filter(id=pk).first()

    not_anonymous = not (isinstance(request.user, AnonymousUser))
    if not_anonymous and request.user == car.owner:
        owner = True

    context = {
        'car': car,
        'owner': owner,

    }
    return render(request, 'home/readmore.html', context)


def update_car(request, pk):
    car = Car.objects.filter(id=pk).first()
    if request.method == 'POST':
        form = CarUpdateForm(request.POST, request.FILES, instance=car)
        if form.is_valid():
            form.save()
            return redirect('home_page')
    form = CarUpdateForm(instance=car)
    context = {
        'car': car,
        'form': form,
    }
    return render(request, 'home/update_car.html', context)


def delete_car(request, pk):
    car = Car.objects.filter(id=pk).first()
    car.delete()
    return redirect('home_page')


def search(request):
    query = request.GET.get('q')
    cars = Car.objects.filter(title__icontains=query, posted=True)
    print(cars)
    return render(request, 'home/search.html',
                  context={'cars': cars})


@login_required
def upload_car(request):
    if request.method == 'POST':
        form = UploadCarForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
    form = UploadCarForm()
    return render(request, 'home/upload_car.html',
                  context={'form': form})


@login_required
def owner_cars(request):
    cars = Car.objects.filter(owner=request.user)
    paginator = Paginator(cars, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'cars': page_obj
    }
    return render(request, 'home/owner_cars.html', context)

