# 1. Create storage
# 2. Create functions
# 3. Show menu
# 4. Take user input
# 5. Call correct function
# 6. Repeat until exit
import pandas as pd
import numpy as np
def calculate_average(marks):
    return sum(marks)/len(marks)
def calculate_grade(average):
    if average >= 90:
        return "A"
    elif average >= 75:
        return "B"
    elif average >= 50:
        return "C"
    else:
        return "F"
students={}
num_students=int(input("enter number of students:"))
for i in range(num_students):
    print(
        f"\n students{i+1}"
    )
    name=input("Enter student name:")
    subject1=int(input("enter subject1 marks:"))
    subject2=int(input("enter subject2 marks:"))
    subject3=int(input("enter subject3 marks:"))
    subject4=int(input("enter subject4 marks:"))
    subject5=int(input("enter subject5 marks:"))
    students[name]=[subject1,subject2,subject3,subject4,subject5]
highest_student=""
lowest_student=""
highest_average= -1
lowest_average=101
averages=[]
data=[]
for name, marks in students.items():
    average=calculate_average(marks)
    grade=calculate_grade(average)
    averages.append(average)
    data.append([
        name,
        marks[0],
        marks[1],
        marks[2],
        marks[3],
        marks[4],
        round(average,2),
        grade
    ])
    print(f"{name:<10} average:{average:.2f}")
    if average> highest_average:
        highest_average=average
        highest_student= name
    if average< lowest_average:
        lowest_average=average
        lowest_student=name
df= pd.DataFrame(
    data,
    columns=[
        "Name",
        "Subject1",
        "subject2",
        "subjet3",
        "subject4",
        "subject5",
        "average",
        "grade"
    ]
)
print("\nDATAFRAME")
print(df)
highest_avg = np.max(averages)
lowest_avg = np.min(averages)

print("\nSTATISTICS")
print(f"Highest Scorer : {highest_student}")
print(f"Lowest Scorer  : {lowest_student}")
print(f"Highest Average: {highest_avg:.2f}")
print(f"Lowest Average : {lowest_avg:.2f}")

 