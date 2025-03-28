
#Global variables
Available_number_of_workers=int()
project_details={}
Completed_project_details={}
Ongoing_project_details={}
On_hold_project_details={}
remaining_workers=0

#defining function for the update of remaining workers when there's a change in the number of workers in other define functions
def update_remaining_workers():
    global remaining_workers
    sum_of_workers = sum(inner_dict.get('number_of_workers', 0) for inner_dict in project_details.values())
    sum_of_workers_from_completed_projects = sum(inner_dict.get('number_of_workers', 0) for inner_dict in Completed_project_details.values())
    remaining_workers = Available_number_of_workers - sum_of_workers + sum_of_workers_from_completed_projects


#defining functions for a more organized and simple way of calling those functions when needed  

#defining function for the first choice menu
def Add_a_new_project():
    print('\n')
    print('\n')#leaving spaces 

    global Available_number_of_workers  #Calling in global variables into the defined function to make changes to the glabal variables inside a defined function
    global ongoing_projects             
    global Completed_projects
    global on_hold_projects
    global project_details
    global remaining_workers

    
    
#initailizing inputs into the choice menu 1
#While is used for the loop of the code so it reruns again    
    while True:
        print("                   Add a new project","\n")    
        try:
            project_code=int(input("Project code(Enter'0' to exit):- "))
        
#process for breaking of the code and return to the main menu when user inputs 0
            if project_code==0:  
                print("exiting")                                
                break            
            elif project_code in project_details:
                print("Project code already exists. Use update function to modify details.")
                return
        
#getting inputs from the user to save them into the directory and modify them if needed         
            client_name=str(input("Clients Name:- "))
            start_date=(input("Start date(dd/mm/yy):- "))
            expected_end_date=(input("Expected end date(dd/mm/yy):- "))
            number_of_workers=int(input("Number of workers:- "))
        
#breaking the code and returning to the main menu if the number of workers are not enough
            if number_of_workers>remaining_workers:
                print("Not enough available workers to assign to the project")
                print("Add more workers by choosing the 3rd choice in the main menu")
                print("exiting")
                return
            else:
                pass
            project_status=str(input("Project status (On hold/Ongoing/Completed) :- "))
        
#process for breaking the code if the user inputs any other values instead of the above given options
            if project_status==('Ongoing'):
                pass
            elif project_status==('Completed'):
                pass
            elif project_status==('On hold'):
                pass
            else:
                print("invalid statement")
                print("exiting to the main menu")
                return
            print("\n")
        
#saving the details into the dictionary called project_details and under that these details save under project code dictionary if the user inputs "Yes" else not saving and breaking the process to return to the main menu
            save=str(input("Do you want to save the project(Yes/No)? ")).lower()
        
            if save==("yes"):
                project_details[project_code] = {
                    "client_name": client_name,
                    "start_date": start_date,
                    "expected_end_date": expected_end_date,
                    "number_of_workers": number_of_workers,
                    "project_status": project_status
                   }
#adding details for the new dictionary called completed project details from the project_details dictionary when project status = completed
                for project_code, details in project_details.items():
                    if details["project_status"] == ("Completed"):
# Copy the project details if the condition above is met to Completed_project_details
                        Completed_project_details[project_code] = details
            

#adding details for the new dictionary called ongoing project details from the project_details dictionary when project status = completed
                for project_code, details in project_details.items():
                    if details["project_status"] == ("Ongoing"):
# Copy the project details if the condition above is met to Ongoing_project_details
                        Ongoing_project_details[project_code] = details
            
#adding details for the new dictionary called on hold project details from the project_details dictionary when project status = completed
                for project_code, details in project_details.items():
                    if details["project_status"] == ("On hold"):
# Copy the project details if the condition above is met to On_hold_project_details
                        On_hold_project_details[project_code] = details
                update_remaining_workers()
                print("Project has been successfully saved")
                

            else:
                print("project is not saved")
                
        except ValueError:
            print("Invalid Statement")
            
        
            
#defining the second choice menu and inputing details under it
def Remove_Completed_Project():
    print('\n')
    while True:
        try:
            global project_details
            global ongoing_projects
            global Completed_projects

            print("         Remove a completed project from existing projects","\n")
            project_code=int(input("Project Code:- "))
#Checking whether the project code number is in the project_details dictionary 
            if project_code not in project_details:
                print("Project code not found.")
                return
            print("\n")
        
        
            project=project_details[project_code]
#saving the details and making changes to the dictionary in which the project status details is changed to "completed" which makes it go from existing projects to Completed projects
            save=str(input("Do you want to remove the project(Yes/No)"))
            if save==("Yes"):
                if project_code in project_details:
                    project["project_status"]="Completed"
                if project_code in Ongoing_project_details:
                    Completed_project_details[project_code] = Ongoing_project_details.pop(project_code)

                elif project_code in On_hold_project_details:
                    Completed_project_details[project_code] = On_hold_project_details.pop(project_code)
                

                update_remaining_workers()

                
                print("Project successfully removed from existing projects")
                
                break
            
            else:
                print("Project is not removed")
                break
        except ValueError:
            print("Invalid Statement")
                

            

#defining the fourth Choice menu and getting inputs to update the details of the user input project code
def Update_Project_details():
    global project_details
    print('\n')
    print('            Update project details'       )
    print('\n')
#asking for the project code in which the updated details should be added 
    try:
        project_code=int(input("Project code: "))
        if project_code in project_details:
            print("\n")
            print("Updating details for project with code",project_code)
            print("\n")
# For the Retrieval of the project details to be updated
            project=project_details[project_code]

# Prompt user for updated information
            client_name = input("Enter new client's Name: ")
            start_date = input("Enter new start date (dd/mm/yy): ")
            expected_end_date = input("Enter new expected end date (dd/mm/yy): ")
            number_of_workers = int(input("Enter new number of workers: "))
            if number_of_workers>remaining_workers+project['number_of_workers']:
                print("Not enough workers to assign")
                return
                
            project_status = str(input("Enter updated project status (On hold/Ongoing/Completed): "))
            if project_status==('Ongoing'):
                pass
            elif project_status==('Completed'):
                pass
            elif project_status==('On hold'):
                pass
            else:
                print("invalid statement")
                return
#process for Saving the updated details if the user wishes to save and updating the dictionaris according to that
            save=str(input(" Do you want to update the details(Yes/No)? "))
            if save==("Yes"):
                project["client_name"] = client_name
                project["start_date"] = start_date
                project["expected_end_date"] = expected_end_date
                project["number_of_workers"] = number_of_workers
                project["project_status"] = project_status
                if project_code in project_details:
                    if project["project_status"]=="Completed":
                        if project_code in Ongoing_project_details:
                            Completed_project_details[project_code] = Ongoing_project_details.pop(project_code)
                        elif project_code in On_hold_project_details:
                            Completed_project_details[project_code] = On_hold_project_details.pop(project_code)
                elif project_code in project_details:
                    if project["project_status"]=="Ongoing":
                        if project_code in Completed_project_details:
                            Ongoing_project_details[project_code] = Completed_project_details.pop(project_code)
                        elif project_code in On_hold_project_details:
                            Ongoing_project_details[project_code] = On_hold_project_details.pop(project_code)
                elif project_code in project_details:
                    if project["project_status"]=="On hold":
                        if project_code in Completed_project_details:
                            On_hold_project_details[project_code] = Completed_project_details.pop(project_code)
                        elif project_code in Ongoing_project_details:
                            On_hold_project_details[project_code] = Ongoing_project_details.pop(project_code)

                update_remaining_workers()
                print("Project details updated successfully")
            else:
                print("project details not updated")
        else:
            print("Project code not found. Cannot update details.")
    except ValueError:
            print("Invalid Statement")
     
    

#Defining the Third Menu Choice and asking for the user input to increase the number of workers             
def Add_new_workers():
    print('\n')
    print("          Add new workers to available workers group")
    print('\n')
    
    try:
        
        
        Number_of_workers_to_add=int(input("Number of workers to add:- "))
        print("\n")
#Saving and updating the total available number of workers            
        save=str(input("do you want to Add(Yes/No)? "))
        if save==("Yes"):
            global Available_number_of_workers
            Available_number_of_workers+=Number_of_workers_to_add
            update_remaining_workers()
            print("Successfully added","\n")
        else:
            print("Workers have not been added","\n")
    except ValueError:
            print("Invalid Statement")

#defining the fifth choice menu to see the project statistics
def Project_Statistics():
    print("\n")
    print("               Project Statistics           ")
    print("\n")
    global project_details
    global Available_number_of_workers
    global Completed_project_details
    global sum_of_workers_from_completed_projects
    global Ongoing_project_details
    global On_hold_project_details


    
#accessing the dictionary to find the number of values being the same as "Completed","Ongoing",On hold" and assigning them into a variable to call only the variable while printing 
    Completed_projects=sum(1 for inner_dict in project_details.values() for value in inner_dict.values() if value =='Completed')
    On_going_projects=sum(1 for inner_dict in project_details.values() for value in inner_dict.values() if value =='Ongoing')
    On_hold_projects=sum(1 for inner_dict in project_details.values() for value in inner_dict.values() if value =='On hold')

    
            
#displaying the statistics        
    print("Total number of Completed projects          :-  ",Completed_projects)
    print("Total number of On_going projects           :-  ",On_going_projects)
    print("Total number of On_hold projects            :-  ",On_hold_projects)
    print("Total number of remaining workers to assign :-  ",remaining_workers)
    print('\n')
    
    exit=input("Press any key to exit to the main menu :  ")

    
    
 



#defining the main menu screen to access the other menus to input,change,view and remove details 
def main():
    while True:
        try:
            print("\n               XYZ Company - Main Menu        \n"       )
            print("1. Add a new project to existing projects")
            print("2. Remove a completed project from existing projects")
            print("3. Add new workers to available workers group")
            print("4. Update details on ongoing projects")
            print("5. Project Statistics")
            print("6. Exit")

            choice=int(input("                               Your Choice Number= "))


            if choice == 1:
                Add_a_new_project()
            elif choice == 2:
                Remove_Completed_Project()
            elif choice == 3:
                Add_new_workers()
            elif choice == 4:
                Update_Project_details()
            elif choice == 5:
                Project_Statistics()
            elif choice == 6:
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please select a valid option.")
        except ValueError:
            print("Invalid Statement")
            
#Calling the main menu to display 
main()
        
        


        
    
        
    
        
    

        
                
            
            
            

    
        
            
            


            
    
                
            
        

