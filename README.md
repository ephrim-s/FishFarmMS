FishFarmMS

Project Overview

FishFarmMS is a comprehensive Fish Farm Management System designed to streamline operations, 
enhance collaboration, and improve efficiency in fish farming businesses. The system 
integrates functionalities for external farmers, outgrowers, wholesalers, retailers, 
farm workers, and consumers, ensuring smooth management of fish stock, inventory, 
deliveries, and financial records.

Inspiration
Developed by Samuel Ephrim a Student at Alx, and a fish farmer passionate about leveraging 
IT technology to enhance collaboration between fish farmers, fishmongers, wholesalers, 
retailers, and consumers. Recognizing the challenges in fish farming operations, 
this system is built to bridge the gap between stakeholders and optimize farm management processes.


Features Implemented So Far

1. User Roles & Authentication
    Admin Dashboard: Admins can manage all users, workers, and inventory.
    Workers Dashboard: Workers can log tasks and manage assigned duties.
    External Farmers, Outgrowers, Wholesalers, Retailers, and Consumers: Different roles with specific access.
    Email-Based Login: Instead of usernames, users log in with the user email.
    Custom Fields: Users have custom fields like phone number, address, destination address, and geo-location.

2. Farm Operations & Management
    Pond Rental & Contract Agreements for external farmers.
    Fish Growth Tracking with images/videos.
    Expense Tracking for better financial management.
    Commission Management for external farmers.
    Insurance Package feature for fish farmers.


Setup Instructions

1. Clone the Repository
    git clone https://github.com/yourusername/FishFarmMS.git
    cd FishFarmMS

2. Create a Virtual Environment
    python -m venv venv
    source venv/bin/activate  # On Windows use: venv\Scripts\activate

3. Install Dependencies
    pip install -r requirements.txt

4. Apply Migrations
    python manage.py migrate

5. Create a Superuser
    python manage.py createsuperuser

6. Run the Server
    python manage.py runserver



Next Steps

1. Stock & Inventory Management
    Tracking of fingerlings, feed, and medication.
    Managing stock distribution and mortality tracking.
    Alerts for stock replenishment.

2. Farm Worker Management
    Attendance tracking.
    Task logging and performance tracking.
    Salary and compensation management.


3. Wholesalers & Retailers Features
    Signup and authentication.
    Order placement and order tracking.
    Payment confirmation and evidence submission.

4. Delivery Service Features
    Geo-Location Sharing: Allows farm to send its location and access customers' locations.
    Manual address input for customers.


Frontend Development: React UI for FishFarmMS.

Deploy to a server.

Enhance APIs for user roles and stock management.




Sample Data for Testing the API's

- creating user 
    * endpoint: localhost:8000/api/auth/register

{
    "email":"samuel@example.com",
    "first_name":"Samuel",
    "last_name":"Ephrim",
    "role":"admin",
    "password":"samuel123",
    "password2":"samuel123"

}

{
    "email":"sarah@example.com",
    "first_name":"Sarah",
    "last_name":"Bans",
    "role":"farmer",
    "password":"sarah123",
    "password2":"sarahl123"

}

{
    "email":"grace@example.com",
    "first_name":"Grace",
    "last_name":"Mensah",
    "role":"wholesaler",
    "password":"grace123",
    "password2":"grace123"

}

{
    "email":"dominic@example.com",
    "first_name":"Dominic",
    "last_name":"Jackson",
    "role":"consumer",
    "password":"dominic123",
    "password2":"dominicl123"

}