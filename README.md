# Jenkins Job Manager

A Python command-line application for managing Jenkins jobs. This application allows users to create, update, delete, and display Jenkins jobs in a user-friendly menu-driven interface.

## Features

- ✅ **Add Jobs** - Create new Jenkins jobs with details (job name, owner, description)
- ✅ **Delete Jobs** - Remove existing jobs with confirmation
- ✅ **Update Jobs** - Modify job details
- ✅ **Display Jobs** - View all existing jobs
- ✅ **Persistent Storage** - All job data is automatically saved to `jobs.json`

## Requirements

- Python 3.6 or higher
- No external dependencies required (uses only Python standard library)

## Installation

1. Clone or download the project
2. Navigate to the project directory:
   ```bash
   cd Python-Final-Lab
   ```

## Usage

### Starting the Application

Run the main program:
```bash
python main.py
```

This will display the main menu with the following options:
```
Jenkins Job Manager Main Menu:
============================================

1. Add jobs
2. Delete jobs
3. Update jobs
4. Load demi data, Comming soon
5. Display jobs
6. Exit the app
```

### ⚠️ Important: Creating Jobs First

**You MUST create at least one job before you can use other features like delete or update.**

To get started:
1. Select option `1 - Add jobs`
2. Enter how many jobs you want to create
3. Provide job details:
   - Job name
   - Owner
   - Description
4. Jobs will be saved automatically to `jobs.json`

Once you have created jobs, you can:
- Update them (option 3)
- Delete them (option 2)
- View them (option 5)

### Data Storage

All job data is automatically saved to the **`jobs.json`** file in the project directory. This file contains:
- Job name
- Owner information
- Job description
- Jenkins path (auto-generated as `/jenkins_home/jobs/{job_name}`)

**Example jobs.json format:**
```json
[
    {
        "job_name": "Build Master",
        "owner": "DevOps Team",
        "description": "Builds the main branch",
        "path": "/jenkins_home/jobs/Build Master"
    },
    {
        "job_name": "Deploy Production",
        "owner": "Release Manager",
        "description": "Deploys to production environment",
        "path": "/jenkins_home/jobs/Deploy Production"
    }
]
```

## Project Structure

```
Python-Final-Lab/
├── main.py              # Main entry point and application loop
├── main_menu.py         # Menu display and user input
├── data.py              # JSON file I/O operations
├── manage_jobs.py       # Business logic for job operations
├── add_jobs.py          # Add jobs functionality
├── delete_jobs.py       # Delete jobs functionality
├── update_jobs.py       # Update jobs functionality
├── display_jobs.py      # Display jobs functionality
├── jobs.json            # Data persistence file (auto-created)
└── README.md            # This file
```

## Menu Options Explained

| Option | Function | Requirement |
|--------|----------|-------------|
| 1 | Add jobs | None - start here first |
| 2 | Delete jobs | At least one job must exist |
| 3 | Update jobs | At least one job must exist |
| 4 | Load demi data | Coming soon |
| 5 | Display jobs | At least one job must exist |
| 6 | Exit the app | None |

## Workflow Example

1. **Start the app:**
   ```bash
   python main.py
   ```

2. **Create your first job (Option 1):**
   - How many jobs? `1`
   - Job name: `Test Job`
   - Owner: `DevOps`
   - Description: `My first test job`
   - ✅ Job saved to jobs.json

3. **Display jobs (Option 5):**
   - View your newly created job

4. **Update job (Option 3):**
   - Modify job details

5. **Delete job (Option 2):**
   - Remove the job with confirmation

6. **Exit (Option 6):**
   - Close the application

## Notes

- All user inputs are validated for proper data types
- Job deletion requires confirmation to prevent accidental removal
- The application will automatically create `jobs.json` if it doesn't exist
- Data persists between sessions - all jobs are saved in `jobs.json`
- Invalid menu selections will prompt you to enter a valid option

## Troubleshooting

**Issue:** "No jobs to delete, going back to main menu"
- **Solution:** You need to create at least one job first. Use option 1 to add jobs.

**Issue:** "Error: Invalid input"
- **Solution:** Make sure you're entering valid numbers when prompted for job selection.

**Issue:** jobs.json is missing
- **Solution:** Create the first job using option 1. The file will be automatically created.

## License

This is an educational project for learning Python fundamentals.
