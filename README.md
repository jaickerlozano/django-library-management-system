# Django Modular Library Management System

A robust and modular Library Management System built with **Django 3.2**. This project demonstrates a clean architecture approach, focusing on scalability, code organization, and advanced form handling.

## 🚀 Key Features

*   **Catalog Management:** Complete CRUD (Create, Read, Update, Delete) operations for Books (*Libros*), Authors (*Autores*), and Publishers (*Editoriales*).
*   **Advanced Search:** Global search functionality filtering across multiple models simultaneously.
*   **Robust Validation:** Custom business logic implemented directly in Django Forms.
*   **Modular Architecture:** Refactored codebase separating concerns for better maintainability.

## 🛠️ Technical Highlights & Refactoring

This project goes beyond the basics by implementing professional coding standards and architectural patterns:

### 1. Modular Architecture (Refactoring)
Instead of a monolithic `views.py` or `urls.py`, the application has been refactored for scalability:
*   **Split Views:** Logic is separated into specific modules (e.g., `books/views/autor_views.py`, `books/views/libro_views.py`) rather than one giant file.
*   **Organized URLs:** URL configurations are decoupled and organized by domain entities within `books/urls/`.
*   **Template Structure:** A clean, inherited template system using `_includes` for components like navigation.

### 2. Advanced Form Handling
Data integrity is ensured through Django's `ModelForm` and `Form` classes with custom validations:
*   **Custom Validators:** Implementation of `clean_<field>` methods to enforce business rules (e.g., minimum character length, restricted words in emails).
*   **Widget Customization:** Enhanced UX using specific widgets (e.g., `SelectDateWidget` for publication dates).
*   **Feedback Loops:** Clear error messaging passed from the backend to the template layer.

## 💻 Tech Stack

*   **Backend:** Python 3.x, Django 3.2
*   **Database:** SQLite (Development)
*   **Utilities:** Django Debug Toolbar, Django Extensions
*   **Frontend:** Django Templates (DTL), HTML5, CSS3

## ⚙️ Installation & Setup

Follow these steps to run the project locally:

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/tu-usuario/django-modular-library.git
    cd django-modular-library
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    python -m venv env
    # Windows
    .\env\Scripts\activate
    # macOS/Linux
    source env/bin/activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Apply migrations:**
    ```bash
    python manage.py migrate
    ```

5.  **Run the development server:**
    ```bash
    python manage.py runserver
    ```

## 📂 Project Structure Overview

```text
biblioteca/
├── books/
│   ├── forms/          # Custom forms with validations
│   ├── models/         # Database models
│   ├── views/          # Modularized views (Autor, Libro)
│   └── urls/           # Decoupled URL configurations
├── templates/
│   ├── _includes/      # Reusable components (Navbar, etc.)
│   ├── autores/        # Author-specific templates
│   └── libros/         # Book-specific templates
└── manage.py

📧 Contact
Project developed by Jaicker Lozano. 
Feel free to reach out for any inquiries regarding Django development.