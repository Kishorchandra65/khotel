from django.shortcuts import render 
from .models import Room, ContactMessage
from collections import defaultdict
def index(request):
    rooms = Room.objects.all()[:3]
    return render(request, "index.html", {"rooms": rooms})

def about(request):
    return render(request, "about.html")

def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")

        if name and email and subject and message:
            try:
                contact_msg = ContactMessage(
                    name=name,
                    email=email,
                    subject=subject,
                    message=message
                )
                contact_msg.save()
                return render(request, "contact.html", {"success": "Your message has been sent successfully."})
            except Exception as e:
                # Optional: print(e) for debugging
                return render(request, "contact.html", {"error": "An error occurred while sending your message. Please try again."})
        else:
            return render(request, "contact.html", {"error": "All fields are required."})
        
    return render(request, "contact.html")


def gallery(request):
    return render(request, "gallery.html")


def continue_page(request):
    return render(request, "continue.html")

def rooms_view(request):
    rooms = Room.objects.filter(available=True)
    room_categories = defaultdict(list)
    for room in rooms:
        room_categories[room.category].append(room)  # Assuming 'category' field exists
    return render(request, 'rooms.html', {'room_categories': room_categories})

def rooms(request):
    all_rooms = Room.objects.filter(available=True)
    room_categories = defaultdict(list)
    for room in all_rooms:
        room_categories[room.category].append(room)
    return render(request, 'rooms.html', {'room_categories': dict(room_categories)})

def menu(request):
    return render(request, "menu.html")

from django.shortcuts import render, redirect

def payment_view(request):
    return redirect("thankyou")
   

def booking(request):
    room_type = request.GET.get('room', '')
    return render(request, 'booking.html', {'room_type': room_type})

def thankyou(request):
    data = request.GET  # all form data

    return render(request, "thankyou.html", {
        "name": data.get("full_name"),
        "room_type": data.get("room_type"),
        "location": data.get("location"),
        "check_in": data.get("check_in"),
        "check_out": data.get("check_out"),
    })

