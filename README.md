# Winkler CoreCompete Project

#This is Jonah Winkler I am a recent graduate of NCSU.

#Changing for comparison to master

# Open the file
wb = xlrd.open_workbook('mrtssales92-present.xlsx')

# Get the list of the sheets name
sheet_list = wb.sheet_names()
print sheet_list

# Select one sheet and get its size
s = wb.sheet_by_name(sheet_list[1])  # or s = wb.sheet_by_index(1)
print s.nrows, s.ncols

# Access the content of a cell 
print s.cell(6,1).value  # 7th row, 2nd column
