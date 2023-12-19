# gunicorn_config.py

bind = "0.0.0.0:8000"  # Use the same port as specified in your original Gunicorn command
workers = 3
threads = 2  # Add threads if needed
