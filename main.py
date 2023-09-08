# Each student will code a program that prints out the following pattern. Each line increases by two stars until it gets to 10, then it starts decreasing by 2 stars. 
#**
#****
#******
#********
#**********
#********
#******
#****
#**

#Students need to use a selection statement and 2 loops in order to complete this activity. 
#Students will receive basic python code and they will piece together the solution. If a student cannot complete this activity they should provide pseudocode of what they imagine the solution to be. 
#--------write your code below ----- #


Step 1: declare num  0, stars  “**”
Step 2: create a loop to repeat total_lines_times
Step 3: create and if else statement to be able to
‘select’ the top half and bottom half of the print
statements. Write conditional statement using i
Step 4 Increase num if i is less than half_total_lines
Step 5. use num to multiple times stars
DISPLAY (stars x num)
Step 6. else decrease num by 1
Step 7. DISPLAY (stars x num)

num =0
stars ="**"

for i in range(10):
    if(i<5):
        print(stars*num)
        num+=1
    else:
        print(stars*num)
        num-=1
