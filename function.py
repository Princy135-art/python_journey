def employee_report(name, age=20, salary=3000, *departments, city="Delhi", **extra_info):
    
    print(f"employee name:{name}")
    print(f"age:{age}")
    print(f"city:{city}")
    print(f"salary:{salary}")
    print("\ndepartments:")
    for department in departments:
        print(department)
    print("\nextra information:")
    for key, value in extra_info.items():
        print(f"{key}:{value}")
    total_departments=len(departments)
    return name, total_departments
#function call here
employee_report(
    "Princy",
    20,
    5000,
    "Hr",
    "Finance",
    city="Mumbai",
    experience= 3,
    designation= "Manager"


)