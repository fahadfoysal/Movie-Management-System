

## Requirements

- **Python**: 3.x
- **Django**: 5.x
- **SQLite**: (default database for Django projects)

## Setup Instructions

1. **Clone the repository:**

    ```bash
    git clone https://github.com/fahadfoysal/Movie-Management-System.git
    cd Movie-Management-system
    ```

2. **Create a virtual environment:**

    ```bash
    python -m venv venv
    ```

3. **Activate the virtual environment:**

    - **Windows:**

        ```bash
        venv\Scripts\activate
        ```

    - **macOS/Linux:**

        ```bash
        source venv/bin/activate
        ```

4. **Install the required packages:**

    ```bash
    pip install -r requirements.txt
    ```

5. **Run migrations to set up the database:**

    ```bash
    python manage.py migrate
    ```

6. **Create a superuser (optional, for accessing the admin interface):**

    ```bash
    python manage.py createsuperuser
    ```

7. **Run the development server:**

    ```bash
    python manage.py runserver
    ```

8. **Access the application in your web browser:**

    Open your browser and navigate to: [http://localhost:8000](http://localhost:8000)
