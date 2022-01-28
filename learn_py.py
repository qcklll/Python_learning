file = 'learning_python.txt'
# a = 0

with open(file) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.replace('can', 'not')
print(pi_string)

# while a < 3:
#     print(pi_string)
#     a += 1
