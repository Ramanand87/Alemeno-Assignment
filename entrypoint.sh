#!/bin/bash


echo "✅ Running migrations..."
python manage.py makemigrations
python manage.py migrate


echo "🚀 Ingesting Excel data..."
python manage.py ingest_excel

echo "🌐 Starting Django server..."
python manage.py runserver 0.0.0.0:8000
