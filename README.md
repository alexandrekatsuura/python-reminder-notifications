# 📝 Reminder with Desktop Notifications

![GitHub repo size](https://img.shields.io/github/repo-size/alexandrekatsuura/python-reminder-notifications?style=for-the-badge)
![GitHub language count](https://img.shields.io/github/languages/count/alexandrekatsuura/python-reminder-notifications?style=for-the-badge)
![GitHub forks](https://img.shields.io/github/forks/alexandrekatsuura/python-reminder-notifications?style=for-the-badge)
![Bitbucket open issues](https://img.shields.io/bitbucket/issues/alexandrekatsuura/python-reminder-notifications?style=for-the-badge)
![Bitbucket open pull requests](https://img.shields.io/bitbucket/pr-raw/alexandrekatsuura/python-reminder-notifications?style=for-the-badge)

## 📚 Academic Use Disclaimer

> ⚠️ This is an academic project created for learning purposes only.
> It is not intended for production use.

## ℹ️ About

This project is a Python application designed to create and manage reminders with desktop notifications. It aims to provide a simple yet effective way to keep track of important tasks and events.

## 🚀 Features

*   **Reminder Management**: Add, view, and delete reminders.
*   **Desktop Notifications**: Receive timely notifications for upcoming reminders.
*   **User-friendly Interface**: An intuitive graphical user interface for easy interaction.
*   **Cross-platform Compatibility**: Designed to work on various operating systems.
*   **Unit Testing**: Comprehensive tests to ensure reliability.
*   **Clean Project Structure**: Modular organization for clarity, maintainability, and scalability.

## 🛠️ Technologies Used

*   **Python 3.x**
*   **Tkinter**: For the graphical user interface.
*   **Plyer**: For cross-platform desktop notifications.
*   **`pytest`**: Framework used to create and run unit tests.

## ⚙️ How to Run the Project

### Prerequisites

Ensure that Python 3.x is installed on your machine.

### Installation

1.  Clone this repository:

    ```bash
    git clone https://github.com/alexandrekatsuura/python-reminder-notifications
    cd python-reminder-notifications
    ```

2.  (Optional but recommended) Create and activate a virtual environment:

    ```bash
    python -m venv .venv
    source .venv/bin/activate      # On Linux/macOS
    # .venv\Scripts\activate       # On Windows
    ```

3.  Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

### Usage

To run the program, use the following command:

```bash
python src/main.py
```

The application will launch, allowing you to manage your reminders.

## ✅ Running the Tests

To run the unit tests, from the project root directory:

```bash
pytest -v
```

This will execute all test cases located in the `tests/` directory, ensuring the reminder and notification logic is working correctly.

## 📁 Project Structure

```bash
python-reminder-notifications/
├── src/
│   ├── main.py             # Main application entry point and GUI logic
│   └── reminder_service.py # Core logic for reminder management and notification scheduling
├── tests/
│   └── test_reminders.py   # Unit tests for the reminder service
├── .gitignore              # Specifies intentionally untracked files to ignore by Git
├── README.md               # Project documentation and setup instructions
└── requirements.txt        # Lists project dependencies
```

## 📄 License

This project is licensed under the [MIT License](LICENSE).




