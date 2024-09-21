from random import choice

def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name, 'w', encoding='utf-8') as f1:
            for el in data_set:
                f1.write(str(el))
                f1.write('\n')
    return write_everything


class MysticBall:
    def __init__(self, *words):
        self.words = words

    def __call__(self):
        return choice(self.words)


first = 'Мама мыла раму'
second = 'Рамена мало было'
func = lambda x, y: x == y
result = list(map(func, first, second))
print(result)

write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

first_ball = MysticBall('Да', 'Нет', 'Наверное')
for i in range(3):
    print(first_ball())
