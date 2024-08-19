# Image Processor API

## Description

The **Image Processor API** is a Django-based application that allows users to upload images and process them asynchronously. The processing includes applying transformations, such as converting images to grayscale. The application is containerized using Docker and orchestrated with Docker Compose, ensuring a seamless deployment process.

## Features

- **Image Upload**: Users can upload an image for processing.
- **Asynchronous Processing**: Images are processed asynchronously using Celery with Redis as the message broker.
- **API Documentation**: Interactive API documentation available via Swagger.

## Tech Stack

- **Django**: Web framework used to build the application.
- **Django Rest Framework**: For building the RESTful API.
- **Celery**: For handling asynchronous tasks.
- **Redis**: As a message broker for Celery.
- **PostgreSQL**: As the database for storing image data.
- **Docker & Docker Compose**: For containerization and orchestration.

## Getting Started

### Prerequisites

Make sure you have Docker and Docker Compose installed on your machine:

- [Docker Installation Guide](https://docs.docker.com/get-docker/)
- [Docker Compose Installation Guide](https://docs.docker.com/compose/install/)

### Build and run the Docker containers
- docker-compose up --build

### Access the application
- API Documentation: http://localhost:8000/swagger/
-

## Use Cases using Swagger

### 1. **Upload Image**
Upload a new image for processing.

**Request Example :**
-

**Response  Example :**
-


### 2. **GET Images - /images/**
Retrieve a list of all uploaded images.

**Request Example :**
-

**Response  Example :**
-

### 3. **GET Image Detail - /images/{id}/**
Retrieve a specific image by its ID.

**Request Example :**
-

**Response  Example :**
-

## Running Tests
- docker-compose exec django pytest

## Contact
- For any inquiries, please contact Nicolas Hurtado at nicolashurtado0712@gmail.com

***Nicolas Hurtado C***
