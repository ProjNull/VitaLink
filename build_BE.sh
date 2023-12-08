#!/usr/bin/env bash
cd backend/
gunicorn --worker-class eventlet -w 1 main:app