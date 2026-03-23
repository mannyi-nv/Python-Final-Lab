import main_menu
import manage_jobs
import data

while True:
    try:
        # Show menu
        choice = main_menu.menu()

        # --- Add Jobs ---
        if choice == "1":
            # Load existing jobs first
            jobs_data = data.load_jobs()

            try:
                jobs_counter = int(input("Please enter how many jobs to create: "))
            except ValueError:
                print("Please enter a valid number")
                continue

            for i in range(jobs_counter):
                job_number = len(jobs_data) + 1  # continue numbering
                job_name = input(f"Please enter job name for job number {i + 1}: ")
                owner = input(f"Enter owner for: {job_name} ")
                description = input(f"Enter description for: {job_name} ")

                new_job = manage_jobs.add_job(job_number, job_name, owner, description)
                jobs_data.append(new_job)

            # Save all jobs
            data.save_jobs(jobs_data)
            print(f"\n{jobs_counter} job(s) added successfully.")
            input("\nPress Enter to return to the main menu...")


            ###############################################################

        # --- Delete Jobs ---
        elif choice == "2":
            jobs_data = data.load_jobs()

            if not jobs_data:
                print("No jobs to delete.")
                continue

            while True:  # <--- Start a retry loop here
                print("\n--- Existing Jobs ---")
                for idx, job in enumerate(jobs_data, start=1):
                    print(f"{idx}. {job['job_name']}")
                
                print("0. Cancel and return to main menu")

                try:
                    user_input = input("\nEnter the number of the job to delete: ")
                    job_choice = int(user_input)

                    if job_choice == 0:
                        print("Delete cancelled.")
                        break  # Exit the retry loop to go back to main menu

                    if 1 <= job_choice <= len(jobs_data):
                        # SUCCESS: Valid selection made
                        job_to_delete = jobs_data[job_choice - 1]["job_name"]
                        conf = "yes".lower
                        user_conf = input(f"Please type 'YES / NO' to confirm: ").lower()
                        if "yes" in user_conf:
                            # Perform the actual deletion
                            jobs_data = manage_jobs.delete_job(jobs_data, job_to_delete)
                            data.save_jobs(jobs_data)
                            print(f"Job '{job_to_delete}' deleted successfully, returning to main menu")
                            break
                        else:
                            print(f"Delete has been cancled by the user")
                            print(f"Returning back to the main menu")
                            break
                        
                    else:
                        print(f"!!! Error: Please enter a number between 1 and {len(jobs_data)}.")

                except ValueError:
                    print("!!! Error: Invalid input. Please enter a valid number.")


            ##########################################################
        # --- View Job ---
        elif choice == "3":
            jobs_data = data.load_jobs()

            if not jobs_data:
                print("No jobs to update.")
                continue
            
            while True:  # <--- Start a retry loop here

                print("\n--- Existing Jobs ---")
                for idx, job in enumerate(jobs_data, start=1):
                    print(f"{idx}. {job['job_name']} (Owner: {job['owner']}, Description: {job['description']})")

                try:
                    job_choice = int(input("Enter the number of the job to update: "))
                    
                    if 1 <= job_choice <= len(jobs_data):
                
                        job_to_update = jobs_data[job_choice - 1]["job_name"]

                        new_owner = input("Enter new owner (leave blank to keep current): ").strip()
                        new_description = input("Enter new description (leave blank to keep current): ").strip()

                        jobs_data = manage_jobs.update_job(
                            jobs_data, job_to_update,
                            new_owner if new_owner else None,
                            new_description if new_description else None
                        )

                        data.save_jobs(jobs_data)
                        print(f"Job '{job_to_update}' updated successfully.")
                        input("\nPress Enter to return to the main menu...")
                        break
                        
                    else:
                        print(f"!!! Error: Please enter a number between 1 and {len(jobs_data)}.")
                    
                    
                

                except Exception as e:
                    print(f" invalid choice:------------ {e}")


            ##########################################################
        elif choice == "5":  # Job display
                    jobs_data = data.load_jobs()

                    if not jobs_data:
                        print("No jobs to display.")
                        continue
                    
                    print("\n--- Jobs Summery ---")
                    for idx, job in enumerate(jobs_data, start=1):
                        print(f"{idx}. Job name: {job['job_name']}, Owner: {job['owner']}, Description: {job['description']}")
                        
                    input("\nPress Enter to return to the main menu...")




                   

        # --- Exit ---
        elif choice == "6":
            print("Exiting...")
            break

                # --- Invalid choice ---
        else:
            print("Invalid menu option. Please choose 1-6.")


    except Exception as e:
        print(f" Unexpected error:------------ {e}")