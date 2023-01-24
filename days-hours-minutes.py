#lfb
user_input_seconds = int(input("write the seconds:  "))

seconds_to_print_function = user_input_seconds % 60

minutes = user_input_seconds // 60

minutes_to_print_function = minutes % 60

hours = minutes // 60

hours_to_print_function = hours % 24

days = hours // 24

print(days, "days", hours_to_print_function , "hours", minutes_to_print_function, "minutes", seconds_to_print_function, "seconds")
