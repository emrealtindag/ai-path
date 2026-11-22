# loops

while, do-while and for loops, counters, sums, series, prime numbers, break and continue. all code uses `using namespace std;`.

---

## while loop

```cpp
while (condition) {
    // runs again and again as long as the condition is true
}
```

the condition is checked before every pass. if it is false at the start, the body never runs.

### how it runs

```cpp
#include <iostream>
using namespace std;

int main() {
    int i = 1;
    while (i <= 3) {
        cout << "Hello " << i << endl;
        i++;
    }
    return 0;
}
```

output:

```text
Hello 1
Hello 2
Hello 3
```

after the third pass `i` becomes 4, `4 <= 3` is false and the loop ends. if you forget `i++`, the condition never becomes false and the loop runs forever.

### problem 1: even numbers up to 30

```cpp
#include <iostream>
using namespace std;

int main() {
    int i = 0;
    while (i <= 30) {
        cout << i << endl;
        i = i + 2;
    }
    return 0;
}
```

### problem 2: multiples of 3 and counting them

prints 0, 3, 6, ..., 30 and counts how many numbers were printed.

```cpp
#include <iostream>
using namespace std;

int main() {
    int i = 0;
    int counter = 0;

    while (i <= 30) {
        cout << i << endl;
        counter++;
        i = i + 3;
    }
    cout << counter << " numbers" << endl; // 11 numbers
    return 0;
}
```

### problem 3: sum, count and mean of 1 to 10

```cpp
#include <iostream>
using namespace std;

int main() {
    int counter = 0;
    int x = 1;
    int sum = 0;

    while (x <= 10) {
        sum = sum + x;
        x++;
        counter++;
    }

    cout << "there are " << counter << " numbers on your screen" << endl; // 10
    cout << "the sum of listed numbers is " << sum << endl;              // 55
    cout << "the mean of numbers " << (double)sum / counter << endl;     // 5.5
    return 0;
}
```

check: 1 + 2 + ... + 10 = 10 * 11 / 2 = 55. without `(double)` the mean would be 5, because int / int cuts the decimals.

### problem 4: entering grades for a class

```cpp
#include <iostream>
using namespace std;

int main() {
    const int population = 10;
    int i = 1;
    double grade;
    double sum = 0;

    cout << "please start to enter grades one by one = " << endl;

    while (i <= population) {
        cout << "enter the grade " << i << " from the keyboard" << endl;
        cin >> grade;
        sum = sum + grade;
        i++;
    }

    cout << "average: " << sum / population << endl;
    return 0;
}
```

### problem 5: factorial with input check

the first `while` keeps asking until the user enters a number that is not negative.

```cpp
#include <iostream>
using namespace std;

int main() {
    int number;
    int factorial = 1;

    cout << "Enter a number from the keyboard = ";
    cin >> number;

    while (number < 0) {
        cout << "enter positive ";
        cin >> number;
    }

    int start = 1;
    while (start <= number) {
        factorial = factorial * start;
        start++;
    }

    cout << number << "! = " << factorial << endl;
    return 0;
}
```

the same idea with a counter, 5! = 1 * 2 * 3 * 4 * 5:

```cpp
int prod = 1;
int i = 1;
int counter = 0;

while (i <= 5) {
    counter++;
    prod = prod * i;
    i++;
}
cout << counter << "! = " << prod << endl; // 5! = 120
```

### problem 6: greatest common divisor

try every number `f` from 2 up to the smaller input. if both numbers divide by `f`, save it. the last saved one is the biggest.

```cpp
#include <iostream>
using namespace std;

int main() {
    int number1, number2;
    cout << "enter two numbers ";
    cin >> number1 >> number2;

    int gcd = 1;
    int f = 2;

    while (f <= number1 && f <= number2) {
        if (number1 % f == 0 && number2 % f == 0) {
            gcd = f;
        }
        f++;
    }

    cout << "the greatest common divisor for " << number1 << " and " << number2 << " is " << gcd << endl;
    return 0;
}
```

### problem 7: addition quiz

asks the same question until the answer is correct.

```cpp
#include <iostream>
#include <cstdlib>
#include <ctime>
using namespace std;

int main() {
    srand(time(0));
    int number1 = rand() % 10;
    int number2 = rand() % 10;
    int answer;

    cout << "what is " << number1 << " + " << number2 << " ? ";
    cin >> answer;

    while (number1 + number2 != answer) {
        cout << "its wrong" << endl;
        cout << "what is " << number1 << " + " << number2 << " ? ";
        cin >> answer;
    }

    cout << "you got this" << endl;
    return 0;
}
```

### problem 8: guess the magic number

`guess` starts at -1 so the loop runs at least once (the magic number is never -1).

```cpp
#include <iostream>
#include <cstdlib>
#include <ctime>
using namespace std;

int main() {
    srand(time(0));
    int guess = -1;
    int magicNumber = rand() % 101; // 0 to 100

    while (guess != magicNumber) {
        cout << "Enter a number between [0-100] = ";
        cin >> guess;

        if (guess == magicNumber)
            cout << "Yes you got it..." << endl;
        else if (guess < magicNumber)
            cout << "Your guess is too low" << endl;
        else
            cout << "Your guess is too high" << endl;
    }

    cout << "The magic number was " << magicNumber << endl;
    return 0;
}
```

---

## do-while loop

```cpp
do {
    // runs first
} while (condition); // then checks the condition
```

the body runs once before the condition is checked, so it always runs at least one time. good for menus and for asking input until it is valid. don't forget the `;` after `while (...)`.

### problem 9: add numbers until 0

```cpp
#include <iostream>
using namespace std;

int main() {
    int sum = 0;
    int number;

    do {
        cout << "enter a number ";
        cin >> number;
        sum = sum + number;
    } while (number != 0);

    cout << "sum: " << sum << endl;
    return 0;
}
```

### problem 10: atm menu

```cpp
#include <iostream>
using namespace std;

int main() {
    int choice;

    do {
        // the menu is printed at least once, before the condition is checked
        cout << "\n--- MENU ---" << endl;
        cout << "1. Check Balance" << endl;
        cout << "2. Deposit Money" << endl;
        cout << "0. Exit" << endl;
        cout << "Your choice: ";
        cin >> choice;

        if (choice == 1) {
            cout << "Your balance: 500 TL" << endl;
        } else if (choice == 2) {
            cout << "Deposit selected." << endl;
        } else if (choice != 0) {
            cout << "Invalid choice! Please try again." << endl;
        }
        // goes back to the top until the user enters 0
    } while (choice != 0);

    cout << "Program closed." << endl;
    return 0;
}
```

### problem 11: sum of even and odd numbers

```cpp
#include <iostream>
using namespace std;

int main() {
    int number;
    char choice;
    int sumOfEvenNumbers = 0;
    int sumOfOddNumbers = 0;

    do {
        cout << "enter a number" << endl;
        cin >> number;

        if (number % 2 == 0)
            sumOfEvenNumbers = sumOfEvenNumbers + number;
        else
            sumOfOddNumbers = sumOfOddNumbers + number;

        cout << "do you want to continue " << endl;
        cin >> choice;
    } while (choice == 'y' || choice == 'Y');

    cout << "the sum of even numbers is " << sumOfEvenNumbers << endl;
    cout << "the sum of odd numbers is " << sumOfOddNumbers << endl;
    return 0;
}
```

---

## for loop

```cpp
for (initialization; condition; increment) {
    // code
}
```

order of steps:

1. initialization runs once at the start.
2. the condition is checked. if it is false, the loop ends.
3. the code inside runs.
4. the increment runs, then back to step 2.

### tracing a for loop

```cpp
#include <iostream>
using namespace std;

int main() {
    int i;
    for (i = 1; i <= 3; i++) {
        cout << "Hello" << i << endl;
    }
    cout << i << endl;
    return 0;
}
```

- first: i = 1, 1 <= 3 is true, prints Hello1, then i++ makes i = 2
- second: i = 2, 2 <= 3 is true, prints Hello2, then i = 3
- third: i = 3, 3 <= 3 is true, prints Hello3, then i = 4
- i = 4, 4 <= 3 is false, the loop ends and nothing is printed
- the `cout << i` after the loop prints 4. this only works because `i` was declared outside the loop. with `for (int i = 1; ...)`, `i` doesn't exist after the loop.

### while vs for

the same loop both ways:

```cpp
int j = 0;
while (j <= 10) {
    cout << j << endl;
    j++;
}

for (int i = 0; i <= 10; i++) {
    cout << i << endl;
}
```

### problem 12: sum and count with for

```cpp
#include <iostream>
using namespace std;

int main() {
    int sum = 0;
    int counter = 0;

    for (int i = 0; i <= 10; i++) {
        cout << i << endl;
        sum = sum + i;
        counter++;
    }

    cout << "sum: " << sum << " count: " << counter << endl; // sum: 55 count: 11
    return 0;
}
```

### problem 13: factorial with for

```cpp
#include <iostream>
using namespace std;

int main() {
    int number;
    cout << "enter a number" << endl;
    cin >> number;

    int factorial = 1;
    for (int i = 1; i <= number; i++) {
        factorial = factorial * i;
    }

    cout << number << "! = " << factorial << endl;
    return 0;
}
```

### problem 14: running the factorial 3 times

the whole program is put inside a loop that runs 3 times. it can be a `while` or a `for (counter = 1; counter <= 3; counter++)`.

```cpp
#include <iostream>
using namespace std;

int main() {
    int counter = 1;

    while (counter <= 3) { // tries 3 times
        int number;
        cout << "enter a number" << endl;
        cin >> number;

        int factorial = 1;
        for (int i = 1; i <= number; i++) {
            factorial = factorial * i;
        }

        cout << number << "! = " << factorial << endl;
        counter++;
    }
    return 0;
}
```

### problem 15: multiplication table

one number:

```cpp
#include <iostream>
using namespace std;

int main() {
    int number;
    cout << "enter a number" << endl;
    cin >> number;

    for (int i = 1; i <= 10; i++) {
        cout << i << " * " << number << " = " << i * number << endl;
    }
    return 0;
}
```

1 to 10, a loop inside a loop. for every value of `counter` the inner `for` runs 10 times:

```cpp
#include <iostream>
using namespace std;

int main() {
    int counter = 1;

    while (counter <= 10) {
        for (int i = 1; i <= 10; i++) {
            cout << i << " * " << counter << " = " << i * counter << endl;
        }
        counter++;
        cout << "*****" << endl;
    }
    return 0;
}
```

### problem 16: power without pow()

2^3 = 2 * 2 * 2, so multiply `base` by itself `power` times. the `do-while`s keep asking until the values are not negative.

```cpp
#include <iostream>
using namespace std;

int main() {
    int base, power;

    do {
        cout << "enter a positive base value" << endl;
        cin >> base;
    } while (base < 0);

    do {
        cout << "enter a positive power value" << endl;
        cin >> power;
    } while (power < 0);

    int product = 1;
    for (int i = 1; i <= power; i++) {
        product = product * base;
    }

    cout << base << " raised to the power of " << power << " is " << product << endl;
    return 0;
}
```

### problem 17: 1 + 1/2 + 1/3 + ... + 1/n

```cpp
#include <iostream>
using namespace std;

int main() {
    int n;
    do {
        cout << "enter the positive n" << endl;
        cin >> n;
    } while (n < 0);

    double sum = 0;
    for (int i = 1; i <= n; i++) {
        sum = sum + (1.0 / i); // 1 / i would be 0 for every i > 1
    }

    cout << "Sum of the sequence is " << sum << endl;
    return 0;
}
```

### problem 18: 1 - 1/2 + 1/3 - 1/4 + ...

`p` flips between 1 and -1 every pass, so the signs alternate.

```cpp
#include <iostream>
using namespace std;

int main() {
    int n;
    int p = 1;
    do {
        cout << "enter the positive n" << endl;
        cin >> n;
    } while (n < 0);

    double sum = 0;
    for (int i = 1; i <= n; i++) {
        sum = sum + (1.0 / i) * p;
        p = -p;
    }

    cout << "Sum of the sequence is " << sum << endl;
    return 0;
}
```

---

## break and continue

- `break`: leaves the loop completely.
- `continue`: skips the rest of this pass and goes to the next one.

```cpp
#include <iostream>
using namespace std;

int main() {
    for (int i = 1; i <= 5; i++) {
        if (i == 3)
            break;
        cout << i << endl; // 1 2, the loop stops at 3
    }

    for (int i = 1; i <= 5; i++) {
        if (i == 3)
            continue;
        cout << i << endl; // 1 2 4 5, only 3 is skipped
    }
    return 0;
}
```

---

## prime numbers

a prime number divides only by 1 and itself. 1 is not prime.

### problem 19: is it prime

start with `flag = true`. try every number from 2 to `number - 1`. if one of them divides the number, set `flag = false` and `break`, there is no need to keep checking.

```cpp
#include <iostream>
using namespace std;

int main() {
    int number;
    do {
        cout << "Enter a positive number = ";
        cin >> number;
    } while (number < 0);

    bool flag = true;
    for (int i = 2; i <= number - 1; i++) {
        if (number % i == 0) {
            flag = false;
            break;
        }
    }

    if ((flag == true) && (number != 1))
        cout << number << " is a prime number" << endl;
    else
        cout << number << " is not a prime number" << endl;
    return 0;
}
```

for 7 the loop checks 2, 3, 4, 5, 6. none of them divide 7, so it is prime. for 6 it stops at 2 because 6 % 2 == 0.

careful with 0: the loop doesn't run, `flag` stays true and 0 would be called prime. writing `number > 1` instead of `number != 1` fixes both 0 and 1.

### problem 20: the first 50 prime numbers, 10 per line

```cpp
#include <iostream>
using namespace std;

int main() {
    const int NUMBER_OF_PRIMES = 50;
    const int NUMBER_OF_PRIMES_PER_LINE = 10;
    int counter = 0;
    int number = 2;

    cout << "The first 50 prime numbers are = " << endl;

    while (counter < NUMBER_OF_PRIMES) {
        bool isPrime = true;

        for (int i = 2; i <= number / 2; i++) {
            if (number % i == 0) {
                isPrime = false;
                break;
            }
        }

        if (isPrime) {
            counter++;
            if (counter % NUMBER_OF_PRIMES_PER_LINE == 0)
                cout << number << endl;
            else
                cout << number << " ";
        }

        number++;
    }
    return 0;
}
```

how it works:

- `number` starts at 2 and goes up by one every pass of the `while`.
- the `for` checks if `number` is prime. the `while` keeps going until 50 primes have been found.
- `counter % 10 == 0` is true at the 10th, 20th, 30th... prime, so a new line starts after every 10 numbers.
- inside the loop it has to be `number % i`, not `number % 2`. with `% 2` it checks the same thing on every pass and only tests if the number is even.
- why `number / 2` is enough: a number can't be divided by anything bigger than its half, except itself. for example 24 / 2 = 12, and 24 has no divisor between 12 and 24. so checking up to `number / 2` gives the same answer as checking up to `number - 1` with about half the work.
