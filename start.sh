#!/bin/bash
gunicorn email_service:app --bind 0.0.0.0:$PORT