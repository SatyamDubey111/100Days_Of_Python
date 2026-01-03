from operator import truediv

#PEDMASLR

bmi = 84 / 1.65 ** 2
print(bmi)  # 30.85399449035813
#  any number into a integer

print(int(bmi)) # 30

print(round(bmi)) # 31 rounding up to nearest highest number

print(round(bmi, 2)) # 30.85  rounding up upto two decimal point value

# assignment opreator

score = 0

# user scores a point
# score = score + 1
score += 1
score -= 1
print(score)

# f-strings
print("your score is " + str(score))  # only score will produce type error


score = 0
height  = 1.4
is_winning = True

# we use f-string for escaping to use lot of + and more

print(f"your score is  = {score}, your height is {height}, you are winning is {is_winning}")