# Django REST API for Hackathon Registration and Submission

### To Run on Localhost

- Have `Python` and `pip` installed on your local machine

### Running the Django project

Create an isolated environment for the project with `virtualenv`. You can install `virtualenv` with the following command:

```
sudo pip install virtualenv
```

Create a new directory for the project:

```
mkdir myproject && cd myproject
```

Create a virtual environment for the project:

```bash
virtualenv env
```

Then, activate it:

```bash
source env/bin/activate
```

Clone the project from GitHub:

```bash
git clone https://github.com/KanvaBhatia/hackathon_app.git
```

cd into the project and install requirements:
```bash
cd hackathon_app
pip install -r requirements.txt
```

Finally, run the project:

```bash
python manage.py migrate
python manage.py runserver
```


Go to http://localhost:8000/api/ to see if the API is up and running.


## Create superuser

Create a superuser to add more users for testing.

```bash
python manage.py createsuperuser
```
Run this command and follow its steps.


# API endpoints

### 1. Create a Hackathon - 

http://127.0.0.1:8000/api/create-hackathon/

Accessible by Authorised users only.
Can add users to staff by using superuser login and going to http://127.0.0.1:8000/admin/

### 2. List all Hackathons - 

http://127.0.0.1:8000/api/hackathons/

Accessible by all users.

### 3. Register for a hackathon - 

http://127.0.0.1:8000/api/register/

Accesible by users who've logged in.

### 4. Make Submissions - 

http://127.0.0.1:8000/api/submit/

Accessible by users who've logged in.

### 5. List the hackathons users are enrolled to -

http://127.0.0.1:8000/api/enrolled-hackathons/

Accessible by users who've logged in.

### 6. View their submissions in the hackathon users were enrolled in -

http://127.0.0.1:8000/api/hackathons/{hackathon_id})/user-submissions

Here, hackathon_id can be 1, 2, 3, etc. 

### 7. View users who are not enrolled to even a single hackathon -

http://127.0.0.1:8000/api/non-enrolled-participants/

### 8. View users who are enrolled to at least a single hackathon -

http://127.0.0.1:8000/api/enrolled-participants/



## Auth endpoints - 

### 1. Login - 

http://127.0.0.1:8000/api/auth/login

### 2. Logout - 

http://127.0.0.1:8000/api/auth/logout


# Deployed on Railway - 
https://hackathonapp-production.up.railway.app/api

### To create more users, login to  -
https://hackathonapp-production.up.railway.app/admin

Username - admin
Password AIPlanet


