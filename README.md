# django-logging-with-auditlog


- The project test django logging using `django-auditlog(https://github.com/jazzband/django-auditlog)`

- 2 Models were created and both registered for log, the first included the history field
while the second did not.

- APIs are added to pull the logs for the records in the project.
  - Per Objects, and
  - Accross all models

- How to run:
  - Run migrate with `python manage.py migrate`
  - Run the server with `python manage.py runsevrer`
