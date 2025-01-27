class Employee:
    def __init__(self, name, salary, department):
        self.name = name
        self._salary = salary
        self.__department = department


    def mysalary(self, amount):
        amount = int(input("Сумма"))
        if amount > 0:
            self._salary += amount
        else:
            print("Зарплата відємна")


    def department(self):
        return self.__department



if __name__ == "__main__":
    res = Employee("Артем", 0, "Карта")
    print(res.mysalary(11))
    print(f"зарплата: {res._salary}")
    print(f"Відділ: {res.department()}")





