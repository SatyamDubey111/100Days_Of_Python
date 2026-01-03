from ftplib import parse150

print("my age: " + str(12))  # can only concatenate str (not "int") to str
print(123 + 456)
print(7 - 3)
print(3 + 2)
print(6 / 3) # here in case of division  actually end up  with a floating point number
# 2.0 we are getting float instead of integer this is python default behaviour (its something called implicit type casting )
#  Because python is implicitly convert the value in floating point number
#  print(5 / 3) # 1.66666
#  print(5// 3)  # 1  its

print(5 / 3) # 1.6666
print(5 // 3) # 1 > its be a quite dangerous when we are using scientific data

print(2 ** 2) # 4

#PEMDAS l->r  () ** * /  + -  -> priority
print(3 * 3 + 3 / 3 -3) # 7.0
print(3 * 3 + 3 / 3 -7) # 3.0
