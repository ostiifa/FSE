previous = int(input("Введите предыдущее показание счетика "))
current = int(input("Введите нынешнее показание счетчика "))
if current >= previous:
    used = current - previous
else:
    used = (10000 - previous) + current
if used <= 300:
    payment = 21
elif used <= 600:
    payment = 21 + (used - 300) * 0.06
elif used <= 800:
    payment = 21 + 300 * 0.06 + (used - 600) * 0.04
else:
    payment = 21 + 300 * 0.06 + 200 * 0.04 + (used - 800) * 0.025
if used > 0:
    avg_price = payment / used
else:
    avg_price = 0
payment = round(payment, 2)
avg_price = round(avg_price, 2)
print(f"Предыдущее {previous} Текущее {current} Использовано {used} К оплате {payment}Ср. цена m^3 {avg_price}")