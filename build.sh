npm run build
python manage.py collectstatic --noinput
gunicorn backend.wsgi