import math


def split_check(total, number_of_people):
  if number_of_people <= 1:
    raise ValueError("More than one person is required to split the check")
  return math.ceil(total/number_of_people)

try:
  total_due = float(input('What is the budget of the meal?'))
  number_of_people = int(input('How many people?'))
  amount_due = split_check(total_due, number_of_people)
except ValueError as err:
  print("Ooops, that's not a valid number")
  print('({})'.format(err))
else:
  print('Each person owes ${}'.format(amount_due))
