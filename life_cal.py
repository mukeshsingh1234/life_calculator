#just say that we live for 90 years
# 1 year = 365 days
# 1 year = 12 months
# 1 year = 52 weeks
age = int(input("Enter you current age"))
month_limit = 90*12
week_limit = 90*52
day_limit = 90*365
month_rem = month_limit - (age*12)
week_rem = week_limit - (age*52)
day_rem = day_limit - (age*365)
print(f"You have {day_rem} days, {week_rem} weeks, and {month_rem} months left." )
