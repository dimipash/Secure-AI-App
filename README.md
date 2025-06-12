# Secure-AI-App

A web application for generating and solving security challenges with AI assistance. This project is currently in development.

## Project Overview

Secure-AI-App is designed to help users learn about security concepts through interactive challenges. The application leverages AI to generate security scenarios and provides a platform for users to solve these challenges.

## Features (Planned)

- User authentication via Clerk
- AI-powered security challenge generation
- Challenge history tracking
- Interactive UI for solving security challenges

## Project Structure

The project is divided into two main components:

### Backend

- FastAPI application
- OpenAI integration for challenge generation
- SQLAlchemy for database management
- Authentication via Clerk SDK

### Frontend

- React application built with Vite
- React Router for navigation
- Clerk for authentication
- Component-based architecture

## Technologies Used

### Backend
- Python 3.13+
- FastAPI
- OpenAI API
- SQLAlchemy
- Uvicorn (ASGI server)
- Clerk SDK for Python

### Frontend
- React 19
- Vite
- React Router
- Clerk for React

## Setup Instructions

### Backend Setup

1. Navigate to the backend directory:
   ```
   cd backend
   ```

2. Create a virtual environment:
   ```
   python -m venv .venv
   ```

3. Activate the virtual environment:
   - Windows: `.venv\Scripts\activate`
   - Unix/MacOS: `source .venv/bin/activate`

4. Install dependencies:
   ```
   pip install -e .
   ```

5. Create a `.env` file with the following variables:
   ```
   CLERK_SECRET_KEY=your_clerk_secret_key
   OPENAI_API_KEY=your_openai_api_key
   ```

6. Run the server:
   ```
   python server.py
   ```

### Frontend Setup

1. Navigate to the frontend directory:
   ```
   cd frontend
   ```

2. Install dependencies:
   ```
   npm install
   ```

3. Create a `.env` file with your Clerk public key:
   ```
   VITE_CLERK_PUBLISHABLE_KEY=your_clerk_publishable_key
   ```

4. Start the development server:
   ```
   npm run dev
   ```

## Usage

Once both the backend and frontend servers are running:

1. Access the frontend application at `http://localhost:5173` (or the port specified by Vite)
2. Sign up or log in using the authentication page
3. Generate new security challenges from the main page
4. View your challenge history in the history section

## Development Status

This project is currently in early development. Many features are still being implemented, and the application structure may change significantly.

