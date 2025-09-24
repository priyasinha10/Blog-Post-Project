# Blog-Post-Project
Blog API with JWT Authentication is a Django REST Framework backend that allows users to create, read, update, and delete blog posts securely. It includes author-only permissions, image uploads, search, pagination, and token-based authentication.

# Django Blog API with JWT Authentication

## Project Description
**Blog API with JWT Authentication** is a Django REST Framework backend that allows users to create, read, update, and delete blog posts securely. It includes author-only permissions, image uploads, search, pagination, and token-based authentication.  

## Features
- CRUD operations for blog posts (title, content, image, author, published date)  
- JWT authentication with 1-day access tokens  
- Only authors can update or delete their own posts  
- Image upload for posts  
- Search by title/content  
- Pagination
- Unit tests for authentication, CRUD, and permissions  

---

## Setup Instructions

### 1. Clone the repository
```bash
git clone <repo-url>
cd blog-project

2. Create a virtual environment
python3 -m venv blog_env
source blog_env/bin/activate

3. Install dependencies
pip install -r requirements.txt

4. Apply migrations
python manage.py makemigrations
python manage.py migrate

5. Create a superuser
python manage.py createsuperuser
username - priya
password - Test@123

6. Run the development server
python manage.py runserver

---

## How to Run and Test the APIs

After setting up the project and running the server (`python manage.py runserver`), you can access and test the API endpoints as follows:

### 1. Obtain JWT Token
Use your username and password to get an access token:

```bash
curl -X POST http://127.0.0.1:8000/api/jwt/token/ \
-H "Content-Type: application/json" \
-d '{"username": "<your_username>", "password": "<your_password>"}'

2. Use the Access Token to Authenticate
Include the token in the Authorization header for all protected endpoints:
-H "Authorization: Bearer <ACCESS_TOKEN>"
---

## Running and Understanding Test Cases

The project includes automated tests to ensure the API works correctly with JWT authentication, CRUD operations, and author permissions.

### **Test Case Overview**

| Test Function | Purpose | Expected Result |
|---------------|---------|----------------|
| `test_jwt_authentication_valid` | Test if a user with a valid JWT token can access `/api/posts/` | `200 OK` |
| `test_create_post_authenticated` | Authenticated user creates a blog post | `201 Created` |
| `test_create_post_unauthenticated` | Unauthenticated user attempts to create a post | `401 Unauthorized` |
| `test_update_post_author` | Author updates their own post | `200 OK` |
| `test_update_post_non_author` | Other user tries to update someone else’s post | `403 Forbidden` |
| `test_delete_post_author` | Author deletes their own post | `204 No Content` |
| `test_delete_post_non_author` | Other user tries to delete someone else’s post | `403 Forbidden` |

### **How JWT Tokens Are Used in Tests**
- `get_jwt_token(user)` generates an **access token** for the given user.
- `authenticate(user)` sets the token in the `Authorization` header for all subsequent requests:
```python
self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {token}")

How to Run Tests

Activate the virtual environment:
source blog_env/bin/activate

Run tests:
python manage.py test posts




