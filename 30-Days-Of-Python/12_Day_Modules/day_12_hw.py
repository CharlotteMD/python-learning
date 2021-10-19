import random
import string

id = ''.join([random.choice(string.ascii_letters
            + string.digits) for n in range(6)])
print(id)

number_of_colors = 8

color = ["#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)])
             for i in range(number_of_colors)]
print(color)


