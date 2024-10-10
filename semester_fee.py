semester = {
    "Name":"Md. Zubar Ibna Mostafa",
    "Semester Completed": ["1st semester","2nd semester","3rd semester","4th semester"],
    "Semester fee" : [139500,90000,85000,95000],
    "Semester Cgpa" :[3.12,3.22,3.00,3.35],
    "Course complete":[15,13,13,16]
}
Semester_fees = 0
for i in range(len(semester['Semester fee'])):
    Semester_fees = Semester_fees + semester["Semester fee"][i]
semester.update ({"Name":'Md. Zubair Ibna Mostafa'})
semester.update ({"Course complete" :[15,15,15,16]})
print (semester)
print (f"{semester['Name']} total tution fee is {Semester_fees} taka")
avg_semester_fee = Semester_fees/4
print (avg_semester_fee)
