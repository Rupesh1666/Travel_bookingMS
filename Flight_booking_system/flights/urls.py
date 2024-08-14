from django.urls import path
from . import views

urlpatterns = [

    path('', views.search_flights, name='search_flights'),
    path('search/', views.search_flights, name='search_flights'),
    path('book/<int:flight_id>/', views.book_flight, name='book_flight'),
    path('flight/<int:flight_id>/', views.flight_detail, name='flight_detail'),
    path('booking_confirmation/<int:booking_id>/', views.booking_confirmation, name='booking_confirmation'),
]
