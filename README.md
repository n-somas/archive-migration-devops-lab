# Archive Migration DevOps Lab

A small learning project for FastAPI, Docker and basic DevOps workflows.

The project simulates a simple archive migration service. It currently provides a FastAPI application with sample document metadata, a health check endpoint, a pytest test and a Docker setup.

## Features

- FastAPI web application
- Health check endpoint
- Sample document metadata endpoint
- Automated test with pytest
- Dockerfile for containerizing the application
- Docker Compose setup for local container execution

## Tech Stack

- Python 3.12
- FastAPI
- Uvicorn
- Pytest
- Docker
- Docker Compose

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | / | Basic service message |
| GET | /health | Application health check |
| GET | /documents | Sample document metadata |
| GET | /docs | FastAPI documentation |

## Local Setup

Create and activate the virtual environment:

    python -m venv .venv
    .\.venv\Scripts\Activate.ps1

Install dependencies:

    pip install -r requirements.txt

Start the application locally:

    uvicorn app.main:app --reload

Open the API documentation:

    http://127.0.0.1:8000/docs

## Docker Setup

Build and start the application with Docker Compose:

    docker compose up --build

Open the API documentation:

    http://localhost:8000/docs

Stop the container:

    docker compose down

## Tests

Run the tests:

    pytest

Expected result:

    1 passed

## Current Status

The application currently runs locally and inside a Docker container.

Implemented:

- FastAPI application
- Health check endpoint
- Sample document endpoint
- Pytest test
- Dockerfile
- Docker Compose setup

## Next Steps

- Add PostgreSQL with Docker Compose
- Store document metadata in the database
- Add basic CRUD endpoints
- Add GitHub Actions for automated tests

## Note

This is a learning project. It uses sample data only and does not contain real customer data.
