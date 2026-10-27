# Healthcare Backend

Django + DRF + PostgreSQL project with JWT auth. Users can register, log in, and manage patients, doctors and patient-doctor mappings.

## Running it

```
python -m venv venv
venv\Scripts\activate        (linux/mac: source venv/bin/activate)
pip install -r requirements.txt
```

Copy `.env.example` to `.env` and put in your own values, and create the postgres database that you named in it. Then:

```
python manage.py makemigrations accounts patients doctors mappings
python manage.py migrate
python manage.py runserver
```

## APIs

Everything except register and login needs the header `Authorization: Bearer <access token>`.

- POST `/api/auth/register/`  (name, email, password)
- POST `/api/auth/login/`  (email, password)
- `/api/patients/` and `/api/patients/<id>/`
- `/api/doctors/` and `/api/doctors/<id>/`
- `/api/mappings/` and `/api/mappings/<id>/`

Example bodies:

```
patient:  {"name": "John", "age": 34, "gender": "M", "phone": "9999999999", "address": "Delhi", "medical_history": "Asthma"}
doctor:   {"name": "Asha Rao", "email": "asha@example.com", "specialization": "Cardiology", "experience": 10}
mapping:  {"patient": 1, "doctor": 1}
```

A user can only see and change the patients they created. Doctors are visible to everyone, but only the user who added a doctor can edit or delete it.
