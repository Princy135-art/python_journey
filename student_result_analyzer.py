import numpy as np
import pandas as pd

#calculate total marks
def calculate_total(marks):
    return sum(marks)
#calculate average markks
def calculate_average(marks):
    return sum(marks)/len(marks)
students={}

num_students= int(input("enter number of students:"))
for i in range(num_students):
    print(

        f"\n students{i+1}"
    )
    name= input("Enter student name:")
    subject1= int(input("enter subject1 marks:"))
    subject2= int(input("enter subject2 marks:"))
    students[name]= [subject1, subject2]
highest_student=""
lowest_student=""
ighest_average = -1
lowest_average= 101
averages= []
data=[]
for name, marks in students.items():
    total= calculate_total(marks)
    average= calculate_average(marks)
    averages.append(average)
    data.append([
        name,
        marks[0],
        marks[1],
        total,
        round(average, 2)
    ])
    print(f"{name:<10} total:{total:<6} average:{average:.2f}")
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
        "total",
        "average"
    ]
)
print("\nDATAFRAME")
print(df)
class_average = np.mean(averages)
highest_avg = np.max(averages)
lowest_avg = np.min(averages)
std_dev = np.std(averages)

print("\nSTATISTICS")
print(f"Highest Scorer : {highest_student}")
print(f"Lowest Scorer  : {lowest_student}")
print(f"Class Average  : {class_average:.2f}")
print(f"Highest Average: {highest_avg:.2f}")
print(f"Lowest Average : {lowest_avg:.2f}")
print(f"Standard Dev   : {std_dev:.2f}")