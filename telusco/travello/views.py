from django.shortcuts import render
from .models import Destination

# Create your views here.

def index(request):

    # dest1 = Destination()
    # dest1.name = "Pokhara"
    # dest1.desc = "City by the lake"
    # dest1.price = 500
    # dest1.img = 'destination_1.jpg'
    # dest1.offer = False

    # dest2 = Destination()
    # dest2.name = "Biratnagar"
    # dest2.desc = "City of thousand hearts"
    # dest2.price = 400
    # dest2.img = 'destination_2.jpg'
    # dest2.offer = True


    # dest3 = Destination()
    # dest3.name = "Nepalgunj"
    # dest3.desc = "City of hotness"
    # dest3.price = 600
    # dest3.img = 'destination_3.jpg'
    # dest3.offer = False

    # dests = [dest1, dest2, dest3]

    dests = Destination.objects.all()

    return render(request, "index.html", {'dests': dests})