# DrawinX Technologies — Django + Bootstrap starter

A Django conversion of the supplied DrawinX website starter. It preserves the original dark navy / electric-blue visual language, page structure, copy, and contact-enquiry workflow while replacing Next.js/React/Prisma with Django templates, Bootstrap, and Django ORM.

## Stack
- Python + Django 5.2
- Django templates (server-rendered HTML)
- Bootstrap 5.3 (CDN) + the original custom CSS design
- SQLite for local development
- PostgreSQL for production (recommended on Render)
- Django admin for enquiry management
- Gunicorn + WhiteNoise for Render deployment

## Pages
- `/` Home
- `/services/` Services
- `/divisions/` Divisions
- `/projects/` Projects
- `/about/` About
- `/contact/` Contact form
- `/privacy/` Privacy notice draft
- `/admin/` Django admin

## Run locally on Ubuntu

```bash
cd drawinx-django-bootstrap
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env  # optional; edit values if needed; SQLite works without DATABASE_URL
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Open http://127.0.0.1:8000. Admin is at http://127.0.0.1:8000/admin/.

## Contact enquiries
The contact form validates input server-side, uses Django CSRF protection, includes a honeypot field, and stores valid enquiries in the database. Manage them in Django admin. In local DEBUG mode email uses Django's console backend. Before production, configure SMTP credentials and verify delivery; database storage does not depend on email delivery. Add provider-level rate limiting / bot protection before public launch (a honeypot alone is not sufficient).

## Render deployment
1. Push this folder to a Git repository.
2. Create a Render PostgreSQL database and copy its Internal Database URL.
3. Create a Render Web Service from the repository.
4. Build command: `./build.sh`
5. Start command: `gunicorn config.wsgi:application`
6. Set environment variables:
   - `DJANGO_SECRET_KEY`: long random secret
   - `DJANGO_DEBUG`: `False`
   - `DJANGO_ALLOWED_HOSTS`: your Render hostname and custom domain, comma-separated
   - `CSRF_TRUSTED_ORIGINS`: `https://your-render-hostname.onrender.com,https://drawinx.com,https://www.drawinx.com`
   - `DATABASE_URL`: Render PostgreSQL Internal Database URL
   - `CONTACT_EMAIL`: monitored company inbox
   - `EMAIL_HOST`, `EMAIL_PORT`, `EMAIL_HOST_USER`, `EMAIL_HOST_PASSWORD`, `EMAIL_USE_TLS`, `DEFAULT_FROM_EMAIL`: SMTP configuration for enquiry notifications
7. Attach the custom domain and configure DNS after verifying domain availability.

`build.sh` installs dependencies and collects static files. Run migrations as a deploy/release step or run `python manage.py migrate` once the database environment is connected. For a simple first deployment, you can append it to the start workflow, but a dedicated release command is preferable when available.

## Important before launch
- Replace the contact email with an inbox that is monitored.
- Configure SMTP if email notifications are needed.
- Add a robust rate limiter / WAF or form protection service.
- Complete and review the privacy notice and retention process.
- Create strong admin credentials and enable MFA on the hosting and email accounts.
- Verify all public project descriptions, permissions, legal details, and domain ownership.
- Configure database backups and test restore procedures.
- Keep secrets in Render environment variables, never in Git.

## Notes
The website intentionally avoids invented testimonials, clients, certifications, and claims. Update project statuses only when verified. The supplied visual stylesheet is retained as the primary design layer; Bootstrap provides responsive utilities and form controls.
