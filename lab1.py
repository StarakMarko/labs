# my number is 23
import math


# table 1 question 1
color = "синій"


print("колір", color)


# table 1 question 2
is_voter = False
is_non_citizen = True


voter_and_citizen = is_voter and is_non_citizen
voter_or_citizen = is_voter or is_non_citizen
not_voter = not is_voter
not_non_citizen = not is_non_citizen


print("and:", voter_and_citizen)
print("or:", voter_or_citizen)
print("not voter:", not_voter)
print("not non citizen:", not_non_citizen)


# table 1 question 3
is_raining = True
is_snowing = True


raining_or_snowing = is_raining or is_snowing


print("raining or snowing:", raining_or_snowing)


# table 2 question 1
x = 4.597
y = 7.954


equation = (3.6*(math.sin(x) + math.cos(y**2))**3
            - math.tan(math.sqrt(math.sin(x)**2 + math.cos(y)**2)))


print("equation=", equation)