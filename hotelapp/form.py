from django import forms
from .models import Booking , Hotel, Room

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = [ 'hotel', 'room']
    def __init__(self, *args, **kwargs):
        super(BookingForm, self).__init__(*args, **kwargs)
        self.fields['hotel'].queryset = Hotel.objects.all()
        self.fields['room'].queryset = Room.objects.filter(is_available=True)