
def add_job(job_number, job_name, owner, description):
    return {
        "job_number": job_number,
        "job_name": job_name,
        "owner": owner,
        "description": description,
        "path": f"/jenkins_home/jobs/{job_name}"
    }

def delete_job(jobs, job_name):
    updated_jobs = []
    found = False
    for job in jobs:
        if job["job_name"] != job_name:
            updated_jobs.append(job)
        else:
            found = True
    if not found:
        print(f"Job '{job_name}' not found.")
    return updated_jobs

def update_job(jobs, job_name, new_owner=None, new_description=None):
    """
    Update owner and/or description of a job in the jobs list.
    Returns the updated list.
    """
    found = False
    for job in jobs:
        if job["job_name"] == job_name:
            if new_owner:
                job["owner"] = new_owner
            if new_description:
                job["description"] = new_description
            found = True
            break  # job names are unique, no need to continue
    if not found:
        print(f"Job '{job_name}' not found.")
    return jobs

