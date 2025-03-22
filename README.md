FishFarmMS

FishFarmMS is a Fish Farm Management System built with Django for backend development. 
It is designed to manage farm operations, including external farmer contracts, stock management, 
worker tasks, and order processing.

Features Implemented So Far

1. User Roles & Authentication
    Admin Dashboard: Admins can manage all users, workers, and inventory.
    Workers Dashboard: Workers can log tasks and manage assigned duties.
    External Farmers, Wholesalers, Retailers, and Consumers: Different roles with specific access.
    Email-Based Login: Instead of usernames, users log in with the user email.
    Custom Fields: Users have custom fields like phone number, address, destination address, and geo-location.


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

2. Stock & Inventory Management
    Tracking of fingerlings, feed, and medication.
    Managing stock distribution and mortality tracking.
    Alerts for stock replenishment.

3. Farm Worker Management
    Attendance tracking.
    Task logging and performance tracking.
    Salary and compensation management.

4. Wholesalers & Retailers Features
    Signup and authentication.
    Order placement and order tracking.
    Payment confirmation and evidence submission.

5. Delivery Service Features
    Geo-Location Sharing: Allows farm to send its location and access customers' locations.
    Manual address input for customers.

Frontend Development: React UI for FishFarmMS.

Deploy to a server.

Enhance APIs for user roles and stock management.