#!/bin/bash
set -e  # Exit immediately on error

# 1. Database migrations (always run)
python manage.py makemigarations
python manage.py migrate

# 2. Superuser creation (environment-controlled)
if [ "$DJANGO_CREATE_SUPERUSER" = "true" ] && [ -n "$DJANGO_SUPERUSER_EMAIL" ] && [ -n "$DJANGO_SUPERUSER_PASSWORD" ]; then
    echo "Creating superuser..."
    export DJANGO_SUPERUSER_USERNAME="${DJANGO_SUPERUSER_EMAIL%@*}"  # Use email prefix as username
    python manage.py createsuperuser --noinput --email "$DJANGO_SUPERUSER_EMAIL" || true

    # Force password update (in case user already exists)
    echo "from django.contrib.auth import get_user_model; User = get_user_model(); \
          user = User.objects.get(email='$DJANGO_SUPERUSER_EMAIL'); \
          user.set_password('$DJANGO_SUPERUSER_PASSWORD'); user.save()" | python manage.py shell
fi

# 3. Static files collection
python manage.py collectstatic --noinput