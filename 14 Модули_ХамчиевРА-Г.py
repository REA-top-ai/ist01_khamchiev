from datetime import*
current_time = datetime.now()
print(current_time)

from random import*
random_list = [randint(1, 100) for _ in range(101)]
print(random_list)
randomer_number = choice(random_list)
print(randomer_number)

import matplotlib.pyplot as plt
import random
number_a = list(range(1, 13))
number_b = random.sample(range(1000), 12)
plt.plot(number_a, number_b, 'o-')
plt.show()