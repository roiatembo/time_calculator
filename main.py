from datetime import datetime, timedelta

def add_time(start_time, duration, day=""):
 
    start_dt = (datetime.strptime(start_time, "%I:%M %p")).strftime("%H:%M")

    if ":" in duration:
        duration_list = duration.split(":")
        hrs = int(duration_list[0])
        min = int(duration_list[1])
    
    result = datetime.strptime(start_dt, "%H:%M") + timedelta(hours=hrs, minutes=min)
    time_difference = datetime.strptime("00:00", "%H:%M") - datetime.strptime(start_dt, "%H:%M")
    
    total_time_added = (hrs * 60) + min
    total_time_diff_lst = str(time_difference).split(",")[1].split(":")
    total_time_diff = (int(total_time_diff_lst[0]) * 60) + (int(total_time_diff_lst[1]))

    if total_time_added > total_time_diff:
        days = "(next day)"
    else:
        days = ""


    if day != "":
        final_result = result.strftime("%I:%M %p, %A")
    else:
        final_result = result.strftime("%I:%M %p")

    if days != "":
        final_result = f"{final_result} {days}"

    return final_result


print(add_time("3:00 PM", "3:10"))
# Returns: 6:10 PM

print(add_time("11:30 AM", "2:32", "Monday"))
# # Returns: 2:02 PM, Monday

print(add_time("11:43 AM", "00:20"))
# # Returns: 12:03 PM

print(add_time("10:10 PM", "3:30"))
# # Returns: 1:40 AM (next day)

# print(add_time("11:43 PM", "24:20", "tueSday"))
# # Returns: 12:03 AM, Thursday (2 days later)

# print(add_time("6:30 PM", "205:12"))
# # Returns: 7:42 AM (9 days later)