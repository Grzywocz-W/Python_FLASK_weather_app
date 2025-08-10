#!/bin/sh

echo "Czekam na PostgreSQL..."
until pg_isready -h db -p 5432; do
  sleep 1
done

echo "PostgreSQL dostępny – startuję aplikację!"
exec python main.py
