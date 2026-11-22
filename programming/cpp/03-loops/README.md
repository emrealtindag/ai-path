# loops

iteration constructs, condition-based loops, counter loops, state tracing, series summations, prime number algorithms, and flow control in c++ (all examples assume using namespace std;).

---

## while loops and condition-based iteration

a `while` loop checks its condition before executing the loop body. if the condition evaluates to false at the start, the body never runs.

```cpp
while (condition) {
    // executes repeatedly while condition evaluates to true
}
```

### problem 1: even numbers up to 30

prints even numbers starting from 0 up to 30:

```cpp
#include <iostream>
using namespace std;

int main() {
    int i = 0;
    while (i <= 30) {
        cout << i << " ";
        i += 2;
    }
    cout << "\n";
    return 0;
}
```

### problem 2: multiples of 3 with step counter

prints multiples of 3 up to 30 and counts total elements using an accumulator counter:

```cpp
#include <iostream>
using namespace std;

int main() {
    int counter = 0;
    int i = 0;

    while (i <= 30) {
        cout << i << " ";
        counter++;
        i += 3;
    }
    cout << "\ntotal elements: " << counter << "\n"; // outputs 11 numbers (0, 3, 6, ..., 30)
    return 0;
}
```

### problem 3: counting steps and calculating the mean (average)

sums integers from 1 to 10, counts the iterations, and calculates the floating-point mean:

```cpp
#include <iostream>
using namespace std;

int main() {
    int counter = 0;
    int x = 1;
    int sum = 0;

    while (x <= 10) {
        sum += x;
        x++;
        counter++;
    }

    double mean = static_cast<double>(sum) / counter;
    cout << "sum: " << sum << ", count: " << counter << ", mean: " << mean << "\n";
    // sum: 55, count: 10, mean: 5.5
    return 0;
}
```

### problem 4: student grade accumulator with constant population

prompts the user to enter grades for a fixed class population one by one and computes the class total:

```cpp
#include <iostream>
using namespace std;

int main() {
    const int population = 10;
    int i = 1;
    double grade;
    double sum = 0.0;

    cout << "please start entering grades one by one:\n";

    while (i <= population) {
        cout << "enter grade " << i << " from keyboard: ";
        cin >> grade;
        sum += grade;
        i++;
    }

    cout << "total grade sum: " << sum << "\n";
    cout << "class average: " << (sum / population) << "\n";
    return 0;
}
```

### problem 5: factorial with positive input validation loop

validates that user input is non-negative before computing factorial:

```cpp
#include <iostream>
using namespace std;

int main() {
    int number;
    cout << "enter a number: ";
    cin >> number;

    // input validation loop: repeats until non-negative number is entered
    while (number < 0) {
        cout << "enter a positive number: ";
        cin >> number;
    }

    int factorial = 1;
    int start = 1;
    while (start <= number) {
        factorial *= start;
        start++;
    }
    cout << number << "! = " << factorial << "\n";
    return 0;
}
```

### problem 6: greatest common divisor (gcd / ebob)

finds the largest positive integer dividing two inputs without remainder:

```cpp
#include <iostream>
using namespace std;

int main() {
    int num1, num2;
    cout << "enter two numbers: ";
    cin >> num1 >> num2;

    int gcd = 1;
    int f = 2;

    while (f <= num1 && f <= num2) {
        if (num1 % f == 0 && num2 % f == 0) {
            gcd = f;
        }
        f++;
    }
    cout << "greatest common divisor: " << gcd << "\n";
    return 0;
}
```

### problem 7: arithmetic quiz loop with random numbers

generates two random numbers below 10 and prompts repeatedly until the user answers correctly:

```cpp
#include <iostream>
#include <cstdlib>
#include <ctime>
using namespace std;

int main() {
    srand(time(0));
    int n1 = rand() % 10;
    int n2 = rand() % 10;

    int answer;
    cout << "what is " << n1 << " + " << n2 << "? ";
    cin >> answer;

    while (n1 + n2 != answer) {
        cout << "wrong answer! try again: ";
        cin >> answer;
    }
    cout << "correct! you got this.\n";
    return 0;
}
```

### problem 8: guess the magic number (0 to 100)

generates a random target and provides high/low hints until guessed:

```cpp
#include <iostream>
#include <cstdlib>
#include <ctime>
using namespace std;

int main() {
    srand(time(0));
    int magic_number = rand() % 101; // 0 to 100
    int guess = -1;

    while (guess != magic_number) {
        cout << "enter a number between 0 and 100: ";
        cin >> guess;

        if (guess == magic_number) {
            cout << "yes you got it! magic number was " << magic_number << "\n";
        } else if (guess < magic_number) {
            cout << "your guess is too low\n";
        } else {
            cout << "your guess is too high\n";
        }
    }
    return 0;
}
```

---

## do-while loops (post-condition iteration)

a `do-while` loop executes its body first, then evaluates the condition at the end. this guarantees that the loop runs at least once, making it ideal for menus and input validation.

```cpp
do {
    // executes at least once before condition is evaluated
} while (condition);
```

### problem 9: sum numbers until user enters zero

```cpp
#include <iostream>
using namespace std;

int main() {
    int number;
    int sum = 0;

    do {
        cout << "enter a number (0 to stop): ";
        cin >> number;
        sum += number;
    } while (number != 0);

    cout << "total sum: " << sum << "\n";
    return 0;
}
```

### problem 10: interactive atm banking menu

redisplays account actions until user selects 0 to exit:

```cpp
#include <iostream>
using namespace std;

int main() {
    int choice;
    int balance = 500;

    do {
        cout << "\n--- atm menu ---\n";
        cout << "1. check balance\n";
        cout << "2. deposit money\n";
        cout << "0. exit\n";
        cout << "your choice: ";
        cin >> choice;

        if (choice == 1) {
            cout << "current balance: " << balance << " tl\n";
        } else if (choice == 2) {
            int deposit;
            cout << "enter deposit amount: ";
            cin >> deposit;
            balance += deposit;
            cout << "updated balance: " << balance << " tl\n";
        } else if (choice != 0) {
            cout << "invalid selection, please retry.\n";
        }
    } while (choice != 0);

    cout << "session closed.\n";
    return 0;
}
```

### problem 11: even and odd numbers accumulator with continue prompt

reads numbers, separates evens and odds, and prompts whether to continue:

```cpp
#include <iostream>
using namespace std;

int main() {
    int num;
    char choice;
    int sum_even = 0;
    int sum_odd = 0;

    do {
        cout << "enter a number: ";
        cin >> num;

        if (num % 2 == 0) {
            sum_even += num;
        } else {
            sum_odd += num;
        }

        cout << "do you want to continue (y/n)? ";
        cin >> choice;
    } while (choice == 'y' || choice == 'Y');

    cout << "sum of evens: " << sum_even << "\n";
    cout << "sum of odds: " << sum_odd << "\n";
    return 0;
}
```

---

## for loops and iteration state tracing

a `for` loop packages initialization, condition, and increment into a concise header:

```cpp
for (initialization; condition; increment) {
    // body
}
```

### execution lifecycle

1. **initialization**: runs once before the first pass.
2. **condition**: evaluated before every pass. if false, loop exits immediately.
3. **body**: executes while condition is true.
4. **increment / update**: executes after each body pass, updating loop control variables.
5. steps 2-4 repeat until condition fails.

for `for (int i = 1; i <= 3; i++) cout << "hello " << i;`:
- pass 1: $i = 1$, condition $1 \le 3$ true -> prints `"hello 1"`, $i++ \to 2$
- pass 2: $i = 2$, condition $2 \le 3$ true -> prints `"hello 2"`, $i++ \to 3$
- pass 3: $i = 3$, condition $3 \le 3$ true -> prints `"hello 3"`, $i++ \to 4$
- exit check: $i = 4$, condition $4 \le 3$ false -> loop terminates.
- if $i$ is declared outside the loop, its post-loop value is **4**.

### problem 12: repeating a task multiple times using nested outer loop

running an inner factorial computation 3 consecutive times via an outer counter loop:

```cpp
#include <iostream>
using namespace std;

int main() {
    int counter = 1;

    while (counter <= 3) {
        cout << "\n[attempt " << counter << " of 3]\n";

        int number;
        cout << "enter a positive number: ";
        cin >> number;

        int factorial = 1;
        for (int i = 1; i <= number; i++) {
            factorial *= i;
        }
        cout << number << "! = " << factorial << "\n";
        counter++;
    }
    return 0;
}
```

### problem 13: multiplication tables

single number table:

```cpp
#include <iostream>
using namespace std;

int main() {
    int number = 5;
    for (int i = 1; i <= 10; i++) {
        cout << i << " * " << number << " = " << (i * number) << "\n";
    }
    return 0;
}
```

full 1 to 10 nested multiplication grid:

```cpp
#include <iostream>
using namespace std;

int main() {
    for (int i = 1; i <= 10; i++) {
        for (int j = 1; j <= 10; j++) {
            cout << (i * j) << "\t";
        }
        cout << "\n";
    }
    return 0;
}
```

### problem 14: integer power computation without pow()

computes $base^{power}$ using loops and multiplications:

```cpp
#include <iostream>
using namespace std;

int main() {
    int base, power;
    do {
        cout << "enter positive base: ";
        cin >> base;
    } while (base < 0);

    do {
        cout << "enter positive power: ";
        cin >> power;
    } while (power < 0);

    int product = 1;
    for (int i = 1; i <= power; i++) {
        product *= base;
    }
    cout << base << " raised to the power of " << power << " is " << product << "\n";
    return 0;
}
```

### problem 15: harmonic and alternating series summation

harmonic series:
$$\sum_{i=1}^n \frac{1}{i} = 1 + \frac{1}{2} + \frac{1}{3} + \dots + \frac{1}{n}$$

```cpp
#include <iostream>
using namespace std;

int main() {
    int n = 10;
    double sum = 0.0;
    for (int i = 1; i <= n; i++) {
        sum += (1.0 / i);
    }
    cout << "harmonic sum: " << sum << "\n";
    return 0;
}
```

alternating series:
$$\sum_{i=1}^n \frac{(-1)^{i+1}}{i} = 1 - \frac{1}{2} + \frac{1}{3} - \frac{1}{4} + \dots$$

```cpp
#include <iostream>
using namespace std;

int main() {
    int n = 6;
    double sum = 0.0;
    int p = 1; // sign toggler

    for (int i = 1; i <= n; i++) {
        sum += (1.0 / i) * p;
        p = -p; // flips between +1 and -1
    }
    cout << "alternating sum: " << sum << "\n";
    return 0;
}
```

### problem 16: prime number checker (flag method)

checks whether a positive integer is prime using a boolean flag and early break:

```cpp
#include <iostream>
using namespace std;

int main() {
    int number;
    do {
        cout << "enter positive number: ";
        cin >> number;
    } while (number < 0);

    bool is_prime = true;

    if (number <= 1) {
        is_prime = false;
    } else {
        for (int i = 2; i < number; i++) {
            if (number % i == 0) {
                is_prime = false;
                break; // divisor found, exit early
            }
        }
    }

    if (is_prime) {
        cout << number << " is a prime number\n";
    } else {
        cout << number << " is not a prime number\n";
    }
    return 0;
}
```

### problem 17: generating the first 50 prime numbers

prints the first 50 prime numbers, formatted 10 per row using nested loops:

> **algorithmic optimization note:** the inner loop evaluates divisors up to `number / 2` (or $\sqrt{number}$). no composite integer can have a divisor larger than half its value, which cuts loop iterations in half compared to testing all numbers up to $n-1$.

```cpp
#include <iostream>
using namespace std;

int main() {
    const int number_of_primes = 50;
    const int primes_per_line = 10;

    int count = 0;
    int number = 2;

    cout << "the first 50 prime numbers are:\n";

    while (count < number_of_primes) {
        bool is_prime = true;

        for (int i = 2; i <= number / 2; i++) {
            if (number % i == 0) {
                is_prime = false;
                break;
            }
        }

        if (is_prime) {
            count++;
            cout << number << "\t";

            if (count % primes_per_line == 0) {
                cout << "\n";
            }
        }
        number++;
    }
    return 0;
}
```

---

## loop flow control: break vs continue

- **`break`**: terminates the surrounding loop immediately and jumps out of the loop block.
- **`continue`**: skips the remainder of the current iteration and jumps directly to the increment/update step.

```cpp
#include <iostream>
using namespace std;

int main() {
    // break example
    for (int i = 1; i <= 5; i++) {
        if (i == 3) break; // stops when i == 3 (prints 1, 2)
        cout << i << " ";
    }
    cout << "\n";

    // continue example
    for (int i = 1; i <= 5; i++) {
        if (i == 3) continue; // skips 3, continues with 4, 5 (prints 1, 2, 4, 5)
        cout << i << " ";
    }
    cout << "\n";
    return 0;
}
```
