#!/bin/sh
# wait-for-postgres.sh
set -e


until  psql  "postgresql://$DB_USER:$DB_PASSWORD@$DB_HOST/postgres"  -c '\q'; do
  >&2 echo "Postgres is unavailable - sleeping"
  sleep 1
done

echo "SELECT 'CREATE DATABASE $DB_NAME' WHERE NOT EXISTS (SELECT FROM pg_database WHERE datname = '$DB_NAME')\gexec"| PGPASSWORD=$DB_PASSWORD psql -h  "$DB_HOST" -U  "$DB_USER"

>&2 echo "Postgres is up - executing command"

python manage.py makemigrations
python manage.py migrate

python manage.py create_immobile 5
python manage.py create_announcement 3
python manage.py create_reserve 8

echo "Executing  Developer Server"
python manage.py runserver 0.0.0.0:8000