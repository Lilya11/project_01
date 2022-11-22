# ЗАДАЧА №5
# Зарплата сотрудника составляет salary руб.
# Расходы на проживание превышают зарплату и составляют expenses руб. в месяц
# Рост цен ежемесячно увеличивает расходы на 3%, кроме первого месяца.
# Напишите скрипт расчета суммы денег, которую необходимо взять в долг.
# чтобы можно было прожить ближайший год (12 месяцев).
#  Формат вывода:
# Необходимо взять в долг ХХХ.ХХ рублей

salary, expenses = 10000, 12000
# expenses_living - расходы на проживание
# expenses_total - все расходы
expenses_living, expenses_total = expenses, expenses
i = 1
while i < 12:
    expenses_living = expenses_living * 1.03
    expenses_total = expenses_total + expenses_living
    i += 1
result = expenses_total - salary * 12
print("Необходимо взять в долг -", result, "рублей")

