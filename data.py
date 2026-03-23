import json

def load_jobs(filename="jobs.json"):
    try:
        with open(filename, "r") as f:
            jobs = json.load(f)
            if not isinstance(jobs, list):
                return []
            return jobs
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []

def save_jobs(jobs, filename="jobs.json"):
    try:
        with open(filename, "w") as f:
            json.dump(jobs, f, indent=4)
        print("Jobs saved successfully.")
    except Exception as e:
        print(f"Error saving jobs: {e}")


