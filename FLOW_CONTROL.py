################ FLOE CONTROL ##############
#       1. IF   2 if...elss                #
#       3. if..elif..else 4. for           #
#       5 while     6. break               #
#       7. Continue                        #
############################################
"""
marks = input("Enter Your Marks...!")
if marks > 80:
    print("Distinction")
elif (marks > 60) and (marks <= 80):
    print("FIRST CLASS")
elif (marks > 40) and (marks <= 60):
    print("Second Class")
else:
    print("FAILED")
"""
######################### END IF ... ELIF ... ELSE #############################
### while
"""
num = int(input("Enter value of n"))
if(num <=0):
    print 'Enter a valid number'
else:
    sum = 0
    while(num > 0):
        sum += num
        num -= 1

print(sum)
"""
########################## END OF WHILE #############################

### FOR LOOP
"""
for quantity in range(99,0,-1):
    if (quantity > 1):
        print(quantity, "Bottles of bear on the wall,", quantity, "Botthes of bear")
        if(quantity > 2):
            suffix = str(quantity) + "Bottles of bear on the wall"
        else:
            suffix = "1 Bottles of bear on the wall"
    elif quantity == 1:
        print("1 Bottle of bear on the wall, 1 Bottle of bear")
        suffix = "No more Bottles on the wall"

    print("Take one down and pass it around,", suffix)
    print("---")
"""
###################### END OF FOR LOOP ###############################

### BREAK STATEMENT
"""
count = 1
while True:
    print count
    count += 1
    if count > 15:
        break
"""
###################### END OF BREAK ###################################

#### Continue
"""
for num in range(20):
    if(num % 2 == 0):
        continue
    print num
"""
#######################3 END OF CONTINUE ################################
