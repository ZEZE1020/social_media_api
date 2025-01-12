
# **BE Capstone Project: Social Media API**

## **Project Overview**

This project aims to develop a Social Media API using Django and Django REST Framework. The API will enable users to create, update, and delete posts, follow other users, and view a feed of posts from users they follow. The system will manage user data, posts, and interactions in a simulated social media environment. This project is designed to provide experience in handling user relationships, database interactions, and large datasets, focusing on CRUD operations and API design.

## **Functional Requirements**

### **Post Management (CRUD)**

* **Create, Read, Update, Delete Posts**: Users can perform CRUD operations on posts.
* **Post Attributes**: Each post includes content, author, timestamp, and optional media (e.g., image URLs).
* **Validation**: Ensure required fields like content and user are validated.
* **Authorization**: Users can only update or delete their own posts.

### **User Management (CRUD)**

* **Create, Read, Update, Delete Users**: Implement CRUD operations for users.
* **User Attributes**: Each user has a unique username, email, password, and optional profile fields like bio and profile picture.
* **Authentication**: Only authenticated users can create, update, or delete their own posts.

### **Follow System**

* **Follow/Unfollow**: Implement endpoints for users to follow and unfollow other users.
* **Relationship Management**: Store follower and following relationships between users.
* **Validation**: Ensure users cannot follow themselves.

### **Feed of Posts**

* **User Feed**: Allow users to view a feed of posts from the users they follow.
* **Sorting**: Display posts in reverse chronological order (most recent posts first).
* **Filtering**: Optionally, allow users to filter the feed by date or search for posts by keyword.

## **Technical Requirements**

### **Database**

* **Django ORM**: Use Django ORM to interact with the database.
* **Models**: Define models for Users, Posts, and Followers.
* **Relationships**: Ensure each post is linked to a user, and followers/following relationships are tracked efficiently.

### **Authentication**

* **Django Authentication**: Implement user authentication using Django’s built-in authentication system.
* **Protected Actions**: Users must be logged in to create, update, or delete posts, follow other users, or view their feed.
* **Optional JWT**: Optionally, implement token-based authentication (JWT) for secure access to the API.

### **API Design**

* **Django Rest Framework (DRF)**: Use DRF to design and expose the necessary API endpoints.
* **RESTful Principles**: Follow RESTful principles, using appropriate HTTP methods (GET, POST, PUT, DELETE) for different operations.
* **Error Handling**: Ensure proper error handling with relevant HTTP status codes (e.g., 404 for not found, 400 for bad request).

### **Deployment**

* **Heroku or PythonAnywhere**: Deploy the API on Heroku or PythonAnywhere.
* **Security and Performance**: Ensure the API is accessible, secure, and performs well in the deployed environment.

### **Pagination and Sorting**

* **Pagination**: Add pagination to the feed of posts for users with large numbers of followed users or a large volume of posts.
* **Sorting Options**: Provide sorting options such as sorting by date or popularity (likes, comments).

## **Setup Instructions**

Follow these steps to set up the project on your local machine:

### **Prerequisites**

* Ensure you have Python 3.6 or higher installed.
* Install PostgreSQL and create a database and user.

### **Clone the Repository**

Clone the repository to your local machine: \
bash \

```
git clone https://github.com/ZEZE1020/social_media_api.git
cd social_media_api
```

1.

### **Set Up Virtual Environment**

Create and activate a virtual environment: \
bash \

```
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

1.

### **Install Dependencies**

Install the required dependencies: \

```
bash
pip install -r requirements.txt
```

1.

### **Environment Variables**

Create a `.env` file in the root directory and add the following environment variables: \
plaintext \

```
SECRET_KEY='your-secret-key'
DEBUG=True  # Set to False in production
DATABASE_NAME='your_database_name'
DATABASE_USER='your_database_user'
DATABASE_PASSWORD='your_database_password'
DATABASE_HOST='localhost'
DATABASE_PORT='5432'
```

1.

### **Update Settings**

Update the `DATABASES` setting in `social_media_api/settings.py` to use environment variables: \
python \

```
import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DATABASE_NAME'),
        'USER': os.getenv('DATABASE_USER'),
        'PASSWORD': os.getenv('DATABASE_PASSWORD'),
        'HOST': os.getenv('DATABASE_HOST'),
        'PORT': os.getenv('DATABASE_PORT'),
    }
}
```

1.

### **Run Migrations**

Apply database migrations: \
bash \

```
python manage.py makemigrations
python manage.py migrate
```

1.

### **Create Superuser**

Create a superuser to access the Django admin interface: \
bash \

```
python manage.py createsuperuser
```

1.

### **Collect Static Files**

Collect static files: \
bash \

```
python manage.py collectstatic
```

1.

### **Run the Development Server**

Start the development server: \
bash \

```
python manage.py runserver
```

1.

You should now be able to access the project at `http://127.0.0.1:8000/`
