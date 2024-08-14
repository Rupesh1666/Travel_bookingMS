# from django.shortcuts import render, redirect, get_object_or_404
# from .models import Flight, Booking
# from .forms import BookingForm

# # def search_flights(request):
# #     if request.method == "GET":
# #         departure_city = request.GET.get('departure_city')
# #         arrival_city = request.GET.get('arrival_city')
# #         departure_date = request.GET.get('departure_date')
# #         flights = Flight.objects.filter(
# #             departure_city=departure_city,
# #             arrival_city=arrival_city,
# #             departure_time__date=departure_date
# #         )
# #         return render(request, 'flights/search_results.html', {'flights': flights})

# def book_flight(request, flight_id):
#     flight = get_object_or_404(Flight, id=flight_id)
#     if request.method == "POST":
#         form = BookingForm(request.POST)
#         if form.is_valid():
#             booking = form.save(commit=False)
#             booking.flight = flight
#             booking.save()
#             return redirect('booking_confirmation', booking_id=booking.id)
#     else:
#         form = BookingForm()
#     return render(request, 'flights/book_flight.html', {'flight': flight, 'form': form})
# def booking_confirmation(request, booking_id):
#     booking = Booking.objects.get(id=booking_id)
#     return render(request, 'flights/booking_confirmation.html', {'booking': booking})
# def search_flights(request):
#     flights = Flight.objects.all()
#     context = {'flights': flights}
#     return render(request, 'flights/search.html', context)

# def flight_detail(request, flight_id):
#     flight = get_object_or_404(Flight, id=flight_id)
#     bookings = Booking.objects.filter(flight=flight)
#     context = {'flight': flight, 'bookings': bookings}
#     return render(request, 'flights/flight_detail.html', context)






from django.shortcuts import render, redirect, get_object_or_404
from .models import Flight, Booking
from .forms import BookingForm

def search_flights(request):
    flights = Flight.objects.all()
    context = {'flights': flights}
    return render(request, 'flights/search.html', context)

def flight_detail(request, flight_id):
    flight = get_object_or_404(Flight, id=flight_id)
    bookings = Booking.objects.filter(flight=flight)
    context = {'flight': flight, 'bookings': bookings}
    return render(request, 'flights/flight_detail.html', context)

def book_flight(request, flight_id):
    flight = get_object_or_404(Flight, id=flight_id)
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.flight = flight
            booking.save()
            return redirect('booking_confirmation', booking_id=booking.id)
    else:
        form = BookingForm()
    return render(request, 'flights/book_flight.html', {'flight': flight, 'form': form})

def booking_confirmation(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    return render(request, 'flights/booking_confirmation.html', {'booking': booking})


# manually
from .forms import FlightSearchForm
def search_flights(request):
    form = FlightSearchForm(request.GET or None)
    flights = Flight.objects.all()

    if form.is_valid():
        departure_city = form.cleaned_data.get('departure_city')
        arrival_city = form.cleaned_data.get('arrival_city')
        departure_date = form.cleaned_data.get('departure_date')

        if departure_city:
            flights = flights.filter(departure_city__icontains=departure_city)
        if arrival_city:
            flights = flights.filter(arrival_city__icontains=arrival_city)
        if departure_date:
            flights = flights.filter(departure_time__date=departure_date)

    return render(request, 'flights/search.html', {'flights': flights, 'form': form})
