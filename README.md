# 🛠️ Jenkins Job Manager (CLI)

A simple **command-line application** written in Python to manage Jenkins jobs locally using a JSON file.

This tool allows you to **create, update, delete, and view jobs** in a structured and user-friendly way.

---

## 🚀 Features

* ➕ Add new jobs
* 🗑️ Delete existing jobs (with confirmation)
* ✏️ Update job details (owner / description)
* 📄 Display all jobs in a clean summary view
* 💾 Persistent storage using `jobs.json`
* 🔁 Input validation with retry loops
* 🧠 Modular design (separation of concerns)

---

## 📁 Project Structure

```
.
├── main.py              # Main application entry point
├── main_menu.py         # Menu display logic
├── manage_jobs.py       # Job operations (add, delete, update)
├── data.py              # JSON read/write operations
├── jobs.json            # Data storage file
```

---

## ⚙️ How It Works

* `main.py` controls the application flow and user interaction
* `main_menu.py` handles menu display
* `manage_jobs.py` contains all job-related logic
* `data.py` handles reading/writing to the JSON file

---

## ▶️ How to Run

1. Make sure you have Python installed (Python 3.8+ recommended)

2. Run the application:

```bash
python main.py
```

---

## 📋 Menu Options

```
1. Add jobs
2. Delete jobs
3. Update jobs
4. Load demo data (coming soon)
5. Display jobs
6. Exit
```

---

## 🧾 Example Job Structure

Each job is stored as a JSON object:

```json
{
    "job_number": 1,
    "job_name": "qa-tests-regression-1",
    "owner": "Manny",
    "description": "Regression tests",
    "path": "/jenkins_home/jobs/qa-tests-regression-1"
}
```

---

## 🧠 Design Principles

* Separation of concerns:

  * Data handling (`data.py`)
  * Business logic (`manage_jobs.py`)
  * UI interaction (`main.py`)
* Defensive programming (input validation, error handling)
* Simple and extendable architecture

---

## 🔮 Future Improvements

* 🔍 Search and filter jobs
* 📊 Better formatted output (table view)
* 📦 Export to CSV / reports
* 🌐 Integration with real Jenkins API
* 🧪 Unit tests

---

## 🙌 Author

Built as a learning project to practice:

* Python fundamentals
* Modular design
* CLI application development

---

## 📌 Notes

* If `jobs.json` does not exist, it will be created automatically
* The application safely handles empty or corrupted JSON files

---

## ⭐️ If you like this project

Give it a ⭐ on GitHub and feel free to contribute!

