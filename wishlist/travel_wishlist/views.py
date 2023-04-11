from django.shortcuts import render, redirect, get_object_or_404
from .models import Place
from .forms import NewPlaceForm, TripReviewForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.contrib import messages
# Create your views here.
@login_required
def place_list(request):
    if request.method == 'POST':
        form = NewPlaceForm(request.POST) # makes a form from the data in the request
        place = form.save(commit=False) # create a model from object from the form
        place.user = request.user
        if form.is_valid(): # validation against DB constraints
            place.save() # actually saved the data to the DB 
            redirect('place_list') # redirects to the home page (by name)

    places = Place.objects.filter(user=request.user).filter(visited=False).order_by('name')
    new_place_form = NewPlaceForm()
    return render(request, 'travel_wishlist/wishlist.html', {'places':places, 'new_place_form':new_place_form})


@login_required
def about(request):
    author = 'Marty M.'
    about = 'A website that creates and saves a list of places to visit'
    return render(request, 'travel_wishlist/about.html', {'author':author, 'about':about})

@login_required
def places_visited(request):
    visited = Place.objects.filter(user=request.user).filter(visited=True)
    return render(request, 'travel_wishlist/visited.html', {'visited':visited})

@login_required
def place_was_visited(request, place_pk):
    if request.method == 'POST':
        # place = Place.objects.get(pk=place_pk)
        place = get_object_or_404(Place, pk=place_pk) # super useful shortcut.... i dont have to do the logic with this shortcut. :)
        if place.user == request.user:
            place.visited = True
            place.save()
        else:
            return HttpResponseForbidden()
    return redirect('place_list')

@login_required
def place_details(request, place_pk):
    place = get_object_or_404(Place, pk=place_pk)
    if place.user != request.user:
        return HttpResponseForbidden()
    if request.method == 'POST':
        form = TripReviewForm(request.POST, request.FILES, instance = place)
        if form.is_valid():
            form.save()
            messages.info(request, 'Trip Information Updated!')
        else:
            messages.error(request, form.errors) #Temp, will make look better later. 
        return redirect('place_details', place_pk = place_pk)
    else:
        if place.visited:
            review_form = TripReviewForm(instance = place)
            return render(request, 'travel_wishlist/place_detail.html', {'place':place, 'review_form':review_form})
        else:
            return render(request, 'travel_wishlist/place_detail.html', {'place':place})

    return render(request, 'travel_wishlist/place_detail.html', {'place':place})


@login_required
def delete_place(request, place_pk):
    place = get_object_or_404(Place, pk=place_pk)
    if place.user == request.user:
        place.delete()
        return redirect('place_list')
    else:
        return HttpResponseForbidden()