# WITI has tasked you to automate a simple grading system. As a python student, write
#a program used to display the grades that the students will be receiving based on the
#mark scored in a subject.
#The grades are;
# 90%-100% Grade is A 
# 80%-89%  Grade is B
# 70%-79%  Grade is C
# 60%-69%  Grade is D
# 50%-59%  Grade is E
# <50%     Fail
         #solution

#approach one

mark_scored = int(input("\nEnter the mark scored:   "))
if mark_scored >= 90:
    print("Grade is A")
elif mark_scored >= 80:
    print("Grade is B")
elif mark_scored >= 70:
    print("Grade is C")
elif mark_scored >= 60:
    print("Grade is D")
elif mark_scored >= 50:
    print("Grade is E")
else:
    print("Fail") 

    # approach two
    
def calculate_grades ():
    
    score = int(input("Enter mark scored:\t"))
    if score >= 90 and score <= 100:
        print("Grade is A")
    elif score >= 80 and score <= 89:
        print("Grade is B") 
    elif score >=70 and score <= 79:
        print("Grade is C")
    elif score >= 60 and score <= 69:
        print("Grade is D")
    elif score >= 50 and score <= 59:
        print("Grade is E")
    else:
        print("Fail")
        
calculate_grades()




  


