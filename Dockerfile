FROM python:3.8-slim

# Copy over app and reqs
COPY src/ /app
COPY reqs/app.txt /app/requirements.txt

# Set cwd to app
WORKDIR /app

# Install dependencies
RUN pip3 install -r /app/requirements.txt
ENV PYTHONPATH "${PYTHONPATH}:/app"
CMD [ "uvicorn", "main:app", "--reload", "--host=0.0.0.0", "--port=80"]

EXPOSE 80