import re
# s = "Sound Level: -11.7 db or 15.2 or 8 db"
# result = re.findall(r"[-+]?\d*\.\d+|\d+", s)
# print (result)

def generator_numbers(text):
    numbers = re.findall(r"[-+]?\d*\.\d+|\d+", text)

    for i in numbers:
        # print('i: ', i)
        yield i

    # numbers = [text.split('[0-9].[0-9]', 'text') for i in text]
    # yield numbers
    # print (numbers)

def sum_profit():
    sum = 0.0
    for number in generator_numbers(text):
        sum += float(number)

    return sum


text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
# print(generator_numbers(text))

total_income = sum_profit()
print(f"Загальний дохід: {total_income}")


