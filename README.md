Marc Lab CRM:
A CRM-based Django web application designed for laboratory management.
The system provides two panels: Admin and User for efficient communication between labs and customers.

Features:-

User Panel:

User login & dashboard
View latest medicines uploaded by the admin
Submit feedback (Good / Complaint) about medicines
Easy & responsive interface

Admin Panel:

Admin login & dashboard
Upload new medicines with details (name, company, description)
Manage uploaded medicines
View user feedback and complaints
Handle responses

Tech Stack:-

Backend: Django (Python):

Frontend: HTML, CSS, JavaScript, Bootstrap
Database: SQLite (default, can be switched to MySQL/PostgreSQL)
Version Control: Git & GitHub

Installation & Setup:-

1. Clone the Repository:-
   git clone https://github.com/alamaftab9426/marc-lab-crm.git
   cd marc-lab-crm
2. Create Virtual Environment:-
    python -m venv venv
    venv\Scripts\activate   # On Windows
    source venv/bin/activate   # On Linux/Mac
3. Install Dependencies:-
    pip install -r requirements.txt
4. Apply Migrations:-
    python manage.py makemigrations
    python manage.py migrate
5. Create Superuser (Admin):-
    python manage.py createsuperuser
   
7. Run the Server:-
   python manage.py runserver

     
   
   
