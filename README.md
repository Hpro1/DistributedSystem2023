# DistributedSystem2023
Implementation of three microservices using Python, Flask, and FastAPI.

Video demonstration: https://www.youtube.com/watch?v=E8eFwpuNl28

These can be tested using curl, or a program with GUI, Postman for example.

```
auth_service.py:
/register endpoint
POST
http://localhost:5000/register
Paste raw as JSON
{
    "username": "testuser",
    "password": "testpassword"
}

Test the /login endpoint
POST
http://localhost:5000/login
{
    "username": "testuser",
    "password": "testpassword"
}
```
```
course_service.py:
POST
http://localhost:8000/courses/
{
    "id": 1,
    "title": "Introduction to Python",
    "description": "Learn the basics of Python programming language."
}

GET
http://localhost:8000/courses/
```
```
content_service.py:
POST
http://localhost:5001/content
{
    "id": 1,
    "course_id": 1,
    "title": "Python Basics",
    "content_type": "video",
    "url": "https://example.com/python-basics-video"
}

GET
http://localhost:5001/content
```
