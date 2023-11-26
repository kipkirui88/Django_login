Django Login System Readme
Table of Contents
Introduction
Setup
Usage
Mockups
Web Server Configuration
Security
Contributing
License
Introduction
This Django Login System provides a secure login and success page. The project includes advanced design mockups, detailed setup instructions, and web server configuration using uWSGI and Nginx.

Setup
Clone Repository:

bash

git clone https://github.com/kipkirui88/Django_login.git
cd django-login-system
Install Dependencies:

bash

pip install -r requirements.txt
Database Migration:

bash

python manage.py makemigrations
python manage.py migrate
Create Superuser (Admin):

bash

python manage.py createsuperuser
Run Development Server:

bash

python manage.py runserver
Usage
Visit http://localhost:8000/login in your browser. Log in using the created superuser credentials. Explore the login and success pages.

Mockups
The mockup is a simple login page with two fields for username and password, as well as a submit button. The user enters their credentials in the login page 

Web Server Configuration
uWSGI Configuration
Use the following uWSGI command to run the application:

bash

uwsgi --http :8000 --module InterIntel.wsgi

Nginx Configuration
Ensure Nginx is installed and create a server block:

nginx

server {
    listen 80;
    server_name https://interintel.onrender.com;

    location = /favicon.ico { access_log off; log_not_found off; }

    location / {
        include         uwsgi_params;
        uwsgi_pass      unix:/InterIntel/project.sock;
    }

    error_page 404 /404.html;
    location = /404.html {
        root /InterIntel/static/;
    }

    error_page 500 502 503 504 /50x.html;
    location = /50x.html {
        root /InterIntel/static/;
    }
}

Security
Sessions are securely managed using Django's built-in session framework. Ensure that HTTPS is enabled for secure communication.

Contributing
Feel free to contribute by opening issues or submitting pull requests.

License
This project is licensed under the MIT License.

