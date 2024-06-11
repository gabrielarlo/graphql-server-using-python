# GraphQL Server

This project sets up a GraphQL server using Python with FastAPI, Strawberry, SQLAlchemy, and MySQL. The server is managed using Poetry for dependency management.

## Prerequisites

- Python 3.8 or higher
- Poetry
- MySQL

## Installation

### Clone the Repository

```bash
git clone https://github.com/gabrielarlo/graphql-server-using-python.git
cd graphql-server-using-python
```

### Set Up Environment Variables

Create a `.env` file in the root directory with the following content:

```env
DATABASE_USER=username
DATABASE_PASSWORD=password@123
DATABASE_HOST=localhost
DATABASE_NAME=dbname
PORT=8000
```

Replace `username`, `password@123`, `localhost`, and `dbname` with your actual database credentials.

### Install Dependencies

Run the following command to install the required dependencies:

```bash
poetry install
```

## Database Setup

### Create Database Tables

Run the following command to create the necessary database tables:

```bash
poetry run python create_tables.py
```

## Running the Server

### Using Uvicorn CLI (Recommended for Development)

For development purposes, where hot-reloading is needed, run the server using the Uvicorn CLI:

```bash
poetry run uvicorn server:app --host 0.0.0.0 --port 8000 --reload
```

### Using `main.py` (Recommended for Production)

For production or environments where hot-reloading is not needed, you can run the server using the `main.py` file:

```bash
poetry run python main.py
```

## Project Structure

```
graphql-server
├── pyproject.toml
├── poetry.lock
├── .env
├── main.py
├── server.py
├── database.py
├── models.py
├── m_types.py
└── create_tables.py
```

## Important Files

- **`pyproject.toml`**: Contains project metadata and dependencies.
- **`.env`**: Contains environment variables for database credentials and server port.
- **`main.py`**: Entry point for running the server without hot-reloading.
- **`server.py`**: Sets up FastAPI and Strawberry for the GraphQL server.
- **`database.py`**: Configures the database connection using SQLAlchemy.
- **`models.py`**: Defines SQLAlchemy models.
- **`m_types.py`**: Defines GraphQL types using Strawberry.
- **`create_tables.py`**: Script to create database tables.

## Notes

- Ensure that your MySQL server is running and accessible with the credentials provided in the `.env` file.
- Adjust the `PORT` in the `.env` file as needed for your setup.
- For production deployments, consider using a process manager like `gunicorn` along with `uvicorn` for better performance and reliability.

---

This setup ensures that your GraphQL server is correctly configured with compatible dependencies, sets up the GraphQL server with FastAPI, and loads the port configuration from the `.env` file. Follow the instructions to install dependencies, create tables, and run the server. If you encounter any issues, ensure all dependencies are correctly installed and versions are compatible.