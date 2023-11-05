===================
** Paths To Test **
===================

User Management:
===============
Create User -> (POST) http://127.0.0.1:8000/auth/users/
Login       -> (POST) http://127.0.0.1:8000/api-token-auth/

Payload:
{
	"username": "<user>",
	"password": "<password>"
}


Menu Model:
==========
Get all menu items -> (GET) http://127.0.0.1:8000/restaurant/menu
Add a menu item    -> (POST) http://127.0.0.1:8000/restaurant/menu
Update a menu item -> (PUT) http://127.0.0.1:8000/restaurant/menu/<id>
Update a menu item -> (DELETE) http://127.0.0.1:8000/restaurant/menu/<id>


Booking Model:
=============
Get all bookings -> (GET) http://127.0.0.1:8000/restaurant/booking/tables/
Add a booking    -> (POST) http://127.0.0.1:8000/restaurant/booking/tables/
Update a booking -> (PUT) http://127.0.0.1:8000/restaurant/booking/tables/<id>
Delete a booking -> (DELETE) http://127.0.0.1:8000/restaurant/booking/tables/<id>


NOTE: 
====
All endpoints (except create user and login) require an authenticated user.