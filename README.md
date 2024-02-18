# Django Test Project

## Introduction

Django Test Project is a sample Django project showcasing the use of Docker for containerized development environments.

## Features

- Dockerized development environment
- Quick setup for Django projects
- Demonstrates best practices for using Docker with Django

## Requirements

- Docker
- Docker Compose

## Installation

Follow these steps to set up the Django Test Project on your local machine:

1. Clone the repository:

    ```bash
    git clone https://github.com/priyabrata-sahoo/django_test_project.git
    cd django_test_project
    ```

2. Build and run the Docker containers:

    ```bash
    docker-compose up --build -d
    ```

    This command will build the Docker image and start the containers in detached mode.

3. Access the Django application:

    Open your web browser and go to [http://localhost:8000](http://localhost:8000) to see the Django Test Project running.

## Docker Compose Commands

- Check the status of Docker containers:

    ```bash
    docker-compose ps
    ```

- Access the shell of a running container:

    ```bash
    docker exec -it <container_name> /bin/bash
    ```

    Replace `<container_name>` with the actual name or ID of your running container.

## Contributing

If you would like to contribute to this project, please follow these guidelines:

1. Fork the repository.
2. Create a new branch for your feature or bug fix: `git checkout -b feature-name`.
3. Make your changes and commit them: `git commit -m "Description of your changes"`.
4. Push your changes to your fork: `git push origin feature-name`.
5. Open a pull request on the original repository.

## License

This project is licensed under the [Apache License 2.0](LICENSE).
