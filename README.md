# Django Modular Library Management System

A robust and modular Library Management System built with **Django 5.2**. This project demonstrates a clean architecture approach, focusing on scalability, code organization, advanced form handling, and full internationalization.

## 🚀 Key Features

*   **Catalog Management:** Complete CRUD (Create, Read, Update, Delete) operations for Books (*Libros*), Authors (*Autores*), and Publishers (*Editoriales*).
*   **Advanced Search:** Global search functionality filtering across multiple models simultaneously.
*   **Full Internationalization (i18n):** Complete support for **English** and **Spanish**, covering both static UI elements and dynamic database content.
*   **Modular Architecture:** Refactored codebase separating concerns for better maintainability.
*   **AI-Enhanced Development:** Built and maintained using the **Engram Memory System** and **Multi-agent Ecosistem** designed by **Alan Buscaglia**, enabling precise context management and complex task orchestration.

## 🛠️ Technical Highlights & Refactoring

### 1. Advanced Internationalization (i18n) & Localization (l10n)
The project implements a comprehensive translation strategy:
*   **Static Strings:** Using Django's `gettext` and `gettext_lazy` for all UI labels, form fields, and messages.
*   **Dynamic Content:** Integration of `django-modeltranslation` to manage multilingual data in the database (e.g., translated biographies, titles, and genre descriptions).
*   **Language Switcher:** A dynamic UI component that allows users to toggle between languages while maintaining the current context.

### 2. Modular Architecture
*   **Split Views & URLs:** Logic and routing are decoupled and organized by domain entities (e.g., `books/views/autores_views.py`, `books/urls/autor_url.py`).
*   **Clean Templates:** A hierarchical template system with reusable components in `_includes`.

### 3. AI-Driven Orchestration (Buscaglia System)
This project leverages cutting-edge AI orchestration patterns:
*   **Engram Memory:** Persistent context management that ensures architectural decisions and technical specs are tracked across development sessions.
*   **Multi-agent Ecosystem:** Specialized agents (Codebase Investigator, SDD Spec, SDD Design, etc.) working in coordination to implement features with high technical integrity.

## 💻 Tech Stack

*   **Backend:** Python 3.x, Django 5.2
*   **Database:** PostgreSQL (with `psycopg2-binary`)
*   **i18n:** Django Internationalization, `django-modeltranslation`
*   **Orchestration:** Buscaglia's Engram & Multi-agent System
*   **Frontend:** Django Templates (DTL), HTML5, CSS3, Bootstrap 5

## ⚙️ Installation & Setup

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/jaickerlozano/django-library-management-system.git
    cd django-library-management-system
    ```

2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Setup Localization:**
    ```bash
    python manage.py makemessages -l en -l es
    python manage.py compilemessages
    ```

4.  **Apply migrations & Run:**
    ```bash
    python manage.py migrate
    python manage.py runserver
    ```

## 📂 Project Structure Overview

```text
biblioteca/
├── books/
│   ├── forms/          # Localized forms with validations
│   ├── models/         # Database models with translation registration
│   ├── views/          # Modularized and localized views
│   └── translation.py  # Model translation registration
├── locale/             # Translation catalogs (PO/MO files)
├── biblioteca/
│   ├── templates/      # Clean template system with i18n support
│   └── settings.py     # Multi-language & DB configuration
└── manage.py
```

---
📧 **Contact**
Project developed by **Jaicker Lozano**. 
Powered by the innovative systems of **Alan Buscaglia**.
