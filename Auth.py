User = {
    "User_id" : 19416913,
    "User_name": "Zr7994",
    "First Name " : "Md. Zubair Ibna Mostfa",
    "Last Name" : "Rakib",
    "mail" : "rakib129175@gmail.com",
    "password":"rakib79944@"
    
}
mail = input("Enter your mail :")
password = input("Enter your password :")
if password== User["password"] and mail== User["mail"]:
    
    print("Login Successful.")

else:
    print("Invalid email or password.")
    
    
