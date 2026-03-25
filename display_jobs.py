import data
# import manage_jobs

def list_jobs():
    while True:
        jobs_data = data.load_jobs()

        if not jobs_data:
            print("No jobs to display.")
            break
                    
        try:
            print("\nJobs Summery:")
            define = f"Jobs Summery:"
            print("=" * len(define))
            print()
            for idx, job in enumerate(jobs_data, start=1):
                print(f"{idx}. Job name: {job['job_name']}, Owner: {job['owner']}, Description: {job['description']}")
            input("\nPress Enter to return back to the main menu...")
            break
        
        except Exception as e:
            print(e)
                 

        # ##### Exit #####
        # elif choice == "6":
        #     print("Exiting...")
        #     break

        # ##### Invalid choice #####
        # else:
        #     print("Invalid menu option. Please choose a number between 1-6.")