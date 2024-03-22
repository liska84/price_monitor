# Use an official Python runtime as a parent image, with support for Chrome
FROM python:3.8-slim-buster

# Install Chrome
RUN apt-get update && apt-get install -y wget gnupg2 cron \
    && wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb \
    && apt install -y ./google-chrome-stable_current_amd64.deb

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DISPLAY=:99

# Set the working directory in the container
WORKDIR /app

# Install Python dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the project files into the container
COPY . /app/

# Set execute permissions on the management command
RUN chmod +x /app/manage.py

# Add your crontab file
COPY crontab /etc/cron.d/my-crontab

# Give execution rights on the cron job and apply it
RUN chmod 0644 /etc/cron.d/my-crontab \
    && crontab /etc/cron.d/my-crontab \
    && touch /var/log/cron.log

# CMD to keep the container running and start cron
CMD cron && tail -f /var/log/cron.log