from django.urls import path
from .views import Home, About, Package, Amenities, Contact

urlpatterns = [
    path('', Home, name='Home'),
    path('about', About, name='About'),
    path('package', Package, name='Package'),
    path('amenities', Amenities, name='Amenities'),
    path('contacts', Contact, name='Contact'),
    # path('review', Review, name='Review')
]
