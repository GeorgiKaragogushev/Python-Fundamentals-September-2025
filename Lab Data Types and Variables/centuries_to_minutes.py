from math import floor

centuries = int(input())


total_years_in_centuries = centuries * 100

total_days_in_years = floor(total_years_in_centuries * 365.2422)

total_hours_in_days = total_days_in_years * 24

total_minutes_in_hours = total_hours_in_days * 60


print(f"{centuries} centuries = {total_years_in_centuries} years = {total_days_in_years} days = {total_hours_in_days} hours = {total_minutes_in_hours} minutes")