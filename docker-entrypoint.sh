#!/bin/sh

set -e

. /venv/bin/activate

python manage.py collectstatic --noinput
python manage.py migrate

if [ "$URLPROMPT_ADMIN_USER" ] && [ ! -f .superuser ];
then
    DJANGO_SUPERUSER_PASSWORD="$URLPROMPT_ADMIN_PASS"
    python manage.py createsuperuser --noinput --username $URLPROMPT_ADMIN_USER --email $URLPROMPT_ADMIN_USER@urlprompt.changeme || true
    touch .superuser
fi



exec gunicorn -w 4 --bind 0.0.0.0:5000 --forwarded-allow-ips='*' urlprompt.wsgi
