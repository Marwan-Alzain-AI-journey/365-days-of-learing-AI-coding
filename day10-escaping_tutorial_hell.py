customer_information = {
        "Email" : "" ,
        "passward" : ""
}
email = input("enter your email: ")
pass_ward = input(" enter your passward: ")
customer_information["Email"] += email
customer_information["passward"] += pass_ward
s1 = open("information.txt", "a")
s1.write("\nEmail: " + customer_information["Email"] + "\nPassward: " + customer_information["passward"] )
s1.close()
def v():
    visibility_email = input("enter S to show Email or H to keep it hidden: ")
    visibility_passward = input("enter S to show passward or H to keep it hidden: ")

    if visibility_email == "S" and visibility_passward == "S":
        return customer_information["Email"] + "\n" + customer_information["passward"]
    elif visibility_email == "H" and visibility_passward == "H":  
        return "your Email + Passward are kept hidden"
    
    elif visibility_email == "H" and visibility_passward == "S":
        return customer_information["passward"] + "\nyour Email is kept hidden"
    
    elif visibility_email == "S" and visibility_passward == "H":
        return customer_information["Email"] + "\nyour Passward is kept hidden"
    else:
        return "invalid input"
print(v())