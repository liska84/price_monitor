# Use an official Python runtime as a parent image, with support for Firefox
FROM python:3.8-slim-buster

# Install necessary packages including dependencies for Firefox and Xvfb
RUN apt-get update && apt-get install -y \
    wget \
    gnupg2 \
    cron \
    firefox-esr \
    xvfb \
    libgl1-mesa-dri \
    libgl1-mesa-glx \
    libdbus-glib-1-2 \
    libxt6 \
    && rm -rf /var/lib/apt/lists/*

# Install Geckodriver for Firefox
RUN wget -O /tmp/geckodriver.tar.gz https://github.com/mozilla/geckodriver/releases/download/v0.34.0/geckodriver-v0.34.0-linux64.tar.gz \
    && tar -xzf /tmp/geckodriver.tar.gz -C /usr/local/bin \
    && rm /tmp/geckodriver.tar.gz

# Set up Xvfb
ENV DISPLAY=:99

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

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

COPY entrypoint.sh /usr/local/bin/entrypoint.sh
RUN chmod +x /usr/local/bin/entrypoint.sh

ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]