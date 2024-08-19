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
  ![image](https://github.com/user-attachments/assets/c2407a2e-9440-40cf-ac07-99c6c0033e37)


## Use Cases using Swagger

### 1. **Upload Image**
Upload a new image for processing.

**Request Example :**
  ![image](https://github.com/user-attachments/assets/3e72385d-aa88-4e07-89d7-b7c033a63ebb)


**Response  Example :**
  ![image](https://github.com/user-attachments/assets/b16259aa-cddf-4bcd-90a3-58928657b647)



### 2. **GET Images - /images/**
Retrieve a list of all uploaded images.

**Response  Example :**
  ![image](https://github.com/user-attachments/assets/9ee0fed2-af53-4f7b-aa56-58fc7a596e33)


### 3. **GET Image Detail - /images/{id}/**
Retrieve a specific image by its ID.

**Request Example :**
  ![image](https://github.com/user-attachments/assets/7faf351b-a523-42c3-bc97-38a0372eca36)


**Response  Example :**
  ![image](https://github.com/user-attachments/assets/d1d9bb24-0d80-4791-a429-a1e9fbe9a7de)

### **Before and after image**

**Before:**
  ![image](https://github.com/user-attachments/assets/e5928d35-d6f1-45c4-a5f3-b5ee0d47d2d8)

**After:**
  ![image](https://github.com/user-attachments/assets/b75c699d-fb26-4ae2-a6b0-d0d48358e301)


## Running Tests
- docker-compose exec django pytest

## Contact
- For any inquiries, please contact Nicolas Hurtado at nicolashurtado0712@gmail.com

***Nicolas Hurtado C***
