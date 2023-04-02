from django.shortcuts import render, redirect
from .models import Place
from .forms import NewPlaceForm



# Create your views here.
def place_list(request):
    if request.method == 'POST':
        form = NewPlaceForm(request.POST) # makes a form from the data in the request
        place.form.save() # create a model from object from the form
        if form.is_valid(): # validation against DB constraints
            place.save() # actually saved the data to the DB 
            redirect('place_list') # redirects to the home page (by name)

    places = Place.objects.filter(visited=False).order_by('name')
    new_place_form = NewPlaceForm()
    return render(request, 'travel_wishlist/wishlist.html', {'places':places, 'new_place_form':new_place_form})


def about(request):
    author = 'Marty M.'
    about = 'A website that creates and saves a list of places to visit'
    return render(request, 'travel_wishlist/about.html', {'author':author, 'about':about})