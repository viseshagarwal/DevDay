###Task-3
# Django Rest Framework Blog API

This project is a simple Django Rest Framework (DRF) API for performing CRUD operations on blog posts. It allows users to create, read, update, and delete blog posts, handling data such as titles, content, publication dates, and author information.

## Getting Started

Follow these instructions to set up and run the project locally.

### Prerequisites

Make sure you have the following software installed on your machine:

- Python (>=3.6)
- Django
- Django Rest Framework

### Installation
Pip install django
Pip install django_framework

## Apply Migrations
python manage.py migrate

##Create Super User
python manage.py createsuperuser
 ## run python server
python manage.py runserver

The API server will start running at http://localhost:8000/. You can access the browsable API interface in your web browser.
API Endpoints
* GET /api/posts/: List all blog posts and create a new blog post.
* GET /api/posts/<id>/: Retrieve, update, or delete a specific blog post by ID.
* POST /api/posts/: List all blog posts and create a new blog post.
* POST /api/posts/<id>/: Retrieve, update, or delete a specific blog post by ID.
* PUT /api/posts/<id>/: Retrieve, update, or delete a specific blog post by ID.

### Task-2

# Online Drawing Board with Canvas

This web application allows users to draw and create art using HTML5 Canvas. It provides basic drawing tools and features for an interactive experience.

## Features

1. **Brush Options**:
   - Users can customize the brush size and color.
   - Use the slider to adjust the brush size.
   - Choose the brush color using the color picker.

2. **Clear Canvas**:
   - Click the "Clear Canvas" button to erase the entire canvas and start over.

###Task-3
# URL Shortener Service

This is a simple URL shortener service that generates a short, unique code for long URLs and redirects users to the original long URL when they access the short URL.

## API Endpoints

1. **POST /api/shorten**:
   - Accepts a long URL in the request body and generates a short code for it.
   - Returns the generated short URL.

2. **GET /:code**:
   - Redirects users to the original long URL associated with the provided short code.

## Short Code Generation

A short, unique code is generated for each long URL using an algorithm like Base64 encoding or hashing functions.

## Data Storage

Long URLs and their corresponding short codes are stored in memory. For a production environment, you may consider using a database for storage.

## Validation and Error Handling

Validation is performed to ensure that the provided long URL is valid. Error handling is implemented to handle cases where invalid requests are made.

## Optional Features

### Expiry Time for Short URLs

Short URLs can have an expiration time, making them valid only for a certain duration. Implementing this feature ensures that short URLs expire after a specified period.

### Custom Short Codes

Users can provide a custom short code for their long URL if available. Implementing this feature allows users to have more control over the short codes generated for their URLs.

## Usage

1. To shorten a URL, make a POST request to `/api/shorten` with a JSON body containing the long URL.
2. The response will contain the generated short URL.
3. Users can access the short URL directly in their browser or use it in their applications.
4. When users access the short URL, they will be redirected to the original long URL.







