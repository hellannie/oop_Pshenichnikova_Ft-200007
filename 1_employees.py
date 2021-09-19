# -*- coding: utf-8 -*-

Workers = []

class Employee:
    name = ''
    post = ''
    age = 18
    pay = 12400

    def __init__(self, name, post, age, pay):
        self.name = name
        self.post = post
        self.age = age
        self.pay = pay
        Workers.append(self)


def average(people):
    s = 0
    for p in people:
        s += p.Pay
    print("\nСредняя заработная плата составляет {} рублей".format(s / len(people)))


def estimate_salary(people):
    print("Работники с заработной платой выше среднего:")
    for p in people:
        if p.Pay > summary / len(Workers):
            print(p.name, ",", p.Post)

def employee_input(number):
    for i in range(0, number):
        print("Введите данные о новом сотруднике")
        temp_fio = input("Имя сотрудника:")
        temp_post = input("Должность:")
        temp_age = int(input("Возраст:"))
        temp_salary = int(input("Заработная плата:"))
        Employee(temp_fio, temp_post, temp_age, temp_salary)


n = int(input("Сколько сотрудников нужно ввести в систему?"))
employee_input(n)
summary = 0
for worker in Workers:
    print('ФИО:', worker.name, ' Должность:', worker.Post, ' Возраст:', worker.age, ' Заработная плата:', worker.Pay)
    summary += int(worker.Pay)
average(Workers)
estimate_salary(Workers)
