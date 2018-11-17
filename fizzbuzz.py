def fizzbuzz_convert(number):
    if number % 15 == 0:
        return "FizzBuzz"

    if number % 3 == 0:
        return 'Fizz'

    if number % 5 == 0:
        return 'Buzz'

    return str(number)


"""
while True:
    print(fizzbuzz_convert(number))
    number += 1

    if number == 101:
        break


"""

for i in range(101):
    print(fizzbuzz_convert(i))
# インライン化
