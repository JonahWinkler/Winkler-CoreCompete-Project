#******************************************************************
#
# Date: February 4, 2019
# Programmer:  Jonah Winkler
# Version: 5
#
# Description:  Retail Data Compiler
#
# This application generates a report of all retail sales by
# type of business. The report includes count, sum, mean, and median of
# data between dates selected by the user.
#
# See comments within the program for further details.
#
#******************************************************************

"""I start the code off with the class MathOps that has functions count, sum, averafge, and median."""

class MathOps:
    # Here are four math operations to class MathOps, count, sum, mean, and median.
    
    def __init__(self,aList):
        # Initialize the list and local variables
        self.listCount = 0
        self.listSum = 0
        self.listMean = 0
        self.listMedian = 0
        self.list = aList
        
    def countElements(self):
        # Counts the numbner of elements in the list and returns the count 
        intCount = 0
        currentListLength = len(self.list)
        while(intCount < currentListLength):
            intCount = intCount +1
            self.listCount = self.listCount + 1
            
        return(self.listCount)
        
        
    def sumElements(self):
        # This adds all elements in the list and returns the sum
        intCount = 0
        sumList = 0
        currentListLength = len(self.list)
        while(intCount < currentListLength):
            sumList = sumList + self.list[intCount]
            intCount = intCount +1
            self.listSum = sumList
            
        return (self.listSum)
        
        
    def meanElement(self):
        # This finds the average of all elements in the list and returns the average
        self.listMean = self.listSum/self.listCount
        
        return(self.listMean)
    
        
    def medianElement(self):
        # This finds the median value in the list and returns the median
        self.list.sort(key=None, reverse=False)
        listlength =len(self.list)
        
        if listlength%2 == 0:
        # If the list has an even number of items then we have to take avg of middle two
            k=0
            k= int(listlength/2)
            self.listMedian = (self.list[k-1] + self.list[k])/2
        else:
            # If the list has an odd number of items then I find the middle item. 
            k=0
            k = int(listlength/2)
            self.listMedian = self.list[k]
            
        return(self.listMedian)
        
"""I first bring data into a list of rows titled inputm."""

import csv

with open('mrtssales_Combined.csv') as inputfile:
    reader = csv.reader(inputfile)
    inputm = list(reader)
 
""" I need to clean the data provided from the csv file. I delete empty rows, then delete rows that
have empty cells. The while loop removes blank rows inside the data. I then delete empty rows as
needed for now to compile. I would like to have a way to tell if there are completely empty rows, and then deleted them,
instead of me visually looking at the original data. Also, potentially have a method to report
to the user the number of missing items in their request. Maybe a double loop that looks for "". 
"""

i=71
while i < 79:
    del inputm[i]
    i+=1

del inputm[44]
del inputm[34]
del inputm[30]
del inputm[27]
del inputm[24]
del inputm[23]
del inputm[5]

"""Here I found the size of the data. I created 2 global variables assigning variable names
of rows and columns."""

Number_Of_Rows = len(inputm)
First_Row = inputm[0] 
Number_Of_Columns =len(First_Row)

""" The data has many commas inside the cells due to numbers being over one thousand, ex: 12,040.
Therefore, I removed the commas to allow for easier computation as integers. I named the new data
set inutm_New I would like to write later code that handles the commas, but this while loop is
what I am using for now.
"""

i=0 
inputm_New=[]
while i < Number_Of_Rows:
    j=0
    while j < Number_Of_Columns:
        item = inputm[i][j]
        item = item.replace(',','')
        inputm_New.append(item)
        j += 1
    i +=1

"""I also need to remove empty columns and columns with variable titles. I would like to handle this
differently and before data cleaning, but this is what I have for now. I update the number of coumns variable."""

del inputm_New[0:Number_Of_Columns*5:] # Removes first five rows for use in analysis
del inputm_New[0::Number_Of_Columns] # Removes first column from data
del inputm_New[0::Number_Of_Columns-1] # Removes second column from data


Number_Of_Columns = Number_Of_Columns - 2

""" There were blank cells after the data. Therefore, I remove all blanks after data, I found
the number by returning the last data enter and verifiy this in original data file. I did not want
to hard code this number in, but this works for now"""

# I tried Number_Of_Data_Points = Number_Of_Columns * Number_Of_Rows but this does not provide the
#correct number for some reason

del inputm_New[28980::]

"""I need to convert the data type from string to integers for computation with the folowiong while loop."""

i=0 
inputm_New_Ints = [] 

while i < len(inputm_New):
    item = inputm_New[i]
    item_int = int(item)
    inputm_New_Ints.append(item_int)
    i += 1

"""Now I ask for the following 2 user inputs for start month and year and end month and year.
I then print the user input on the screen with a to between their selection"""

print("Hello, thank you for using Jonah's application. This application provides a" +'/n' + "report of statistics based on estimates of monthly retail and food services sales by kind of" +'/n'+" business between 1992-2018. Please provide a start month/year and an end month/year using"+'/n'+"two digits for the month and four digits for the year.")
print()

Start = input("Enter start month and year in the following format: ##/####   ")
End = input("Enter end month and year in the following format: ##/####   ")

print()
print (Start, "to", End)

""" I now must pull months and years from user input's string.
Then I convert the string variables to integers and relabel.
I would like to make sure the user input is valid with an if statement to make sure
start date is before end date. """

StartMonth = Start[0:2]
StartYear = Start[3:7]
EndMonth = End[0:2]
EndYear = End[3:7]

intStartMonth = int(StartMonth)
intEndMonth = int(EndMonth)
intStartYear = int(StartYear)
intEndYear = int(EndYear)

""" Now I calculate the number of months the users wants data from, and the first
location of the data they want in the data set"""

Number_Of_Months = (intEndYear - intStartYear)*12 + intEndMonth - intStartMonth + 1

First_Month_Data_Location = (intStartYear - 1992)*12 + intStartMonth -1

""" I create a file to save data titled Jonah_Project_Output.txt. I use the following while
loop to create, print, and save all desired statistics on data for users. The loop also provides
the retail category for each set of statistics. """

file = open('Jonah_Project_Output.txt',"w")

i=0
j=5
while i < len(inputm_New_Ints):
    List_For_Calulations = MathOps(inputm_New_Ints[i + First_Month_Data_Location:i + First_Month_Data_Location + Number_Of_Months:])
    print()
    file.write(inputm[j][1] +'\n')
    print(inputm[j][1])
    print()
    
    count_of_list = List_For_Calulations.countElements()
    sum_of_list = List_For_Calulations.sumElements()
    mean_of_list = List_For_Calulations.meanElement()
    median_of_list = List_For_Calulations.medianElement()
    
    print("   The number of values in data selected is: %d" % count_of_list)
    print("   The sum of values in data selected is: %d" % sum_of_list)
    print("   The mean of values in data selected is: %d" % mean_of_list)
    print("   The median of values in data selected is: %d" % median_of_list)
    
    file.write('\t' + "The number of values in data selected is: " + str(count_of_list) +'\n')
    file.write('\t' + "The sum of values in data selected is: " + str(sum_of_list) + '\n')
    file.write('\t' + "The mean of values in data selected is: " + str(mean_of_list) + '\n')
    file.write('\t' + "The median of values in data selected is: " + str(median_of_list) + '\n'+'\n')
    
    i += (Number_Of_Columns)
    j +=1
    
    
file.close()
print('\n' + "Your report can now be accessed in a file titled Jonah_Project_Output.txt")