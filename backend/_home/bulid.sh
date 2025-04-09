#!/bin/bash

# Exit immediately if any command fails
set -e

# Run database migrations
echo "Running database migrations..."
python manage.py makemigrations
python manage.py migrate

# Create superuser if needed (optional)
echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin', 'admin@example.com', 'password') if not User.objects.filter(username='admin').exists() else None" | python manage.py shell

# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --noinput

echo "Build completed successfully"