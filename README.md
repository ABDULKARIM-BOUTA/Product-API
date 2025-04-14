Rest-API

A robust Django REST Framework API with custom user authentication using JWT, product search using Algolia, and a clean, scalable structure for real-world projects.

Live Demo:

rest-api-dj.up.railway.app/

Features:

  -JWT Authentication (SimpleJWT)
  -Custom user model with email login
  -Product listing & management
  -Full-text search via Algolia
  -DRF auto-generated schema docs (via drf-spectacular)
  -Token refresh, throttle limits, and pagination
  -CORS support & secure deployment configs

Tech Stack:

  -Backend: Django, Django REST Framework
  -Auth: JWT (SimpleJWT)
  -Search: Algolia
  -Docs: drf-spectacular
  -Deployment: Render
  -Database: PostgreSQL

Project Structure:
  
  ├── api/               # API-wide settings and utils

  ├── products/          # Product app (CRUD, list, search)
  
  ├── users/             # Custom user model, auth backends
  
  ├── search/            # Algolia search indexing
  
  ├── _home/             # Django settings and core urls
  
  ├── py_client/         # Python client for testing the API
  
  ├── requirements.txt   # Python dependencies
  
  └── manage.py


Getting Started

Clone the repository
  
  git clone https://github.com/ABDULKARIM-BOUTA/Rest-API.git
  
  cd Rest-API

Create a virtual environment
  
  python -m venv venv
  
  venv\Scripts\activate

Set up environment variables and Create a .env file:
 
  SECRET_KEY=your_secret_key_here
  DEBUG=True
  ALGOLIA_APPLICATION_ID=your_algolia_app_id
  ALGOLIA_API_KEY=your_algolia_api_key

Install dependencies
  
  pip install -r requirements.txt

Run migrations
  
  python manage.py migrate

Create a superuser

  python manage.py createsuperuser

Start the development server

  python manage.py runserver

to use the search function you need to have an Algolia account
