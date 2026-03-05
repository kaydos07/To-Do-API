# To-Do API

A simple Django REST Framework API for managing a to-do list. This repository provides endpoints for creating, reading, updating, and deleting to-do items.

## 🚀 Features

- CRUD operations for task management
- Built with Django and Django REST Framework (DRF)
- SQLite database for easy setup
- Modular app structure under `api` folder
- Includes basic tests for models and API views

## 🔧 Setup & Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url> "To-Do API"
   cd "To-Do API"/to_do_api
   ```

2. **Create and activate a virtual environment**
   ```bash
   python -m venv to_do_api-env
   # Windows PowerShell
   .\to_do_api-env\Scripts\Activate.ps1
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables (optional)**
   The project uses `python-dotenv` to load environment variables from a `.env` file. At minimum, you can set:
   ```env
   DJANGO_SECRET_KEY=your_secret_key
   DEBUG=True
   ```

5. **Apply migrations**
   ```bash
   python manage.py migrate
   ```

6. **Run the development server**
   ```bash
   python manage.py runserver
   ```
   The API will be available at `http://127.0.0.1:8000/`.

## 🧠 Project Structure

```
to_do_api/             # Django project root
  manage.py            # Django CLI
  db.sqlite3           # SQLite database file
  to_do_api/           # Project settings and urls
    settings.py
    urls.py
    wsgi.py
    asgi.py
  api/                 # Application code
    models.py          # Task model
    serializer.py      # DRF serializers
    views.py           # API views
    urls.py            # App-level routes
    tests.py           # Unit and API tests
```

## 📦 API Endpoints

| Method | Endpoint        | Description                       |
|--------|-----------------|-----------------------------------|
| GET    | `/tasks/`       | List all tasks                    |
| POST   | `/tasks/`       | Create a new task                 |
| GET    | `/tasks/{id}/`  | Retrieve a specific task          |
| PUT    | `/tasks/{id}/`  | Update a task                     |
| DELETE | `/tasks/{id}/`  | Delete a task                     |

> Note: Endpoint paths assume the root URL configuration includes the `api` app under `''`.

## ✅ Running Tests

Use Django's test runner:
```bash
python manage.py test
```

## 📄 License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## 💡 Contributions

Feel free to open issues or submit pull requests for improvements! Check the issue tracker for existing tasks or feature requests.

---

Happy coding! 📝
