#importing modules
import sys
import percolation_functions

#creating main function
def main():
    #using try function to check for errors and handle errors
    try:
        #using the condition if the length of the terminal argument is 1 and the command is perc.py it will call in the execution function from the module and create a 5x5 percolation grid or else it will give a wrong statement prompt
        if len(sys.argv) == 1:
            if sys.argv[0]=='perc.py':
                rows = 5
                columns = 5
                percolation_functions.execution(columns, rows)  
            else:
                print('wrong statement')

         #using the condition if the length of the terminal argument is 2 and according to the second argument the length of the column and rows are determined with a maximum being 9 and minimum being 3 for the rows and column values and will call in the module function to print the grid or else it will print wrong format        
        elif len(sys.argv) == 2: 
            rows, columns = map(int, sys.argv[1].split('x'))
            if 3 <= rows <= 9 and 3 <= columns <= 9:
                percolation_functions.execution(columns, rows)
        #or else giving an output as the grid size entered being above 9x9 or below 3x3  
            else:
                print("grid size exceeds 9x9 or below 3x3 therefore try again")
        #if the length of the system argument being above 2 or 0 ,a message is printed as wrong format 
                    
        else:
            print("Wrong format")
            return

    except:
        print('Execution Error')

main() #calling in the main function for the running of the code

