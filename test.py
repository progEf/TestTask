import numpy as np


class TestTask:
    def __init__(self, size):
        self.size = size
        self.array = np.random.randint(-100, 100, size=(size, size))

    def func(self):
        MinValue = []
        String = ''
        for ind, row in enumerate(self.array):
            point = " "
            if self.array.min() in row:  # Find the minimum value and add a star to the beginning
                point = '*'
                MinValue.append(ind + 1)
            MinimumPositive = []
            replacements = 0
            count = 1
            for i, num in enumerate(row):
                if num >= 0:
                    MinimumPositive.append(num)  # Finding the positive value
                point += f"{num:4d}"
                if i < self.size - 1:
                    i += 1
                if (row[i] > 0 and row[i - 1] > 0) or (row[i] < 0 and row[i - 1] < 0):
                    count += 1
                    if count == 3:  # there were 3 or more consecutive + or - numbers
                        replacements += 1  # Plus one coincidence
                        count = 1  # Сбрасываем счетчик после замены
                else:
                    count = 1
            String += f'{point} | {min(MinimumPositive) if any(MinimumPositive) else None} | {replacements}\n'
        return String, MinValue


task = TestTask(size=10).func()
print(f'Строка, содержащую минимальное числа:' + ', '.join(f'{item}' for item in task[1]))
print('Min|-----------------List-----------------|Min+|in a row')
print(task[0])
print('--------------------------------------------------------')
# if array.min() in row:
#    point = '*'
