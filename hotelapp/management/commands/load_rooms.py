# hotelapp/management/commands/load_rooms.py
from django.core.management.base import BaseCommand
from hotelapp.models import Room
from django.core.files import File
from pathlib import Path

class Command(BaseCommand):
    help = 'Load default room data with categories'

    def handle(self, *args, **kwargs):
        # Optional: Clear existing rooms
        Room.objects.all().delete()

        rooms = [
            {
                'title': 'Deluxe Room',
                'category': 'Deluxe',
                'description': 'Spacious room with modern amenities and elegant interiors.',
                'capacity': 2,
                'price_per_night': 5000,
                'available': True,
                'image': 'delu1.jpg',
            },
            {
                'title': 'Suite Room',
                'category': 'Suite',
                'description': 'Luxury suite with premium services and comfortable seating.',
                'capacity': 3,
                'price_per_night': 8000,
                'available': True,
                'image': 'suit1.jpg',
            },
            {
                'title': 'Executive Room',
                'category': 'Executive',
                'description': 'Elegant and cozy setup for business travelers.',
                'capacity': 2,
                'price_per_night': 6000,
                'available': True,
                'image': 'exe1.jpg',
            },
            {
                'title': 'Family Suite',
                'category': 'Family',
                'description': 'Perfect for families — spacious and comfortable.',
                'capacity': 4,
                'price_per_night': 9000,
                'available': True,
                'image': 'fam1.jpg',
            },
            {
                'title': 'Presidential Suite',
                'category': 'Presidential',
                'description': 'Top-tier luxury with private lounge and premium amenities.',
                'capacity': 4,
                'price_per_night': 15000,
                'available': True,
                'image': 'pres.jpg',
            },
            {
                'title': 'Honeymoon Suite',
                'category': 'Honeymoon',
                'description': 'Romantic setup with elegant décor, perfect for couples.',
                'capacity': 2,
                'price_per_night': 12000,
                'available': True,
                'image': 'hon1.jpg',
            },
        ]

        for r in rooms:
            image_path = Path('hotelapp/static/images/rooms') / r['image']  # path where images exist
            with open(image_path, 'rb') as f:
                r['image'] = File(f)
                Room.objects.create(**r)