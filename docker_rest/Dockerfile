FROM python:3.12.2

WORKDIR /usr/local/app

# Install the application dependencies
COPY ./requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy in the source code
COPY app.py ./
COPY telefonica.py ./

EXPOSE 8000

# Setup an app user so the container doesn't run as the root user
RUN useradd app
USER app

ENTRYPOINT ["python", "app.py"]
