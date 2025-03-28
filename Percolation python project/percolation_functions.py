#importing modules
import random #importing random for randomly choosing algorithm
from datetime import date #importing date from datetime module for name the text file
from random import randint #importing randint from random randomly choosing between numbers algorith to populate the grid 
from prettytable import PrettyTable #importing pretty table to prettify the table



#creating an execution function to run all the defined functions 
def execution(columns,rows):
    grid, check_percolation = creating_grid_and_insertion(columns, rows, probability=0.15)
    full_grid = printing_grid(grid, check_percolation)
    table = PrettyTable(header=False,hrules=True)
    for row in grid:
        table.add_row(row)
    create_text_file_and_html_file(full_grid, table,check_percolation)


#defining function for creating the full grid filled with random spaces and random 2 digit integers with the percolation process check by calling in the system argument for the number of rows 
def creating_grid_and_insertion(columns,rows,probability=0.15):
    #creating a local variable called grid where it creates multiple lists within a list where the number of inner lists are determined by rows and number of elements in each inner list is determined by columns 
    grid=[['' for i in range(columns)]for i in range(rows)]
    #creating a local variable to insert the ok's in a list according to the number of columns 
    check_percolation = ['OK' for i in range(columns)]

    #inserting random 2 digits numbers into the grid and changing the 'ok's in percolation check list to 'no' if the grid has string values in it 
    for r in range(rows):
      for c in range(columns):
        if random.random()> probability:
          grid[r][c]=randint(10,99)
        else:
          grid[r][c]=''
          
          check_percolation[c] = 'NO'
    return grid,check_percolation


def printing_grid(grid,check_percolation):
    #creating a variable called full grid for transfering the final grid including perculation check into it
    full_grid=''
    #creating variable which acts as the pretty table function
    table=PrettyTable(header=False,hrules=True,field_names=False)
    #using for loop each inner_lists are made into a string from list and each of the elements in the string are seperated by tabs and assigned into the full grid vairiable
    for r in grid:     
      full_grid+= "\t".join(map(str, r)) +'\n'
      #each inner_lists are add in a row and prettified in a table 
      table.add_row(r)
    
    #the check_perculation list is added into the full grid variable to create the whole table with perculation check 
    full_grid+="\t".join(check_percolation)
    #the prettified table is printed with check perculation list under it where it becomes one string and each element are seperated by spaces to display a final table with perculation status   
    print(table,'\n','   '.join(check_percolation))
    return full_grid
    
    
def create_text_file_and_html_file(full_grid,table,check_percolation):
      
      #creating a local variable for naming the date today for naming of the text file
      date_today=date.today()
      #creating a local variable for creating a random 4 digit number for naming of the text file
      four_digit_numbers=random.randint(1000,9999)
      #creating the whole file name using the created local variables the date and random 4 digit number
      file_name=(f'{date_today}_{four_digit_numbers}.txt')
      #Creating a text file with the file_name variable as its name and writing the created whole grid variable into the text file
      with open(file_name , 'w') as fn:
        fn.write(f'{full_grid}')
        fn.close()
     
      
#creating html code by opening the file as it's random 4 digit number and date today as its name
      html_f=(f'{date_today}_{four_digit_numbers}.html')
      with open(html_f, "w") as html_file:
        html_file.write("<html>\n")
        html_file.write("<head><title>Grid Results</title></head>\n")
        html_file.write("<body>\n")
        html_file.write("<pre>\n")
        html_file.write(table.get_string()+'\n'+'   '.join(check_percolation))
        html_file.write("</pre>\n")
        html_file.write("<p>"   "</p>\n")
        html_file.write("</body>\n")
        html_file.write("</html>\n")
        return date_today,four_digit_numbers,full_grid

