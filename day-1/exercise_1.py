name = 'Taimoor'
age = 26
drinks_coffee = True
salary = 50000.0

print(name + ' is ' + str(age) + ' years old and ' + ('drinks' if drinks_coffee else 'does not drink') + ' coffee and earns Rs.'+ str(salary))

years_until_retirement = 60 - age
print(name + ' will retire in ' + str(years_until_retirement)+ ' years')

coffee_cups_in_a_day = 3
coffee_cups_in_a_week= coffee_cups_in_a_day * 7
coffee_expenses_per_week = coffee_cups_in_a_week * 150
print(name + ' spends Rs.'+ str(coffee_expenses_per_week)+ ' on coffee every week')

