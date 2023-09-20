#!/bin/bash
echo "Creating Migrations..."
python3 manage.py makemigrations
echo ====================================

echo "Starting Migrations..."
python3 manage.py migrate
echo ====================================

echo "Setting up default user..."
python3 manage.py createsuperuser --noinput
echo ====================================

echo "Starting Server on port $PORT..."
python3 manage.py runserver 0.0.0.0:$PORT
