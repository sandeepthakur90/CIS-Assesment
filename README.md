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
    - 
[CIS API-Endpoints Sandeep Thakur.postman_collection.json](https://github.com/user-attachments/files/19603437/CIS.API-Endpoints.Sandeep.Thakur.postman_collection.json){
	"info": {
		"_postman_id": "2e39d089-81fc-46c1-9f21-723914f312f0",
		"name": "CIS API-Endpoints Sandeep Thakur",
		"schema": "https://schema.getpostman.com/json/collection/v2.1.0/collection.json",
		"_exporter_id": "43750356",
		"_collection_link": "https://sandeep-7513527.postman.co/workspace/sandeep's-Workspace~7af79d6f-3300-4c2d-8ba8-c1bf645d06e6/collection/43750356-2e39d089-81fc-46c1-9f21-723914f312f0?action=share&source=collection_link&creator=43750356"
	},
	"item": [
		{
			"name": "User",
			"item": [
				{
					"name": "SIgnup",
					"request": {
						"auth": {
							"type": "noauth"
						},
						"method": "POST",
						"header": [],
						"body": {
							"mode": "raw",
							"raw": "{\n  \"email\": \"rohit@gmail.com\",\n  \"password\": \"Password@123\",\n  \"password2\": \"Password@123\",\n  \"first_name\": \"rohit\",\n  \"last_name\": \"singh\",\n  \"role\": \"ADMIN\"\n}",
							"options": {
								"raw": {
									"language": "json"
								}
							}
						},
						"url": {
							"raw": "http://127.0.0.1:8000/api/users/signup/",
							"protocol": "http",
							"host": [
								"127",
								"0",
								"0",
								"1"
							],
							"port": "8000",
							"path": [
								"api",
								"users",
								"signup",
								""
							]
						}
					},
					"response": [
						{
							"name": "successfull signup",
							"originalRequest": {
								"method": "POST",
								"header": [],
								"body": {
									"mode": "raw",
									"raw": "{\n  \"email\": \"rohit@gmail.com\",\n  \"password\": \"Password@123\",\n  \"password2\": \"Password@123\",\n  \"first_name\": \"rohit\",\n  \"last_name\": \"singh\",\n  \"role\": \"ADMIN\"\n}",
									"options": {
										"raw": {
											"language": "json"
										}
									}
								},
								"url": {
									"raw": "http://127.0.0.1:8000/api/users/signup/",
									"protocol": "http",
									"host": [
										"127",
										"0",
										"0",
										"1"
									],
									"port": "8000",
									"path": [
										"api",
										"users",
										"signup",
										""
									]
								}
							},
							"status": "Created",
							"code": 201,
							"_postman_previewlanguage": "json",
							"header": [
								{
									"key": "Date",
									"value": "Fri, 04 Apr 2025 07:47:16 GMT"
								},
								{
									"key": "Server",
									"value": "WSGIServer/0.2 CPython/3.8.10"
								},
								{
									"key": "Content-Type",
									"value": "application/json"
								},
								{
									"key": "Vary",
									"value": "Accept"
								},
								{
									"key": "Allow",
									"value": "POST, OPTIONS"
								},
								{
									"key": "X-Frame-Options",
									"value": "DENY"
								},
								{
									"key": "Content-Length",
									"value": "665"
								},
								{
									"key": "X-Content-Type-Options",
									"value": "nosniff"
								},
								{
									"key": "Referrer-Policy",
									"value": "same-origin"
								},
								{
									"key": "Cross-Origin-Opener-Policy",
									"value": "same-origin"
								}
							],
							"cookie": [],
							"body": "{\n    \"refresh\": \"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTc0MzgzOTIzNiwiaWF0IjoxNzQzNzUyODM2LCJqdGkiOiI1ZDAzODNlYTk5ODI0NWViOGQ3MTA5NWI1NDE2Y2YwZCIsInVzZXJfaWQiOjd9.Avs9wgvX3Rp4Y_-QsUUMBMZefGfSDg7TMBmqe1rDPYY\",\n    \"access\": \"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzQzNzU2NDM2LCJpYXQiOjE3NDM3NTI4MzYsImp0aSI6IjkwOTA4ZWFiZTc0MjRhYjFiYzAwY2JlYTk0ODExN2E0IiwidXNlcl9pZCI6N30.W8F-EY53w07B1fIy3hMACxGtJvBwFWO0nmk7aMJxl2g\",\n    \"user\": {\n        \"id\": 7,\n        \"email\": \"rohit@gmail.com\",\n        \"first_name\": \"rohit\",\n        \"last_name\": \"singh\",\n        \"role\": \"ADMIN\",\n        \"is_active\": true,\n        \"date_joined\": \"2025-04-04T07:47:16.465605Z\",\n        \"failed_tasks_count\": 0\n    }\n}"
						}
					]
				},
				{
					"name": "login",
					"request": {
						"auth": {
							"type": "noauth"
						},
						"method": "POST",
						"header": [],
						"body": {
							"mode": "raw",
							"raw": "{\n  \"email\": \"rohit@gmail.com\",\n  \"password\": \"Password@123\"\n}",
							"options": {
								"raw": {
									"language": "json"
								}
							}
						},
						"url": {
							"raw": "http://127.0.0.1:8000/api/users/login/",
							"protocol": "http",
							"host": [
								"127",
								"0",
								"0",
								"1"
							],
							"port": "8000",
							"path": [
								"api",
								"users",
								"login",
								""
							]
						}
					},
					"response": [
						{
							"name": "successfull login",
							"originalRequest": {
								"method": "POST",
								"header": [],
								"body": {
									"mode": "raw",
									"raw": "{\n  \"email\": \"rohit@gmail.com\",\n  \"password\": \"Password@123\"\n}",
									"options": {
										"raw": {
											"language": "json"
										}
									}
								},
								"url": {
									"raw": "http://127.0.0.1:8000/api/users/login/",
									"protocol": "http",
									"host": [
										"127",
										"0",
										"0",
										"1"
									],
									"port": "8000",
									"path": [
										"api",
										"users",
										"login",
										""
									]
								}
							},
							"status": "OK",
							"code": 200,
							"_postman_previewlanguage": "json",
							"header": [
								{
									"key": "Date",
									"value": "Fri, 04 Apr 2025 07:48:38 GMT"
								},
								{
									"key": "Server",
									"value": "WSGIServer/0.2 CPython/3.8.10"
								},
								{
									"key": "Content-Type",
									"value": "application/json"
								},
								{
									"key": "Vary",
									"value": "Accept"
								},
								{
									"key": "Allow",
									"value": "POST, OPTIONS"
								},
								{
									"key": "X-Frame-Options",
									"value": "DENY"
								},
								{
									"key": "Content-Length",
									"value": "665"
								},
								{
									"key": "X-Content-Type-Options",
									"value": "nosniff"
								},
								{
									"key": "Referrer-Policy",
									"value": "same-origin"
								},
								{
									"key": "Cross-Origin-Opener-Policy",
									"value": "same-origin"
								}
							],
							"cookie": [],
							"body": "{\n    \"refresh\": \"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTc0MzgzOTMxOCwiaWF0IjoxNzQzNzUyOTE4LCJqdGkiOiJhOGYzY2Q5NWFhMTA0ZDNlOWE0MzZmYmNjY2M3ZmQ0NSIsInVzZXJfaWQiOjd9.Algdcw4CIFMOzWOw6FRQw9OIP2Pmiu0-vVhZcCzZXog\",\n    \"access\": \"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzQzNzU2NTE4LCJpYXQiOjE3NDM3NTI5MTgsImp0aSI6IjVhZGZjNzU1NGRjOTQ4MTliYWM0YmM5ZGU4OWQxODc1IiwidXNlcl9pZCI6N30.YgL_Rc4dGUYzURBL6yvNuxDRPgTBKU_HqOXCF6VZn8M\",\n    \"user\": {\n        \"id\": 7,\n        \"email\": \"rohit@gmail.com\",\n        \"first_name\": \"rohit\",\n        \"last_name\": \"singh\",\n        \"role\": \"ADMIN\",\n        \"is_active\": true,\n        \"date_joined\": \"2025-04-04T07:47:16.465605Z\",\n        \"failed_tasks_count\": 0\n    }\n}"
						}
					]
				},
				{
					"name": "users-list",
					"request": {
						"auth": {
							"type": "bearer",
							"bearer": [
								{
									"key": "token",
									"value": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzQzNzYyOTk3LCJpYXQiOjE3NDM3NTkzOTcsImp0aSI6Ijg1MDM3MjRiMzI3NjRhN2M4MTE0ZDIxMzQxZDY4YTUyIiwidXNlcl9pZCI6N30.J1Su5HNR6vrteOkkL0ns4OHsAXu_WVw3cFem0EA0lII",
									"type": "string"
								}
							]
						},
						"method": "GET",
						"header": [],
						"url": {
							"raw": "http://127.0.0.1:8000/api/users/user_list/",
							"protocol": "http",
							"host": [
								"127",
								"0",
								"0",
								"1"
							],
							"port": "8000",
							"path": [
								"api",
								"users",
								"user_list",
								""
							]
						}
					},
					"response": [
						{
							"name": "New Request",
							"originalRequest": {
								"method": "GET",
								"header": [],
								"url": {
									"raw": "http://127.0.0.1:8000/api/users/user_list/",
									"protocol": "http",
									"host": [
										"127",
										"0",
										"0",
										"1"
									],
									"port": "8000",
									"path": [
										"api",
										"users",
										"user_list",
										""
									]
								}
							},
							"status": "OK",
							"code": 200,
							"_postman_previewlanguage": "json",
							"header": [
								{
									"key": "Date",
									"value": "Fri, 04 Apr 2025 10:25:38 GMT"
								},
								{
									"key": "Server",
									"value": "WSGIServer/0.2 CPython/3.8.10"
								},
								{
									"key": "Content-Type",
									"value": "application/json"
								},
								{
									"key": "Vary",
									"value": "Accept"
								},
								{
									"key": "Allow",
									"value": "GET, POST, HEAD, OPTIONS"
								},
								{
									"key": "X-Frame-Options",
									"value": "DENY"
								},
								{
									"key": "Content-Length",
									"value": "1210"
								},
								{
									"key": "X-Content-Type-Options",
									"value": "nosniff"
								},
								{
									"key": "Referrer-Policy",
									"value": "same-origin"
								},
								{
									"key": "Cross-Origin-Opener-Policy",
									"value": "same-origin"
								}
							],
							"cookie": [],
							"body": "[\n    {\n        \"id\": 1,\n        \"email\": \"user@example.com\",\n        \"first_name\": \"John\",\n        \"last_name\": \"Doe\",\n        \"role\": \"ADMIN\",\n        \"is_active\": true,\n        \"date_joined\": \"2025-04-04T07:00:27.819974Z\",\n        \"failed_tasks_count\": 0\n    },\n    {\n        \"id\": 2,\n        \"email\": \"test@gmail.com\",\n        \"first_name\": \"\",\n        \"last_name\": \"\",\n        \"role\": \"ADMIN\",\n        \"is_active\": true,\n        \"date_joined\": \"2025-04-04T07:11:02.443670Z\",\n        \"failed_tasks_count\": 0\n    },\n    {\n        \"id\": 3,\n        \"email\": \"kumarsatyam72770@gmail.com\",\n        \"first_name\": \"\",\n        \"last_name\": \"\",\n        \"role\": \"ADMIN\",\n        \"is_active\": true,\n        \"date_joined\": \"2025-04-04T07:13:01.625635Z\",\n        \"failed_tasks_count\": 0\n    },\n    {\n        \"id\": 4,\n        \"email\": \"kumarsatyamm72770@gmail.com\",\n        \"first_name\": \"\",\n        \"last_name\": \"\",\n        \"role\": \"ADMIN\",\n        \"is_active\": true,\n        \"date_joined\": \"2025-04-04T07:22:18.971687Z\",\n        \"failed_tasks_count\": 0\n    },\n    {\n        \"id\": 5,\n        \"email\": \"thakursandeep31100@gmail.com\",\n        \"first_name\": \"\",\n        \"last_name\": \"\",\n        \"role\": \"MANAGER\",\n        \"is_active\": true,\n        \"date_joined\": \"2025-04-04T07:23:19.159324Z\",\n        \"failed_tasks_count\": 0\n    },\n    {\n        \"id\": 6,\n        \"email\": \"kapil@gmail.com\",\n        \"first_name\": \"\",\n        \"last_name\": \"\",\n        \"role\": \"USER\",\n        \"is_active\": true,\n        \"date_joined\": \"2025-04-04T07:25:56.712619Z\",\n        \"failed_tasks_count\": 0\n    },\n    {\n        \"id\": 7,\n        \"email\": \"rohit@gmail.com\",\n        \"first_name\": \"rohit\",\n        \"last_name\": \"singh\",\n        \"role\": \"ADMIN\",\n        \"is_active\": true,\n        \"date_joined\": \"2025-04-04T07:47:16.465605Z\",\n        \"failed_tasks_count\": 0\n    }\n]"
						}
					]
				},
				{
					"name": "user-details",
					"request": {
						"auth": {
							"type": "bearer",
							"bearer": [
								{
									"key": "token",
									"value": "{{access}}",
									"type": "string"
								}
							]
						},
						"method": "GET",
						"header": [],
						"url": {
							"raw": "http://127.0.0.1:8000/api/users/1/",
							"protocol": "http",
							"host": [
								"127",
								"0",
								"0",
								"1"
							],
							"port": "8000",
							"path": [
								"api",
								"users",
								"1",
								""
							]
						}
					},
					"response": [
						{
							"name": "user-details",
							"originalRequest": {
								"method": "GET",
								"header": [],
								"url": {
									"raw": "http://127.0.0.1:8000/api/users/1/",
									"protocol": "http",
									"host": [
										"127",
										"0",
										"0",
										"1"
									],
									"port": "8000",
									"path": [
										"api",
										"users",
										"1",
										""
									]
								}
							},
							"status": "OK",
							"code": 200,
							"_postman_previewlanguage": "json",
							"header": [
								{
									"key": "Date",
									"value": "Fri, 04 Apr 2025 10:35:38 GMT"
								},
								{
									"key": "Server",
									"value": "WSGIServer/0.2 CPython/3.8.10"
								},
								{
									"key": "Content-Type",
									"value": "application/json"
								},
								{
									"key": "Vary",
									"value": "Accept"
								},
								{
									"key": "Allow",
									"value": "GET, PUT, PATCH, DELETE, HEAD, OPTIONS"
								},
								{
									"key": "X-Frame-Options",
									"value": "DENY"
								},
								{
									"key": "Content-Length",
									"value": "172"
								},
								{
									"key": "X-Content-Type-Options",
									"value": "nosniff"
								},
								{
									"key": "Referrer-Policy",
									"value": "same-origin"
								},
								{
									"key": "Cross-Origin-Opener-Policy",
									"value": "same-origin"
								}
							],
							"cookie": [],
							"body": "{\n    \"id\": 1,\n    \"email\": \"user@example.com\",\n    \"first_name\": \"John\",\n    \"last_name\": \"Doe\",\n    \"role\": \"ADMIN\",\n    \"is_active\": true,\n    \"date_joined\": \"2025-04-04T07:00:27.819974Z\",\n    \"failed_tasks_count\": 0\n}"
						}
					]
				},
				{
					"name": "user-activate",
					"request": {
						"auth": {
							"type": "bearer",
							"bearer": [
								{
									"key": "token",
									"value": "{{access}}",
									"type": "string"
								}
							]
						},
						"method": "POST",
						"header": [],
						"url": {
							"raw": "http://127.0.0.1:8000/api/users/1/reactivate/",
							"protocol": "http",
							"host": [
								"127",
								"0",
								"0",
								"1"
							],
							"port": "8000",
							"path": [
								"api",
								"users",
								"1",
								"reactivate",
								""
							]
						}
					},
					"response": [
						{
							"name": "user-activate",
							"originalRequest": {
								"method": "POST",
								"header": [],
								"url": {
									"raw": "http://127.0.0.1:8000/api/users/1/reactivate/",
									"protocol": "http",
									"host": [
										"127",
										"0",
										"0",
										"1"
									],
									"port": "8000",
									"path": [
										"api",
										"users",
										"1",
										"reactivate",
										""
									]
								}
							},
							"status": "OK",
							"code": 200,
							"_postman_previewlanguage": "json",
							"header": [
								{
									"key": "Date",
									"value": "Fri, 04 Apr 2025 10:39:22 GMT"
								},
								{
									"key": "Server",
									"value": "WSGIServer/0.2 CPython/3.8.10"
								},
								{
									"key": "Content-Type",
									"value": "application/json"
								},
								{
									"key": "Vary",
									"value": "Accept"
								},
								{
									"key": "Allow",
									"value": "POST, OPTIONS"
								},
								{
									"key": "X-Frame-Options",
									"value": "DENY"
								},
								{
									"key": "Content-Length",
									"value": "52"
								},
								{
									"key": "X-Content-Type-Options",
									"value": "nosniff"
								},
								{
									"key": "Referrer-Policy",
									"value": "same-origin"
								},
								{
									"key": "Cross-Origin-Opener-Policy",
									"value": "same-origin"
								}
							],
							"cookie": [],
							"body": "{\n    \"detail\": \"User has been reactivated successfully.\"\n}"
						}
					]
				},
				{
					"name": "user-deactivate",
					"request": {
						"auth": {
							"type": "bearer",
							"bearer": [
								{
									"key": "token",
									"value": "{{access}}",
									"type": "string"
								}
							]
						},
						"method": "POST",
						"header": [],
						"url": {
							"raw": "http://127.0.0.1:8000/api/users/1/deactivate/",
							"protocol": "http",
							"host": [
								"127",
								"0",
								"0",
								"1"
							],
							"port": "8000",
							"path": [
								"api",
								"users",
								"1",
								"deactivate",
								""
							]
						}
					},
					"response": [
						{
							"name": "user-deactivate",
							"originalRequest": {
								"method": "POST",
								"header": [],
								"url": {
									"raw": "http://127.0.0.1:8000/api/users/1/deactivate/",
									"protocol": "http",
									"host": [
										"127",
										"0",
										"0",
										"1"
									],
									"port": "8000",
									"path": [
										"api",
										"users",
										"1",
										"deactivate",
										""
									]
								}
							},
							"status": "OK",
							"code": 200,
							"_postman_previewlanguage": "json",
							"header": [
								{
									"key": "Date",
									"value": "Fri, 04 Apr 2025 10:38:38 GMT"
								},
								{
									"key": "Server",
									"value": "WSGIServer/0.2 CPython/3.8.10"
								},
								{
									"key": "Content-Type",
									"value": "application/json"
								},
								{
									"key": "Vary",
									"value": "Accept"
								},
								{
									"key": "Allow",
									"value": "POST, OPTIONS"
								},
								{
									"key": "X-Frame-Options",
									"value": "DENY"
								},
								{
									"key": "Content-Length",
									"value": "52"
								},
								{
									"key": "X-Content-Type-Options",
									"value": "nosniff"
								},
								{
									"key": "Referrer-Policy",
									"value": "same-origin"
								},
								{
									"key": "Cross-Origin-Opener-Policy",
									"value": "same-origin"
								}
							],
							"cookie": [],
							"body": "{\n    \"detail\": \"User has been deactivated successfully.\"\n}"
						}
					]
				}
			]
		},
		{
			"name": "Tasks",
			"item": [
				{
					"name": "task-list",
					"protocolProfileBehavior": {
						"disableBodyPruning": true
					},
					"request": {
						"auth": {
							"type": "bearer",
							"bearer": [
								{
									"key": "token",
									"value": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzQzNzY2NDYzLCJpYXQiOjE3NDM3NjI4NjMsImp0aSI6IjExMDgyM2MxYzZlNjRlYzhiZmYwZWM0MTIzOWI5YjJmIiwidXNlcl9pZCI6N30.dl0Ish88-B9OIWDTcjpCWLY34ZfhPoifIBtKcyl0Nf8",
									"type": "string"
								}
							]
						},
						"method": "GET",
						"header": [],
						"body": {
							"mode": "raw",
							"raw": "{\n  \"title\": \"Update Documentation\",\n  \"description\": \"Update API docs for v2 endpoints\",\n  \"assigned_to\": 5,\n  \"deadline\": \"2025-04-10T23:59:00Z\"\n}",
							"options": {
								"raw": {
									"language": "json"
								}
							}
						},
						"url": {
							"raw": "http://127.0.0.1:8000/api/tasks/task_list/",
							"protocol": "http",
							"host": [
								"127",
								"0",
								"0",
								"1"
							],
							"port": "8000",
							"path": [
								"api",
								"tasks",
								"task_list",
								""
							]
						}
					},
					"response": [
						{
							"name": "task-list",
							"originalRequest": {
								"method": "GET",
								"header": [],
								"body": {
									"mode": "raw",
									"raw": "{\n  \"title\": \"Update Documentation\",\n  \"description\": \"Update API docs for v2 endpoints\",\n  \"assigned_to\": 5,\n  \"deadline\": \"2025-04-10T23:59:00Z\"\n}",
									"options": {
										"raw": {
											"language": "json"
										}
									}
								},
								"url": {
									"raw": "http://127.0.0.1:8000/api/tasks/task_list/",
									"protocol": "http",
									"host": [
										"127",
										"0",
										"0",
										"1"
									],
									"port": "8000",
									"path": [
										"api",
										"tasks",
										"task_list",
										""
									]
								}
							},
							"status": "OK",
							"code": 200,
							"_postman_previewlanguage": "json",
							"header": [
								{
									"key": "Date",
									"value": "Fri, 04 Apr 2025 09:36:53 GMT"
								},
								{
									"key": "Server",
									"value": "WSGIServer/0.2 CPython/3.8.10"
								},
								{
									"key": "Content-Type",
									"value": "application/json"
								},
								{
									"key": "Vary",
									"value": "Accept"
								},
								{
									"key": "Allow",
									"value": "GET, POST, HEAD, OPTIONS"
								},
								{
									"key": "X-Frame-Options",
									"value": "DENY"
								},
								{
									"key": "Content-Length",
									"value": "660"
								},
								{
									"key": "X-Content-Type-Options",
									"value": "nosniff"
								},
								{
									"key": "Referrer-Policy",
									"value": "same-origin"
								},
								{
									"key": "Cross-Origin-Opener-Policy",
									"value": "same-origin"
								}
							],
							"cookie": [],
							"body": "[\n    {\n        \"id\": 1,\n        \"title\": \"Update Documentation\",\n        \"description\": \"Update API docs for v2 endpoints\",\n        \"assigned_to\": 5,\n        \"assigned_by\": 7,\n        \"status\": \"PENDING\",\n        \"deadline\": \"2025-04-10T23:59:00Z\",\n        \"created_at\": \"2025-04-04T08:02:07.754090Z\",\n        \"updated_at\": \"2025-04-04T08:02:07.754111Z\",\n        \"assigned_to_details\": {\n            \"id\": 5,\n            \"email\": \"thakursandeep31100@gmail.com\",\n            \"first_name\": \"\",\n            \"last_name\": \"\",\n            \"role\": \"MANAGER\",\n            \"is_active\": true,\n            \"date_joined\": \"2025-04-04T07:23:19.159324Z\",\n            \"failed_tasks_count\": 0\n        },\n        \"assigned_by_details\": {\n            \"id\": 7,\n            \"email\": \"rohit@gmail.com\",\n            \"first_name\": \"rohit\",\n            \"last_name\": \"singh\",\n            \"role\": \"ADMIN\",\n            \"is_active\": true,\n            \"date_joined\": \"2025-04-04T07:47:16.465605Z\",\n            \"failed_tasks_count\": 0\n        }\n    }\n]"
						}
					]
				},
				{
					"name": "task-create",
					"request": {
						"auth": {
							"type": "bearer",
							"bearer": [
								{
									"key": "token",
									"value": "{{authToken}}",
									"type": "string"
								}
							]
						},
						"method": "POST",
						"header": [],
						"body": {
							"mode": "raw",
							"raw": "{\n  \"title\": \"Fix Login Bug\",\n  \"description\": \"Resolve the issue with user login on mobile devices\",\n  \"assigned_to\": 3,\n  \"assigned_by\": 1,\n  \"status\": \"IN_PROGRESS\",\n  \"deadline\": \"2025-04-08T18:00:00Z\"\n}",
							"options": {
								"raw": {
									"language": "json"
								}
							}
						},
						"url": {
							"raw": "http://127.0.0.1:8000/api/tasks/task_list/",
							"protocol": "http",
							"host": [
								"127",
								"0",
								"0",
								"1"
							],
							"port": "8000",
							"path": [
								"api",
								"tasks",
								"task_list",
								""
							]
						}
					},
					"response": [
						{
							"name": "task-create",
							"originalRequest": {
								"method": "POST",
								"header": [],
								"body": {
									"mode": "raw",
									"raw": "{\n  \"title\": \"Fix Login Bug\",\n  \"description\": \"Resolve the issue with user login on mobile devices\",\n  \"assigned_to\": 3,\n  \"assigned_by\": 1,\n  \"status\": \"IN_PROGRESS\",\n  \"deadline\": \"2025-04-08T18:00:00Z\"\n}",
									"options": {
										"raw": {
											"language": "json"
										}
									}
								},
								"url": {
									"raw": "http://127.0.0.1:8000/api/tasks/task_list/",
									"protocol": "http",
									"host": [
										"127",
										"0",
										"0",
										"1"
									],
									"port": "8000",
									"path": [
										"api",
										"tasks",
										"task_list",
										""
									]
								}
							},
							"status": "Created",
							"code": 201,
							"_postman_previewlanguage": "json",
							"header": [
								{
									"key": "Date",
									"value": "Fri, 04 Apr 2025 10:46:41 GMT"
								},
								{
									"key": "Server",
									"value": "WSGIServer/0.2 CPython/3.8.10"
								},
								{
									"key": "Content-Type",
									"value": "application/json"
								},
								{
									"key": "Vary",
									"value": "Accept"
								},
								{
									"key": "Allow",
									"value": "GET, POST, HEAD, OPTIONS"
								},
								{
									"key": "X-Frame-Options",
									"value": "DENY"
								},
								{
									"key": "Content-Length",
									"value": "670"
								},
								{
									"key": "X-Content-Type-Options",
									"value": "nosniff"
								},
								{
									"key": "Referrer-Policy",
									"value": "same-origin"
								},
								{
									"key": "Cross-Origin-Opener-Policy",
									"value": "same-origin"
								}
							],
							"cookie": [],
							"body": "{\n    \"id\": 2,\n    \"title\": \"Fix Login Bug\",\n    \"description\": \"Resolve the issue with user login on mobile devices\",\n    \"assigned_to\": 3,\n    \"assigned_by\": 7,\n    \"status\": \"IN_PROGRESS\",\n    \"deadline\": \"2025-04-08T18:00:00Z\",\n    \"created_at\": \"2025-04-04T10:46:41.169022Z\",\n    \"updated_at\": \"2025-04-04T10:46:41.169035Z\",\n    \"assigned_to_details\": {\n        \"id\": 3,\n        \"email\": \"kumarsatyam72770@gmail.com\",\n        \"first_name\": \"\",\n        \"last_name\": \"\",\n        \"role\": \"ADMIN\",\n        \"is_active\": true,\n        \"date_joined\": \"2025-04-04T07:13:01.625635Z\",\n        \"failed_tasks_count\": 0\n    },\n    \"assigned_by_details\": {\n        \"id\": 7,\n        \"email\": \"rohit@gmail.com\",\n        \"first_name\": \"rohit\",\n        \"last_name\": \"singh\",\n        \"role\": \"ADMIN\",\n        \"is_active\": true,\n        \"date_joined\": \"2025-04-04T07:47:16.465605Z\",\n        \"failed_tasks_count\": 0\n    }\n}"
						}
					]
				},
				{
					"name": "task-detail",
					"request": {
						"auth": {
							"type": "bearer",
							"bearer": [
								{
									"key": "token",
									"value": "{{authToken}}",
									"type": "string"
								}
							]
						},
						"method": "GET",
						"header": [],
						"url": {
							"raw": "http://127.0.0.1:8000/api/tasks/2/",
							"protocol": "http",
							"host": [
								"127",
								"0",
								"0",
								"1"
							],
							"port": "8000",
							"path": [
								"api",
								"tasks",
								"2",
								""
							]
						}
					},
					"response": [
						{
							"name": "task-detail",
							"originalRequest": {
								"method": "GET",
								"header": [],
								"url": {
									"raw": "http://127.0.0.1:8000/api/tasks/2/",
									"protocol": "http",
									"host": [
										"127",
										"0",
										"0",
										"1"
									],
									"port": "8000",
									"path": [
										"api",
										"tasks",
										"2",
										""
									]
								}
							},
							"status": "OK",
							"code": 200,
							"_postman_previewlanguage": "json",
							"header": [
								{
									"key": "Date",
									"value": "Fri, 04 Apr 2025 10:48:17 GMT"
								},
								{
									"key": "Server",
									"value": "WSGIServer/0.2 CPython/3.8.10"
								},
								{
									"key": "Content-Type",
									"value": "application/json"
								},
								{
									"key": "Vary",
									"value": "Accept"
								},
								{
									"key": "Allow",
									"value": "GET, PUT, PATCH, DELETE, HEAD, OPTIONS"
								},
								{
									"key": "X-Frame-Options",
									"value": "DENY"
								},
								{
									"key": "Content-Length",
									"value": "670"
								},
								{
									"key": "X-Content-Type-Options",
									"value": "nosniff"
								},
								{
									"key": "Referrer-Policy",
									"value": "same-origin"
								},
								{
									"key": "Cross-Origin-Opener-Policy",
									"value": "same-origin"
								}
							],
							"cookie": [],
							"body": "{\n    \"id\": 2,\n    \"title\": \"Fix Login Bug\",\n    \"description\": \"Resolve the issue with user login on mobile devices\",\n    \"assigned_to\": 3,\n    \"assigned_by\": 7,\n    \"status\": \"IN_PROGRESS\",\n    \"deadline\": \"2025-04-08T18:00:00Z\",\n    \"created_at\": \"2025-04-04T10:46:41.169022Z\",\n    \"updated_at\": \"2025-04-04T10:46:41.169035Z\",\n    \"assigned_to_details\": {\n        \"id\": 3,\n        \"email\": \"kumarsatyam72770@gmail.com\",\n        \"first_name\": \"\",\n        \"last_name\": \"\",\n        \"role\": \"ADMIN\",\n        \"is_active\": true,\n        \"date_joined\": \"2025-04-04T07:13:01.625635Z\",\n        \"failed_tasks_count\": 0\n    },\n    \"assigned_by_details\": {\n        \"id\": 7,\n        \"email\": \"rohit@gmail.com\",\n        \"first_name\": \"rohit\",\n        \"last_name\": \"singh\",\n        \"role\": \"ADMIN\",\n        \"is_active\": true,\n        \"date_joined\": \"2025-04-04T07:47:16.465605Z\",\n        \"failed_tasks_count\": 0\n    }\n}"
						}
					]
				},
				{
					"name": "my-tasks",
					"request": {
						"auth": {
							"type": "bearer",
							"bearer": [
								{
									"key": "token",
									"value": "{{authToken}}",
									"type": "string"
								}
							]
						},
						"method": "GET",
						"header": [],
						"url": {
							"raw": "http://127.0.0.1:8000/api/tasks/my-tasks/",
							"protocol": "http",
							"host": [
								"127",
								"0",
								"0",
								"1"
							],
							"port": "8000",
							"path": [
								"api",
								"tasks",
								"my-tasks",
								""
							]
						}
					},
					"response": [
						{
							"name": "my-tasks",
							"originalRequest": {
								"method": "GET",
								"header": [],
								"url": {
									"raw": "http://127.0.0.1:8000/api/tasks/my-tasks/",
									"protocol": "http",
									"host": [
										"127",
										"0",
										"0",
										"1"
									],
									"port": "8000",
									"path": [
										"api",
										"tasks",
										"my-tasks",
										""
									]
								}
							},
							"status": "OK",
							"code": 200,
							"_postman_previewlanguage": "json",
							"header": [
								{
									"key": "Date",
									"value": "Fri, 04 Apr 2025 10:50:20 GMT"
								},
								{
									"key": "Server",
									"value": "WSGIServer/0.2 CPython/3.8.10"
								},
								{
									"key": "Content-Type",
									"value": "application/json"
								},
								{
									"key": "Vary",
									"value": "Accept"
								},
								{
									"key": "Allow",
									"value": "GET, HEAD, OPTIONS"
								},
								{
									"key": "X-Frame-Options",
									"value": "DENY"
								},
								{
									"key": "Content-Length",
									"value": "2"
								},
								{
									"key": "X-Content-Type-Options",
									"value": "nosniff"
								},
								{
									"key": "Referrer-Policy",
									"value": "same-origin"
								},
								{
									"key": "Cross-Origin-Opener-Policy",
									"value": "same-origin"
								}
							],
							"cookie": [],
							"body": "[]"
						}
					]
				},
				{
					"name": "overdue-tasks",
					"request": {
						"auth": {
							"type": "bearer",
							"bearer": [
								{
									"key": "token",
									"value": "{{authToken}}",
									"type": "string"
								}
							]
						},
						"method": "GET",
						"header": [],
						"url": {
							"raw": "http://127.0.0.1:8000/api/tasks/overdue-tasks/",
							"protocol": "http",
							"host": [
								"127",
								"0",
								"0",
								"1"
							],
							"port": "8000",
							"path": [
								"api",
								"tasks",
								"overdue-tasks",
								""
							]
						}
					},
					"response": [
						{
							"name": "overdue-tasks",
							"originalRequest": {
								"method": "GET",
								"header": [],
								"url": {
									"raw": "http://127.0.0.1:8000/api/tasks/overdue-tasks/",
									"protocol": "http",
									"host": [
										"127",
										"0",
										"0",
										"1"
									],
									"port": "8000",
									"path": [
										"api",
										"tasks",
										"overdue-tasks",
										""
									]
								}
							},
							"status": "OK",
							"code": 200,
							"_postman_previewlanguage": "json",
							"header": [
								{
									"key": "Date",
									"value": "Fri, 04 Apr 2025 10:52:17 GMT"
								},
								{
									"key": "Server",
									"value": "WSGIServer/0.2 CPython/3.8.10"
								},
								{
									"key": "Content-Type",
									"value": "application/json"
								},
								{
									"key": "Vary",
									"value": "Accept"
								},
								{
									"key": "Allow",
									"value": "GET, HEAD, OPTIONS"
								},
								{
									"key": "X-Frame-Options",
									"value": "DENY"
								},
								{
									"key": "Content-Length",
									"value": "2"
								},
								{
									"key": "X-Content-Type-Options",
									"value": "nosniff"
								},
								{
									"key": "Referrer-Policy",
									"value": "same-origin"
								},
								{
									"key": "Cross-Origin-Opener-Policy",
									"value": "same-origin"
								}
							],
							"cookie": [],
							"body": "[]"
						}
					]
				}
			]
		},
		{
			"name": "notify",
			"item": [
				{
					"name": "notify manager",
					"request": {
						"method": "GET",
						"header": []
					},
					"response": []
				}
			]
		}
	]
}


