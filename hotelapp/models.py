from django.db import models


class Hotel(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=300)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return self.name


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)

class Room(models.Model):
    CATEGORY_CHOICES = [
        ('Deluxe', 'Deluxe'),
        ('Suite', 'Suite'),
        ('Executive', 'Executive'),
        ('Family', 'Family'),
        ('Presidential', 'Presidential'),
        ('Honeymoon', 'Honeymoon'),
    ]
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='Deluxe')
    description = models.TextField()
    capacity = models.IntegerField()
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    image = models.ImageField(upload_to='rooms/')

    def __str__(self):
        return f"{self.title} ({self.category})"
