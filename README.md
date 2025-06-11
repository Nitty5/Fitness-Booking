Fitness Booking API

This is a Django REST API for booking fitness classes like Yoga

---
Features

- View upcoming classes
- Book a slot (with validation)
- View your bookings by email

---
Tech Stack

- Python 3.10.12
- Django
- Django REST Framework
- Postgresql

---
 Setup Instructions

1. Clone the repo:
   ```bash
   git clone https://github.com/your-username/fitness-booking-api.git
   cd fitness-booking-api

2.Create activate Virtual Environment
python3 -m venv venv
source venv/bin/activate

3.Install Requirements
pip install -r requirements.txt

4.Run Migrations
python manage.py migrate

5.Run Development Server
python manage.py runserver


Sample Curl Requests

1.Get all Classes 
curl --location --request GET 'http://127.0.0.1:8000/api/classes/' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--data-raw '{
  "class_id": "1",
  "client_name": "Jhon Mark",
  "client_email": "Jhon@gmail.com"
}'

2.Book a class
curl --location 'http://127.0.0.1:8000/api/book/' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--data-raw '{
  "class_id": "1",
  "client_name": "Anna",
  "client_email": "Anna@gmail.com"
}'


3.View Bookings through Email
curl --location 'http://127.0.0.1:8000/api/bookings/?email=Jhon%40gmail.com' \
--data ''
