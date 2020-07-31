# put your python code here
import math
students_c1 = int(input())
students_c2 = int(input())
students_c3 = int(input())

desks_c1 = students_c1 / 2
desks_c2 = students_c2 / 2
desks_c3 = students_c3 / 2

desks_to_buy = math.ceil(desks_c1) + math.ceil(desks_c2) + math.ceil(desks_c3)
print(desks_to_buy)
