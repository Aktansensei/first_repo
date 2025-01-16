def bayes_theorem():
    total_people = 100
    people_with_glasses = 30
    blue_eyes_with_glasses = 18
    blue_eyes_without_glasses = 12

    # A - wear glasses
    # B - has blue eyes

    P_A = people_with_glasses / total_people
    P_B_given_A = blue_eyes_with_glasses / people_with_glasses
    total_blue_eyes = blue_eyes_with_glasses + blue_eyes_without_glasses
    P_B = total_blue_eyes / total_people
    P_A_given_B = P_B_given_A * P_A / P_B
    return P_A_given_B 

print(bayes_theorem()*100, '%')

# import numpy as np # type: ignore
# import matplotlib.pyplot as plt # type: ignore

# # Параметры нормального распределения
# mu = 5  # Математическое ожидание
# sigma = 2  # Стандартное отклонение
# sample_size = 1000  # Размер выборки

# # Генерация выборки
# sample = np.random.normal(mu, sigma, sample_size)

# # Построение гистограммы
# plt.hist(sample, bins=30, color='skyblue', edgecolor='black', alpha=0.7)
# plt.title('Гистограмма нормального распределения')
# plt.xlabel('Значение')
# plt.ylabel('Частота')
# plt.grid(True, linestyle='--', alpha=0.6)
# plt.axvline(x=mu, color='red', linestyle='--', label='Среднее значение')
# plt.legend()
# plt.show()

from random import randint
def bignumber(n):
    res = 0
    for _ in range(n):
        res += randint(0, 1)
    return abs(res/n - 0.5)

print('подбрасывание монеты')
print('10 раз', bignumber(10))
print('100 раз', bignumber(100))
print('1000 раз', bignumber(1000))
print('10000 раз', bignumber(10000))