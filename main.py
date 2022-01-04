# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇

# frist divide values into two variables 
frist = (two_digit_number[0])
second = (two_digit_number[1])
# convert string into int data tyep
new_frist = int(frist)
new_second = int(second)
# get sum of the two numbers of the adding +
value1 = int(new_frist + new_second)
# Print as requested way - 2 method are showing in the below
print(frist + " + " + second + " = " + str(value1))
print(str(new_frist) + " + " + str(new_second) + " = " + str(value1))

print(3 * 3 + 3 / 3 - 3)


print(round(8 / 3, 2))

print(6 + 4 / 2 - (1 * 2))

a = int("5") / int(2.7)
print(a)
print(type(a))
