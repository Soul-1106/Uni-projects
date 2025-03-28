Traffic Data Analysis and Visualization
This Python program is designed to process and analyze traffic data from CSV files, providing insights into vehicle counts, classifications, and speed violations. Additionally, it visualizes the data using histograms. The program allows users to validate input dates, process multiple datasets in a session, and generate statistical results.

Key Features:
Data Processing:

Reads traffic data from CSV files.

Extracts vehicle count, type, speed, and direction.

Identifies speed violations.

Counts electric vehicles, buses, and trucks.

Histogram Visualization:

Generates a histogram to display vehicle frequency at two junctions (Hanley Highway/Westway & Elm Avenue/Rabbit Road) per hour.

Uses graphical representations for better analysis.

User Interaction:

Requests a valid date as input.

Handles incorrect date formats and out-of-range values.

Asks the user whether to process additional datasets.

Data Storage & Export:

Saves results to a text file (result.txt) for record-keeping.

Handles missing or incorrect data gracefully.

Validation & Error Handling:

Ensures valid user input for date selection.

Handles file-related errors such as missing or empty files.

Provides meaningful error messages for incorrect inputs.

Workflow:
User Input:

The user enters a date, which is validated.

The program checks if a corresponding CSV file exists.

Data Processing:

Reads the CSV file and extracts key information.

Computes various statistics (e.g., total vehicles, truck percentage, busiest hours).

Identifies weather-related traffic trends.

Visualization:

Displays a histogram to represent vehicle flow at different hours.

User Decision:

Asks whether the user wants to process another dataset.

If yes, the process repeats; otherwise, the program ends.

This program is useful for traffic analysis, urban planning, and optimizing road infrastructure based on data-driven insights. 🚗📊