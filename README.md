# CIS-Assesment

## Objective
  Develop a User CRUD System with Role-Based Access Control (Admin, Manager, User)
  and JWT Authentication. The system must allow Managers to assign tasks with
  deadlines, trigger notifications for missed deadlines, automatically deactivate users
  after repeated failures, and include a mechanism to reactivate users.

 ### Problem Statement   

1. **User Management:**  
   - CRUD operations for users with roles: **Admin**, **Manager**, and **User**.  
   - JWT authentication (register, login, logout).  

2. **Role-Based Access:**  
   - **Admin:** Full access to all endpoints.  
   - **Manager:** Assign tasks to users, view tasks, and receive notifications.  
   - **User:** View assigned tasks, update task status.  

3. **Task Management:**  
   - Managers can assign tasks to users with deadlines.  
   - Notify managers if a user misses a deadline.  
   - Automatically deactivate users who miss 5 tasks in a week.  
   - Managers can reactivate deactivated users.

## Approach
 #### Setup manually 
  1.  Git clone - http
  2.  pip install -r requirements.txt
  3.  python manage.py makemigrations
  4.  python manage.py migrate
  5.  python manage.py runserver
#### Via docker 
  - docker-compose up --build
### Workflow
  ![cis ](https://github.com/user-attachments/assets/5d4eefbb-8a78-421a-9a99-d7d1bf38c49e)

### postman collection : 
	 https://sandeep-7513527.postman.co/workspace/sandeep's-Workspace~7af79d6f-3300-4c2d-8ba8-c1bf645d06e6/collection/43750356-2e39d089-81fc-46c1-9f21-723914f312f0?action=share&creator=43750356

