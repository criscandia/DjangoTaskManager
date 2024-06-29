# Task Manager

Task Manager is a simple web application that allows users to manage their tasks effectively. Built with Django and Django REST Framework, this application provides both a user-friendly interface and a comprehensive API.

## Table of Contents

- [Project Overview](#project-overview)
- [Installation](#installation)
- [Usage](#usage)
- [API Documentation](#api-documentation)
- [Contributing](#contributing)
- [License](#license)

## Project Overview

The Task Manager application enables users to create, edit, and delete tasks. It is designed with a focus on simplicity and ease of use. Users can manage tasks through a web interface or interact programmatically via a RESTful API. The application uses SQLite for data storage and is equipped with authentication features for secure access.

## Installation

To install and set up the Task Manager:

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/your-repository.git

python manage.py runserver
## Usage
Access the web application at http://localhost:8000/.
Use the Task List button to view all tasks.
Use the Create Task button to add new tasks.
API endpoints are available for integration with other applications.
API Documentation
The API provides endpoints for managing tasks and user authentication. Access the interactive API documentation at:

## Swagger Documentation
Key Endpoints:
Register a new user: POST /api/register/
Obtain authentication token: POST /api/token/
List tasks: GET /api/tasks/
Create a new task: POST /api/tasks/
Edit a task: PUT /api/tasks/{id}/
Delete a task: DELETE /api/tasks/{id}/
Contributing
Contributions are welcome! Please fork the repository and submit a pull request with your changes. Ensure that your code follows best practices and is well-documented.

License
This project is licensed under the MIT License - see the LICENSE file for details.
