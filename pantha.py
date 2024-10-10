Pantha = {
    "Name": "Muktadir Us Saleheen",
    "Age" : 25,
    "University": "Tumi Ami Tumi(UIU)",
    "Course Completed": ["DsA","Java","C++","Calculus","Dm","Math 1"],
    "Credit Completed" : 59,
    "Semester Credit Complete": [15,12,13,15,17]
}
Pantha.update ({"University" : "United International University"})
Pantha.update ({"Semester Credit Complete":[15,15,15,15,15]})
Pantha.update ({"Course Completed": ["DsA","Java","Physics","Math","English","SE","System Design"]})
print (Pantha)
print (f"Pantha completed {Pantha['Course Completed']} this course.")
print (f'{Pantha["Course Completed"][1]}')