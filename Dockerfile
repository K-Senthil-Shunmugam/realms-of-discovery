# Stage 1: Build React App
FROM node:21 AS build

WORKDIR /app/frontend

# Copy package.json and package-lock.json for the frontend
COPY front-end/package*.json ./

# Install frontend dependencies
RUN npm install

# Copy the rest of the frontend app
COPY front-end/ .

# Build the React app
RUN npm run build

# Stage 2: Set up Python Backend with Nginx as Reverse Proxy
FROM python:3.9-slim AS backend

WORKDIR /app

# Install dependencies for the Python backend
COPY back-end/requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the Python app
COPY back-end/ /app

# Install Node.js (needed for serving the React app)
RUN apt-get update && apt-get install -y curl && \
    curl -sL https://deb.nodesource.com/setup_16.x | bash - && \
    apt-get install -y nodejs

# Install Nginx
RUN apt-get update && apt-get install -y nginx

# Copy the build output of the React app from the build stage
COPY --from=build /app/frontend/build /app/frontend/build

RUN npm install -g serve

# Nginx configuration
COPY nginx.conf /etc/nginx/nginx.conf

# Expose ports for both backend and frontend (Nginx will listen on port 80)
EXPOSE 80 

# Use supervisord to manage multiple processes (Flask app and Nginx)
RUN apt-get install -y supervisor
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

# Start the backend (Flask) and Nginx with supervisord
CMD ["/usr/bin/supervisord"]
