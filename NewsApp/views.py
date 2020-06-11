from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# To work with other database that's not sqlite, you'd have to do pip install databaseclient\
# ie pip install mysqlclient for mysql database.


def Home(request):
    return render(request, 'index.html')


def About(request):
    # extra_data = {
    #     "Feelings": "I feel great learning this"
    # }
    return render(request, 'about.html')


def Package(request):
    return render(request, 'package.html')


def Amenities(request):
    return render(request, 'amenities.html')


def Contact(request):
    return render(request, 'contact.html')


# def Review(request):
#     return render(request, 'contact.html')
