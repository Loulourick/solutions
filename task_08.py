from datetime import date
def century_message(name, age, current_year):
    year = current_year - age + 100
    return f"{name}, тебе исполнится 100 лет в {year} году"
if __name__ == "__main__":
    current_year = date.today().year

    name = input("Введите имя: ")
    age = int(input("Введите возраст: "))

    century_message(name, age, current_year)
