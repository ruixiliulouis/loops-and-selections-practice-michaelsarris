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


x=0
stars = "**"
#print(stars)

if (x<5):
    for i in range(6):
        print(stars*x)
        x+=1
x-=1
for i in range(6):
    x-=1
    print(stars*x)
   
