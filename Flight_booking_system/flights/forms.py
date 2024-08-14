from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['passenger_name', 'seat_number']

# manuallt
# flights/forms.py

from django import forms

class FlightSearchForm(forms.Form):
    departure_city = forms.CharField(max_length=100, required=False, label='Departure City')
    arrival_city = forms.CharField(max_length=100, required=False, label='Arrival City')
    departure_date = forms.DateField(required=False, label='Departure Date', widget=forms.TextInput(attrs={'type': 'date'}))

