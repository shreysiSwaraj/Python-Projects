import datetime

user_input = input("Enter your goal with deadline separated by colon\n")
input_list = user_input.split(":")

goal = input_list[0]
deadline = input_list[1]

deadline_date = datetime.datetime.strptime(deadline, "%d.%m.%Y")
print(deadline_date)
today_date = datetime.datetime.today()

time_diff = deadline_date - today_date
print(f"{int(time_diff.total_seconds()/60/60)} hours left before the deadline")
