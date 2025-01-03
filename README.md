# Realms of Discovery

## Overview
Realms of Discovery is a text-based adventure game that immerses players in a dynamic and interactive world. This repository includes both the backend and frontend components, designed to work seamlessly together. The project is fully containerized using Docker and is ready for deployment.

The backend handles game logic, user authentication, and database interactions, while the frontend provides a responsive and intuitive user interface for players.

---

## Features

### Backend
- *Game Logic*: Implements player, NPC, room, and utility mechanics for an engaging adventure experience.
- *User Authentication*: Includes login, logout, and signup functionalities.
- *MongoDB Integration*: Stores and retrieves game data efficiently.
- *Modular Design*: Organized into dedicated modules for scalability.

### Frontend
- *Responsive UI*: Built with modern web technologies for seamless cross-device gameplay.
- *Dynamic Components*: Interactive game elements powered by React.
- *Media Assets*: High-quality images enhance the visual experience.

### Deployment
- *Dockerized*: Both backend and frontend are containerized for easy deployment.
- *Nginx Configuration*: Configured for efficient serving of the application.

---

## File Structure

### Root Directory
- *Dockerfile*: Docker setup for containerizing the application.
- *nginx.conf*: Configuration for Nginx reverse proxy.
- *supervisord.conf*: Supervisor configuration for process management.

### Backend (back-end)
- *app.py*: Entry point for the backend server.
- *authentication/*: Handles user login, logout, and signup.
  - login.py, logout.py, signup.py
- *config.py: Contains database connection settings. **Update the database link before running the application.*
- *game_logic/*: Core game logic and utilities.
  - game.py, npc.py, player.py, room.py, etc.
  - room_images/: Contains default room images.
- *mongo_db/*: Database interaction logic.
  - db.py
- *requirements.txt*: Python dependencies for the backend.

### Frontend (front-end)
- *package.json* & *package-lock.json*: Dependency management.
- *public/*: Static assets for the frontend.
  - index.html, favicon.ico, manifest.json, etc.
  - *Realms Image/*: Thematic background images (e.g., inferno, kingdom, sea).
  - *images/*: Logos and team photos.
- *src/*: Source code for the frontend.
  - App.js, index.js: Application entry points.
  - *components/*: Modular React components (e.g., Home.js, Login.js, Play.js).

---

## Prerequisites

- Docker
- Node.js (for local frontend development)
- Python 3.8+ (for local backend development)
- MongoDB instance (*Update the link in config.py*)

---

## Installation and Deployment

### 1. Clone the Repository
bash
git clone https://github.com/yourusername/realms-of-discovery.git
cd realms-of-discovery


### 2. Build and Run Docker Containers
bash
docker-compose up --build


### 3. Update Database Configuration
Modify the config.py file in back-end/ to include your MongoDB connection link.

### 4. Access the Application
- *Frontend*: Open your browser at http://localhost:80.
- *Backend*: The server runs on http://localhost:5000.