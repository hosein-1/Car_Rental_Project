from django import forms

from .models import Reservation


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['driver', 'start_date', 'end_date', 'delivery_address']
