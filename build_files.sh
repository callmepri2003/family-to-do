#!/bin/bash

# Install Python dependencies
python3 -m pip install -r requirements.txt

# Run Django migrations
python3 manage.py migrate

python3 manage.py shell <<EOF
from django.contrib.auth.models import User
from django.core.management import call_command

# Check if the superuser already exists to avoid duplicate creation
if not User.objects.filter(username='admin').exists():
    call_command('createsuperuser', '--noinput', '--username', 'admin', '--email', 'admin@example.com')
    user = User.objects.get(username='admin')
    user.set_password('adminpassword')  # Set password for superuser
    user.is_superuser = True
    user.is_staff = True
    user.save()
EOF