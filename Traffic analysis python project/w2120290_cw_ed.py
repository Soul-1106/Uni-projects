#Author:H.I.A Haneef
#Date:19/12/2024
#Student ID:20231259

# Task D: Histogram Display
from graphics import *

class HistogramApp:
    def __init__(self, traffic_data,date):
        """
        Initializes the histogram application with the traffic data and selected date.
        """
        self.traffic_data = traffic_data
        self.date = date

        list_of_times_hanley_highway=[inner_list[2].split(":")[0] for inner_list in self.traffic_data if inner_list[0]=='Hanley Highway/Westway'] #Extraction of hour values for vehicles passing through Hanley Highway/Westway using list comprehention method which extracts the hour (index 2) from the timestamp of vehicles at 'Hanley Highway/Westway' by splitting the time string on ':'
        hour_count_Hanley_Highway={}  # Dictionary to store hour and vehicle count for hanleyhighway
        count=0 # Initializing vehicle count
        for i in list_of_times_hanley_highway: #This nested loop counts the number of vehicles for each hour at 'Hanley Highway/Westway' and stores it in the hour_count_Hanley_Highway dictionary
            count=0
            for j in list_of_times_hanley_highway:
                if i==j:
                    count+=1
            hour_count_Hanley_Highway[i]=count
    

        list_of_times_Elm_Avenue=[inner_list[2].split(":")[0] for inner_list in self.traffic_data if inner_list[0]=='Elm Avenue/Rabbit Road']
        hour_count_Elm_Avenue={}  # Dictionary to store hour and vehicle count for hanleyhighway
        count=0 # Initializing vehicle count
        for i in list_of_times_Elm_Avenue: #This nested loop counts the number of vehicles for each hour at 'Hanley Highway/Westway' and stores it in the hour_count_Hanley_Highway dictionary
            count=0
            for j in list_of_times_Elm_Avenue:
                if i==j:
                    count+=1
            hour_count_Elm_Avenue[i]=count

            #creating nested dictionary to store the hour counts of two junctions
        self.traffic_data={"Elm_Avenue":hour_count_Elm_Avenue,
                            "Hanley_Highway":hour_count_Hanley_Highway}

     # Will hold the canvas for drawing

    def setup_window(self):
        """
        Sets up the Tkinter window and canvas for the histogram.
        """

        self.window = GraphWin("Histogram" ,1200,600)  # Will hold the canvas for drawing
        self.window.setBackground("black")
        

    def draw_histogram(self):
        """
        Draws the histogram with axes, labels, and bars.
        """
        #drawing a line for the histogram
        line_point1=Point(100,525)
        line_point2=Point(1100,525)
        line = Line(line_point1,line_point2)
        line.setWidth(3)
        line.setFill("white")
        line.draw(self.window)

        # Grouped histogram parameters
        num_groups = 24  # Number of groups
        line_length = 1100 - 100  # Length of the line (1100 - 100)

        # Small space between each group
        space_between_groups = 15  # Space between groups

        group_length = (line_length - (num_groups - 1) * space_between_groups) / num_groups #Get the value for the width the group should have on the line

        max_height = 400  # Maximum possible height for a rectangle
        max_traffic_value = max(max(self.traffic_data["Elm_Avenue"].values()), max(self.traffic_data["Hanley_Highway"].values()))  # Get the highest value from both datasets
        scaler = max_height / max_traffic_value 
        
        for group in range(num_groups):
        # Start x-coordinate of the group, adding space between groups
            group_start_x = 100 + group * (group_length + space_between_groups)
            # Get the heights for the two rectangles based on the current group
            group_key = f'{group:02}'  # Generate the key (e.g., '00', '01', etc.)

            try:
                height_for_Elm_Avenue_triangle = self.traffic_data["Elm_Avenue"][group_key] # Get height from traffic_data1 
                height_for_Hanley_Highway_traingle = self.traffic_data["Hanley_Highway"][group_key] # Get height from traffic_data2

            except KeyError: # default to 0 if key not found
                             # default to 0 if key not found
                height_for_Elm_Avenue_triangle = 0
                height_for_Hanley_Highway_traingle = 0

            # Scale the heights for better visualization
            scaled_height_for_Elm_Avenue_rectangle = height_for_Elm_Avenue_triangle * scaler
            scaled_height_for_Hanley_Highway_rectangle = height_for_Hanley_Highway_traingle * scaler

            # Creating the first rectangle for the current group (elm highway)
            x1 = group_start_x
            x2 = x1 + group_length / 2  # The width of the first rectangle
            y_base = 525  # Base y-coordinate (on the line)

            rectangle_for_Elm_Avenue = Rectangle(Point(x1, y_base), Point(x2, y_base - scaled_height_for_Elm_Avenue_rectangle))
            rectangle_for_Elm_Avenue.setFill("#baf202") 
            rectangle_for_Elm_Avenue.setOutline("white")
            rectangle_for_Elm_Avenue.draw(self.window)


            # Creating the second rectangle for the current group(hanley highway)
            x1 = x2  # The second rectangle starts where the first one ends
            x2 = x1 + group_length / 2  # The width of the second rectangle

            rectangle_for_Hanley_Highway = Rectangle(Point(x1, y_base), Point(x2, y_base - scaled_height_for_Hanley_Highway_rectangle))
            rectangle_for_Hanley_Highway.setFill("#e62060")  
            rectangle_for_Hanley_Highway.setOutline("white") 
            rectangle_for_Hanley_Highway.draw(self.window)

            # Position label above the first rectangle (Vehicle count Elm Avenue)
            label1 = Text(Point((x1 + x2) / 2 -17, y_base - scaled_height_for_Elm_Avenue_rectangle - 10), str(height_for_Elm_Avenue_triangle))  
            label1.setSize(10)
            label1.setTextColor("white")
            label1.draw(self.window)

            # Position label above the second rectangle(vehicle count Hanley Highway)
            label2= Text(Point((x1 + x2) / 2, y_base - scaled_height_for_Hanley_Highway_rectangle - 10), str(height_for_Hanley_Highway_traingle))  
            label2.setSize(10) 
            label2.setTextColor("white") 
            label2.draw(self.window)


            # Add the number under each group(Hour count)
            label3 = Text(Point(((x1 + x2) / 2) - 8, y_base + 10), group_key)  # Position the number under the group
            label3.setSize(10)  
            label3.setTextColor("white")  
            label3.draw(self.window) 


        

    def add_legend(self):
        """
        Adds a legend to the histogram to indicate which bar corresponds to which junction.
        """
        legend_x = self.window.getWidth() - 1100
        legend_y = 50
        spacing = 25

        # Data1 Legend (Elm avenue)
        legend_box1 = Rectangle(Point(legend_x, legend_y), Point(legend_x + 20, legend_y + 20))
        legend_box1.setFill("#baf202")
        legend_box1.setOutline("white")
        legend_box1.draw(self.window) 

        legend_label1 = Text(Point(legend_x + 97, legend_y + 10), "Elm Avenue/Rabbit Road")
        legend_label1.setSize(10)
        legend_label1.setTextColor("white")
        legend_label1.draw(self.window)

        # Data2 Legend (Hanley Highway)
        legend_box2 = Rectangle(Point(legend_x, legend_y + spacing), Point(legend_x + 20, legend_y + 20 + spacing))
        legend_box2.setFill("#e62060")
        legend_box2.setOutline("white")
        legend_box2.draw(self.window)

        legend_label2 = Text(Point(legend_x + 100, legend_y + spacing + 10), "Hanley Highway/Westway")
        legend_label2.setSize(10)
        legend_label2.setTextColor("white")
        legend_label2.draw(self.window)

        # Data3 Legend (hour label)
        legend_label3 = Text(Point(625, 550), "Hours 00:00 to 24:00")
        legend_label3.setSize(12)
        legend_label3.setTextColor("white")
        legend_label3.draw(self.window)

        # Data4 Legend (Title)

        legend_label4 = Text(Point(legend_x +238, legend_y - 15), f"Histogram of Vehicle Frequency per Hour ({self.date[0]:02d}/{self.date[1]:02d}/{self.date[2]:02d})")
        legend_label4.setSize(15)
        legend_label4.setTextColor("white")
        legend_label4.draw(self.window)
        

        # Data5 Legend(Vehicle frequency)
        legend5_y=120
        legend_label5_string="vehicle Frequency"
        for label in legend_label5_string:
            legend_label5 = Text(Point(15, legend5_y), label)
            legend_label5.setSize(15)
            legend_label5.setTextColor("white")
            legend_label5.draw(self.window)
            legend5_y+=20
            

    def run(self):
        """
        Runs the Tkinter main loop to display the histogram.
        """
        try:
            self.setup_window() #Sets up the window 
            self.draw_histogram() #Draw the histogram
            self.add_legend() #Add Legends
            self.window.getMouse() # Wait for the Mouse click to close the window
            self.window.close() #Close the window as everything gets wiped
        except GraphicsError:
            pass

# Task E: Code Loops to Handle Multiple CSV Files
class MultiCSVProcessor:
    def __init__(self):
        """
        Initializes the application for processing multiple CSV files.
        """
        self.current_data = None
        self.traffic_data = {}
        self.date = []

        
    def validate_date_input(self):# This function is used for validating the inputs for the date
                                # This function runs in a loop until the conditions are met and stores the values inside the filepath varaiable and returns the variable as that will be the csv file name
                                # This function checks to see if the user input is inside a given range or not
                                # If it's not in range , it returns an error message and reasks for the user to type the input 
                                # If the user input is not valid , it returns integer required and asks the user to type again
                                #Prompts the user for a date in DD MM YYYY format, validates the input for:- Correct data type- Correct range for day, month, and year
        
        prompts=[('day',1,31,"DD"),('month',1,12,"MM"),('year',2000,2024,"YYYY")]
        date=[]
        for prompt,min_limit,max_limit,format in prompts:
            while True:
                try:
                    value = int(input(f"Please enter the {prompt} of the survey in the format {format}: "))
                    if not(min_limit<=value<=max_limit):
                        print(f"Out of range - values must be in the range {min_limit} and {max_limit}")
                        continue
                    else:
                        date.append(value)
                        break
                except ValueError:
                    print("integer required")
                    continue
        
        self.date=date
        file_path=f'traffic_data{self.date[0]:02d}{self.date[1]:02d}{self.date[2]:02d}.csv'
        return file_path

    def load_csv_file(self, file_path): # This function is used to process the csv file according to the filename passed as file_path, process the data needed, stores it into a final list variable called outcomes,saves the results in a text file and displays the results of the processed data 
                                        # This function checks whether the file exists or not and if the filename does not match file_path it returns the error message for file not found  
        """
        Loads a CSV file and processes its data.
        """
        """
        Processes the CSV data for the selected date and extracts:
        - Total vehicles
        - Total trucks
        - Total electric vehicles
        - Two-wheeled vehicles, and other requested metrics
        """
        try:
            with open(file_path, mode='r') as data:   # opens the csv file in read mode as data
                lines=data.readlines()              #obtain the data from the csv file and put it into a variable called lines
                self.current_data=[line.strip().split(",") for line in lines[1:]]  #creates a list with nested lists using list comprehention which checks each line by line and removes all the white spaces and escape characters using strip method and seprates them with comma using split method
               
        
            file_name=file_path             
            total_vehicles=len(self.current_data) # calculation for finding total vehichles using list comprehension method and reading it's length

            total_trucks=len([inner_list for inner_list in self.current_data if inner_list[8]=='Truck'])  # calculation for finding total trucks by using list comprehension where the vehicle (index 8) is truck and reads the length of the created list 

            total_electric_vehicles=len([inner_list for inner_list in self.current_data if inner_list[9] =='True']) # calculation for finding total electric vehicles by using list comprehension  where elctricHybrid (index 9) is "true" and and reads the length of the created list 
                
            total_two_wheeled_vehicles =len([inner_list for inner_list in self.current_data if inner_list[8]=='Bicycle'or inner_list[8]=="Motorcycle" or inner_list[8]=="Scooter"]) #calculation for finding total two wheeled vehicles by using list comprehension where vehicle is (index 8) is "Scooter" or "Motorcycle" or "Bicycle " and reads the length of the created list 

            total_busses_leaving_Elm_Avenue_heading_north=len([inner_list for inner_list in self.current_data if inner_list[8]=='Buss' and inner_list[0]=='Elm Avenue/Rabbit Road' and inner_list[4]=="N"]) #calculation for finding total busses leaving Elm Avenue and heading north using list comprehension which takes the lines into a list where the vehicle (index 8) is "Buss" and direction in (index 4) is  "N" and reads the length of the created list 

            total_vehicles_not_turning_left_or_right=len([inner_list for inner_list in self.current_data if inner_list[3]==inner_list[4]]) # calculation for finding total electric vehicles by using list comprehension where the value of direction in(index 4) and direction out(index 5) is equal and and reads the length of the created list 


            percentage_of_trucks=round((total_trucks/total_vehicles) * 100) # Calculation for finding the total percentage of trucks out of total vehicles 

            total_bicycles=len([inner_list for inner_list in self.current_data if inner_list[8]=='Bicycle']) # calculation for finding total number of bicycles by using list comprehension where the vehicle (index 8) is "Bicycle" and reads the length of the created list for finding the percentage of bicycles out of total vehicles
            average_bicycle=round(total_bicycles/24) # Calculation for finding average bicycles

            total_vehicle_over_speed_limit=len([inner_list for inner_list in self.current_data if int(inner_list[6])<int(inner_list[7])]) # Calculation for finding the number of vehicles recorded as over the speed limit
            only_Elm_Avenue_vehicles=[inner_list for inner_list in self.current_data if inner_list[0]=='Elm Avenue/Rabbit Road'] # list creation using list comprehention method to filter the vehicles from only Elm Avenue/Rabbit Road
            only_Hanley_Highway_vehicles=[inner_list for inner_list in self.current_data if inner_list[0]=='Hanley Highway/Westway']# list creation using list comprehention method to filter the vehicles from only Hanley Highway/Westway
            average_Elm_avenue_scooters=round((len([inner_list for inner_list in self.current_data if inner_list[8]=='Scooter' and inner_list[0]=='Elm Avenue/Rabbit Road'])/len(only_Elm_Avenue_vehicles)*100)) # Calculation for finding the average number of scooter passing through Elm Avenue/Rabbit Road using list comprehention method which filters scooter records at 'Elm Avenue/Rabbit Road' and calculates their percentage out of total vehicles at that junction

            # Calculation for finding the busiest hour by counting the number of vehicles in each hour
            list_of_times_hanley_highway=[inner_list[2].split(":")[0] for inner_list in self.current_data if inner_list[0]=='Hanley Highway/Westway'] #Extraction of hour values for vehicles passing through Hanley Highway/Westway using list comprehention method which extracts the hour (index 2) from the timestamp of vehicles at 'Hanley Highway/Westway' by splitting the time string on ':'
            hour_count_Hanley_Highway={}  # Dictionary to store hour and vehicle count for hanleyhighway
            count=0 # Initializing vehicle count
            for i in list_of_times_hanley_highway: #This nested loop counts the number of vehicles for each hour at 'Hanley Highway/Westway' and stores it in the hour_count_Hanley_Highway dictionary
                count=0
                for j in list_of_times_hanley_highway:
                    if i==j:
                        count+=1
                hour_count_Hanley_Highway[i]=count
            total_vehicles_in_busiest_hour_passing_hanley_highwhay=max(hour_count_Hanley_Highway.values()) #Finding the highest number of vehicles recorded in peakest hour using the max() function on the busy_time dictionary
            busy_hours=[f'{key}:00 and'  f' {int(key)+1}:00' for key, value in hour_count_Hanley_Highway.items() if value == total_vehicles_in_busiest_hour_passing_hanley_highwhay] #Constructing a list of the busiest hour ranges and joining them into a single string for display
            busy_hours=','.join(busy_hours)

            

            #Extraction of the hours where it's raining (either Light or Heavy Rain)
            rainy_hours=[inner_list[2].split(":")[0] for inner_list in self.current_data if inner_list[5]=='Light Rain' or inner_list[5]=='Heavy Rain']  #Filtering vehicle records where the weather (index 5) is 'Light Rain' or 'Heavy Rain' and getting only the hour values of it into a list
            rainy_hours=set(rainy_hours) # removing duplicates to count the total hours
            rainy_hours=len(list(rainy_hours)) #calculation for obtaining the total hours



            #saving all the results in a variable and containing it in a list 
            outcomes= [
                f"data file selected is {file_name}",
                f"The total number of vehicles recorded for this date is {total_vehicles}",
                f"The total number of trucks recorded for this date is {total_trucks}",
                f"The total number of electric vehicles for this date is {total_electric_vehicles}",
                f"The total number of two-wheeled vehicles for this date is {total_two_wheeled_vehicles}",
                f"The total number of Buses leaving Elm Avenue/Rabbit Road heading North is {total_busses_leaving_Elm_Avenue_heading_north}",
                f"The total number of Vehicles through both junctions not turning left or right is {total_vehicles_not_turning_left_or_right}",
                f"The percentage of total vehicles recorded that are trucks for this date is {percentage_of_trucks}%",
                f"The average number of Bikes per hour for this date is: {average_bicycle}",
                f"The total number of Vehicles recorded as over the speed limit for this date is {total_vehicle_over_speed_limit}",
                f"The total number of vehicles recorded through Elm Avenue/Rabbit Road junction is {len(only_Elm_Avenue_vehicles)}",
                f"The total number of vehicles recorded through Hanley Highway/Westway junction is {len(only_Hanley_Highway_vehicles)}",
                f"{average_Elm_avenue_scooters}% of vehicles recorded through Elm Avenue/Rabbit Road are scooters.",
                f"The highest number of vehicles in an hour on Hanley Highway/Westway is {total_vehicles_in_busiest_hour_passing_hanley_highwhay}",
                f"The most vehicles through Hanley Highway/Westway were recorded between {busy_hours}",
                f"The number of hours of rain for this date is: {rainy_hours}"
            ]
        except FileNotFoundError: #error handling if the file is not found and returning a message 
                return"File not found. Try again."
        except ZeroDivisionError:
            return "File is empty"
        except IndexError:
            pass
        #Displaying the outcomes
        print(f'\n**********************************************\n{outcomes[0]}\n**********************************************\n')
        for lines in outcomes[1:]:
            print((lines))


        #Saving the processed data to a text file
        with open(f'results.txt',"a") as file: # Opening the file in append mode to avoid overwriting existing content.
            file.write((f'**********************************************\n{outcomes[0]}\n**********************************************\n'))
            for lines in outcomes[1:]:
                file.write(f'{lines}\n') # Writes each line from the 'outcomes' list to the file with a newline character
            file.write("\n\n\n") # for improving readability
        return outcomes

    def clear_previous_data(self): #This function resets the values of the instances
        """
        Clears data from the previous run to process a new dataset.
        """

        self.current_data = None
        self.traffic_data=None
        self.date = None

    def handle_user_interaction(self):  #This function asks the user whether load another dataset or not and returns the yes or no string
                                        #The function loops again and asks again If the user inputs anything other than 'yes' or 'no' in captalized form
        """                           
        Handles user input for processing multiple files.
        """

        while True:
            validate_continue=input("Load another dataset 'Y' or 'N' : ").upper()
            if validate_continue == 'Y':
                break
            elif validate_continue =="N":
                break
            else:
                print("Type 'Y' or 'N'")
                continue
        return validate_continue

    def process_files(self):
        """
        Main loop for handling multiple CSV files until the user decides to quit.
        """
        while True:
            self.clear_previous_data()  # Clear previous data before processing a new file
            file_path = self.validate_date_input()  # Get and validate file path based on date input
            outcomes = self.load_csv_file(file_path)  #Get the outcomes from the processed data 

            if outcomes == "File not found. Try again.": #Error handling if the file is not found the program will loop to the start 
                print("File not found. Try again.")
            elif outcomes =="File is empty":
                print("File is empty" )
            elif outcomes:
                # Generate and run the histogram app
                app = HistogramApp(self.current_data, self.date)
                app.run()
            
            # Get the validation and according to the user input yes or no , the program ends or reloops respectively
            validation=self.handle_user_interaction() 
            if validation == "Y": 
                continue
            elif validation=="N":
                print("Thank you for using . Goodbye!")
                break

if __name__ == "__main__":
    # This ensures the script runs the 'MultiCSVProcessor' class only when executed directly and not when imported as a module(good programming habit)
    processor = MultiCSVProcessor()
    processor.process_files()