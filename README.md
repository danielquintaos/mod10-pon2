
This project includes a Flask API for managing to-dos and a Flutter mobile application that consumes the API. It supports CRUD operations—creating, reading, updating, and deleting to-do items.

---

## Folder Structure:

```
mod10-pon2/
│
├── api/
│   ├── __init__.py
│   ├── app.py          # Main application file, updated to handle to-dos
│   └── resources/      # Resources for Flask API
│       └── __init__.py
│
├── tests/
│   └── test_api.py     # Tests for the API
│
├── docs/
│   ├── openapi.yaml    # API documentation
│   └── insomnia.json   # Insomnia collection for API testing
│
├── mobile_app/         # Flutter application
│   ├── lib/
│   ├── test/
│   └── pubspec.yaml
│
├── static/
│   └── swagger/        # Swagger UI files
│
├── templates/
│   └── swagger.html    # HTML file to serve Swagger UI
│
├── Dockerfile
├── docker-compose.yml
│
├── requirements.txt
└── README.md           # This documentation
```

---

## Getting Started:

### Prerequisites:

- Python 3.9+
- Docker and Docker Compose
- Flutter SDK
- Android SDK or an Android Emulator

### Installation:

1. **Clone the Repository**

   Start by cloning the repository to your local machine:
   ```
   git clone https://github.com/danielquintaos/mod10-pon2.git
   cd mod10-pon2
   ```

2. **API Setup**

   Use Docker Compose to build and run the containerized application:
   ```
   docker-compose up --build
   ```

   This command builds the Docker image if it hasn't been built and starts the service defined in `docker-compose.yml`. The `--build` option ensures that the Docker image is rebuilt with any new changes.

## Using the API:

1. **Accessing Swagger UI**

   Once the Docker container is running, you can access Swagger UI by navigating to:
   
   [http://localhost:5000/docs](http://localhost:5000/docs)

   This page will display the live API documentation, where you can view detailed information about the API endpoints and try them out in real-time.

2. **Testing with Insomnia**

   Import the `insomnia.json` or `insomnia_get.json` file located in the `docs/` directory into Insomnia to test the API endpoints.

## Mobile App Setup:

1. **Run the Flutter App**

   Navigate to the `mobile_app` directory within the project:
   ```
   cd mobile_app
   ```

   Make sure an Android emulator is running or an Android device is connected to your computer, then execute:
   ```
   flutter run
   ```

   This command compiles the Flutter app and installs it on the connected Android device or emulator.
