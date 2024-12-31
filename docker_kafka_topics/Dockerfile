FROM python:3.12.2

WORKDIR /usr/local/app

# Install the application dependencies
COPY ./requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy in the source code
COPY consumer.py ./
COPY telefonica.py ./

# Disable buffering for Python output
ENV PYTHONUNBUFFERED=1

# Setup an app user so the container doesn't run as the root user
RUN useradd app
USER app

CMD ["python", "consumer.py"]
