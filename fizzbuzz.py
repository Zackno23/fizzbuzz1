def fizzbuzz_convert(number):
    if number % 15 == 0:
        return "FizzBuzz"
    elif number % 3 == 0:
        return 'Fizz'
    elif number % 5 == 0:
        return 'Buzz'
    else:
        return str(number)


number = 1

while True:
    print(fizzbuzz_convert(number))
    number += 1

    if number == 101:
        break
