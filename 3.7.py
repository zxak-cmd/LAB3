# Конвертер валют: USD <-> RUB, EUR <-> RUB

# Задаем фиксированные курсы валют (для примера)
USD_TO_RUB = 92.50  # 1 доллар = 92.50 рублей
EUR_TO_RUB = 100.20 # 1 евро = 100.20 рублей

print("=== КОНВЕРТЕР ВАЛЮТ ===")
print("1. Доллары (USD) -> Рубли (RUB)")
print("2. Евро (EUR) -> Рубли (RUB)")
print("3. Рубли (RUB) -> Доллары (USD)")
print("4. Рубли (RUB) -> Евро (EUR)")

choice = input("\nВыберите направление конвертации (1-4): ")

if choice == "1":
    amount = float(input("Введите сумму в долларах: "))
    result = amount * USD_TO_RUB
    print(f"{amount:.2f} USD = {result:.2f} RUB")

elif choice == "2":
    amount = float(input("Введите сумму в евро: "))
    result = amount * EUR_TO_RUB
    print(f"{amount:.2f} EUR = {result:.2f} RUB")

elif choice == "3":
    amount = float(input("Введите сумму в рублях: "))
    result = amount / USD_TO_RUB
    print(f"{amount:.2f} RUB = {result:.2f} USD")

elif choice == "4":
    amount = float(input("Введите сумму в рублях: "))
    result = amount / EUR_TO_RUB
    print(f"{amount:.2f} RUB = {result:.2f} EUR")

else:
    print("Ошибка: выбран неверный пункт меню.")