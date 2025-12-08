🏨 Hotel Booking Website — Django

A fully responsive Hotel Booking Web Application built using Django, HTML, CSS, and JavaScript.
Users can explore hotel rooms, view details, contact the hotel, and book rooms.
Admins can easily manage rooms, bookings, and hotel information through the Django Admin Panel.

🚀 Features

✔ Modern and responsive UI
✔ Add rooms from Django Admin Panel
✔ View room details and availability
✔ Room booking system (date & guest selection)
✔ Contact form with message saving in database
✔ Image upload support for rooms
✔ Secure admin panel authentication
✔ Deployed live on Render

🛠️ Tech Stack
Technology	Purpose
Django	Backend & ORM
HTML5	Structure
CSS3	Styling & animations
JavaScript	Interactivity
SQLite	Development database
Render	Deployment
📂 Project Structure
hotel/
 ├─ hotel/               # Project settings & URLs
 ├─ hotelapp/            # Main application
 │   ├─ migrations/      # Database migrations
 │   ├─ static/          # CSS, JS, images
 │   ├─ templates/       # HTML Templates
 │   ├─ models.py        # Database models
 │   ├─ views.py         # Business logic
 │   ├─ urls.py          # App routing
 ├─ media/               # Uploaded room images
 ├─ manage.py
 └─ requirements.txt

💻 Installation & Setup
1️⃣ Clone the repository
git clone https://github.com/YourUsername/YourRepo.git
cd YourRepo

2️⃣ Create virtual environment
python -m venv env
env\Scripts\activate  # Windows

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Run migrations
python manage.py makemigrations
python manage.py migrate

5️⃣ Create superuser (admin)
python manage.py createsuperuser

6️⃣ Run development server
python manage.py runserver


Then open in browser:

http://127.0.0.1:8000/

🔐 Admin Panel

Login URL:

/admin/


From here you can:

Add rooms

Upload room images

Manage bookings

Read contact messages

🌐 Live Demo

🔗 Hosted on Render
(Replace this with your link)

https://yourwebsite.onrender.com

📸 Screenshots (Optional)
<img width="1891" height="916" alt="Screenshot 2025-12-03 192645" src="https://github.com/user-attachments/assets/23c7773e-6a43-4fbb-a9fd-b0b83e5a889d" />
<img width="1894" height="922" alt="Screenshot 2025-12-03 192628" src="https://github.com/user-attachments/assets/06c36c0e-c252-4f49-92be-ce2488d14579" />



🤝 Contributing

Want to improve this project? Fork the repo, create a new branch, and submit a pull request.

🌟 Show Your Support

If you like this project, don’t forget to ⭐ the repository!

👤 Developer

Kishor Chandra
