# ******************************************************************
#                       Fizz Buzz                                  #
# ******************************************************************

def  fizz_buzz(value: int) -> int:
    """
    The function returns the following "fizz", "buzz" or "fizz buzz"
    :param n: range of values starting from 1  to 100 included
    :return: "fizz" if n%3, "buzz" if n%5, "fizz buzz" n%5 & n%3
    """
    if (value % 15 == 0) :
            return  "fizz buzz"

    elif value % 3 == 0:
            return  "fizz"
    elif value % 5 == 0:
            return  "buzz"
    else:
        return str(value)


input("Play Fizz Buzz. Press ENTER to start")
print()

next_number = 0
while next_number < 99:
    next_number += 1
    print(fizz_buzz(next_number))
    next_number += 1
    correct_answer = fizz_buzz(next_number)
    players_answer = input("Your go: ")
    if players_answer != correct_answer:
        print("You lose, the correct answer was {}".format(correct_answer))
        break
else:
    print("Well done, you reached {}".format(next_number))
