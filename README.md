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
    git clone https://github.com/ephrim-s/FishFarmMS.git
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


================================
-- ADMIN LOGIN CREDENTIALS--
    email: amind@example.com
    password: adminadmin
================================


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


-- API ENDPOINTS For Core APP--

https://ephrims5.pythonanywhere.com/api/auth/register/
https://ephrims5.pythonanywhere.com/api/auth/login/
https://ephrims5.pythonanywhere.com/api/auth/token/refresh/
https://ephrims5.pythonanywhere.com/api/auth/logout/

-- API ENDPOINTS For Farmer-DashBoard APP--
https://ephrims5.pythonanywhere.com/farmer-dashboard/ponds/
https://ephrims5.pythonanywhere.com/farmer-dashboard/add-pond/
https://ephrims5.pythonanywhere.com/farmer-dashboard/pond-rentals/
https://ephrims5.pythonanywhere.com/farmer-dashboard/fish-growth/
https://ephrims5.pythonanywhere.com/farmer-dashboard/fish-growth/<int:pk>/


--admin dashboard--
https://ephrims5.pythonanywhere.com/api/auth/admin-dashboard/

--farmer dashboard--
https://ephrims5.pythonanywhere.com/farmer-dahsboard/dashboard/




---Sample Data for Testing the API's---

- creating user -

{
    "email":"samuel@example.com",
    "first_name":"Samuel",
    "last_name":"Ephrim",
    "role":"outgrower",
    "password":"samuel123",
    "password2":"samuel123"

}

{
    "email":"sarah@example.com",
    "first_name":"Sarah",
    "last_name":"Bans",
    "role":"farmer",
    "password":"sarah123",
    "password2":"sarah123"

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

{
    "email":"john@example.com",
    "first_name":"John",
    "last_name":"Appiah",
    "role":"worker",
    "password":"john123",
    "password2":"john123"

}
{
    "email":"johnson@example.com",
    "first_name":"Johnson",
    "last_name":"Ments",
    "role":"retailer",
    "password":"johnson123",
    "password2":"johnson123"

}



---sample data for testing Refresh token--

{
    "refresh":"refresh_token"
}

---sample data for logout--

{
  "refresh_token": "your_refresh_token_here"
}


sample data for creating ponds

{
    "name": "pond5",
    "length": 10,
    "width": 10,
    "heigth": 3.5,
    "location": "agona site a",
    "status": "available"
}



sample data for renting pond
{
    "pond":"",
    "start_date":"2025-04-02",
    "end_date":"2025-10-02",
}

sample data for fish growth record
{    
    "rental":"5",
    "size_in_cm":"10"
}

sample data for creating expense
{
    "category": "feed",
    "amount": 5000.75,
    "description": "Purchased fish feed for the pond"
}

{
    "category": "medication",
    "amount": 1200.50,
    "description": "Bought antibiotics for fish treatment"
}

{
    "category": "feed",
    "amount": 1200.50,
    "description": "Bought antibiotics for fish treatment"
}