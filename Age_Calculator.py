borning_year = input("In which year where you born\n->")
borning_month = input("In which month were you born\n->")
if borning_month == "January":
    borning_month=1
elif borning_month =="February":
    borning_month=2
elif borning_month =="March":
    borning_month = 3
elif borning_month =="April":
    borning_month = 4 
elif borning_month =="May":
    borning_month = 5
elif borning_month =="June":
    borning_month = 6
elif borning_month =="July":
    borning_month = 7
elif borning_month =="August":
    borning_month = 8
elif borning_month =="September":
    borning_month = 9
elif borning_month =="October":
    borning_month = 10
elif borning_month =="November":
    borning_month = 11
elif borning_month =="December":
    borning_month = 12

age_y = 2021-int(borning_year)
age_m = 12-int(borning_month)
print("You are {0} years and {1} months old".format(age_y,age_m))

