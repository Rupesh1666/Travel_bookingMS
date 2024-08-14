from django.db import models

class Flight(models.Model):
    flight_number = models.CharField(max_length=100)
    departure_city = models.CharField(max_length=100)
    arrival_city = models.CharField(max_length=100)
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    # Add additional fields as needed

    def __str__(self):
        return self.flight_number

class Booking(models.Model):
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    passenger_name = models.CharField(max_length=100)
    seat_number = models.CharField(max_length=10)
    booking_date = models.DateTimeField(auto_now_add=True)
    # Add additional fields as needed

    def __str__(self):
        return f"{self.passenger_name} - {self.flight}"
