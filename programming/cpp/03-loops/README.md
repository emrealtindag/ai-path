# loops

detailed study notes, algorithm patterns, and classroom problem solutions covering while, do-while, and for iteration constructs in c++.

---

## while loops and condition-based iteration

a while loop repeats a block of code as long as its condition evaluates to true. if the condition is false initially, the loop does not run.

### problem 1: even numbers up to 30

prints only even numbers starting from 0 up to 30:

```cpp
int i = 0;
while (i <= 30) {
    std::cout << i << " ";
    i += 2;
}
```

### problem 2: counting steps and calculating the mean (average)

sums numbers from 1 to 10, counts the iterations, and calculates the floating-point mean:

```cpp
int counter = 0;
int x = 1;
int sum = 0;

while (x <= 10) {
    sum += x;
    x++;
    counter++;
}

double mean = static_cast<double>(sum) / counter;
std::cout << "sum: " << sum << ", count: " << counter << ", mean: " << mean << "\n";
// sum: 55, count: 10, mean: 5.5
```

### problem 3: factorial with positive input validation

validates that user input is non-negative before computing factorial:

```cpp
int number;
std::cout << "enter a number: ";
std::cin >> number;

// input validation
while (number < 0) {
    std::cout << "enter a positive number: ";
    std::cin >> number;
}

int factorial = 1;
int start = 1;
while (start <= number) {
    factorial *= start;
    start++;
}
std::cout << number << "! = " << factorial << "\n";
```

### problem 4: greatest common divisor (gcd / ebob)

finds the largest positive integer that divides two input numbers without remainder:

```cpp
int num1, num2;
std::cin >> num1 >> num2;

int gcd = 1;
int f = 2;

while (f <= num1 && f <= num2) {
    if (num1 % f == 0 && num2 % f == 0) {
        gcd = f;
    }
    f++;
}
std::cout << "greatest common divisor: " << gcd << "\n";
```

### problem 5: subtraction quiz with random numbers

generates two random numbers below 10 and prompts the user repeatedly until the correct answer is given:

```cpp
#include <cstdlib>
#include <ctime>

srand(time(0));
int n1 = rand() % 10;
int n2 = rand() % 10;

int answer;
std::cout << "what is " << n1 << " + " << n2 << "? ";
std::cin >> answer;

while (n1 + n2 != answer) {
    std::cout << "wrong answer! try again: ";
    std::cin >> answer;
}
std::cout << "correct!\n";
```

### problem 6: guess the magic number (0 to 100)

generates a random target and provides high/low feedback until guessed:

```cpp
int magic_number = rand() % 101; // 0 to 100
int guess = -1;

while (guess != magic_number) {
    std::cout << "enter a number between 0 and 100: ";
    std::cin >> guess;

    if (guess == magic_number) {
        std::cout << "yes you got it! magic number was " << magic_number << "\n";
    } else if (guess < magic_number) {
        std::cout << "your guess is too low\n";
    } else {
        std::cout << "your guess is too high\n";
    }
}
```

---

## do-while loops

do-while evaluates the condition at the end of the loop body, guaranteeing at least one execution pass. commonly used for interactive menus and user confirmations.

### problem 7: atm banking menu

presents an interactive account menu that redisplays until the user enters 0:

```cpp
int choice;
int balance = 500;

do {
    std::cout << "\n--- atm menu ---\n";
    std::cout << "1. check balance\n";
    std::cout << "2. deposit money\n";
    std::cout << "0. exit\n";
    std::cout << "your choice: ";
    std::cin >> choice;

    if (choice == 1) {
        std::cout << "current balance: " << balance << " tl\n";
    } else if (choice == 2) {
        int deposit;
        std::cout << "enter deposit amount: ";
        std::cin >> deposit;
        balance += deposit;
        std::cout << "updated balance: " << balance << " tl\n";
    } else if (choice != 0) {
        std::cout << "invalid selection, please retry.\n";
    }
} while (choice != 0);

std::cout << "session closed.\n";
```

### problem 8: even and odd numbers accumulator with continue prompt

reads numbers, accumulates evens and odds separately, and asks the user if they want to continue:

```cpp
int num;
char choice;
int sum_even = 0;
int sum_odd = 0;

do {
    std::cout << "enter a number: ";
    std::cin >> num;

    if (num % 2 == 0) {
        sum_even += num;
    } else {
        sum_odd += num;
    }

    std::cout << "do you want to continue (y/n)? ";
    std::cin >> choice;
} while (choice == 'y' || choice == 'Y');

std::cout << "sum of evens: " << sum_even << "\n";
std::cout << "sum of odds: " << sum_odd << "\n";
```

---

## for loops and iteration state tracing

for loops package initialization, condition, and increment into a single header.

### loop execution sequence:

```cpp
for (initialization; condition; increment) {
    // body
}
```

execution follows:
1. `initialization` runs once at the beginning.
2. `condition` is evaluated. if false, loop exits.
3. `body` executes.
4. `increment` updates the variable.
5. repeats from step 2.

for `for (int i = 1; i <= 3; i++) cout << "hello " << i;`:
- pass 1: i = 1, condition true -> prints "hello 1", i becomes 2
- pass 2: i = 2, condition true -> prints "hello 2", i becomes 3
- pass 3: i = 3, condition true -> prints "hello 3", i becomes 4
- exit check: i = 4, condition false -> loop terminates.
- after loop exit, i has value 4.

### problem 9: multiplication tables

single number table:
```cpp
int number = 5;
for (int i = 1; i <= 10; i++) {
    std::cout << i << " * " << number << " = " << (i * number) << "\n";
}
```

nested loop generating full 1 to 10 multiplication table:
```cpp
for (int i = 1; i <= 10; i++) {
    for (int j = 1; j <= 10; j++) {
        std::cout << (i * j) << "\t";
    }
    std::cout << "\n";
}
```

### problem 10: integer power computation without pow()

computes $base^{power}$ using only loops and multiplications:

```cpp
int base, power;
do {
    std::cout << "enter positive base: ";
    std::cin >> base;
} while (base < 0);

do {
    std::cout << "enter positive power: ";
    std::cin >> power;
} while (power < 0);

int product = 1;
for (int i = 1; i <= power; i++) {
    product *= base;
}
std::cout << base << " raised to " << power << " is " << product << "\n";
```

### problem 11: harmonic and alternating series summation

harmonic series: $1 + 1/2 + 1/3 + \dots + 1/n$

```cpp
int n = 10;
double sum = 0.0;
for (int i = 1; i <= n; i++) {
    sum += (1.0 / i);
}
std::cout << "harmonic sum: " << sum << "\n";
```

alternating series: $1 - 1/2 + 1/3 - 1/4 + \dots$ using a sign flipper `p`:

```cpp
int n = 6;
double sum = 0.0;
int p = 1;

for (int i = 1; i <= n; i++) {
    sum += (1.0 / i) * p;
    p = -p; // flips between +1 and -1
}
std::cout << "alternating sum: " << sum << "\n";
```

### problem 12: prime number checker

checks whether a positive integer is prime using a boolean flag and early break:

```cpp
int number;
do {
    std::cout << "enter positive number: ";
    std::cin >> number;
} while (number < 0);

bool is_prime = true;

if (number <= 1) {
    is_prime = false;
} else {
    for (int i = 2; i < number; i++) {
        if (number % i == 0) {
            is_prime = false;
            break; // divisor found, no need to check further
        }
    }
}

if (is_prime) {
    std::cout << number << " is a prime number\n";
} else {
    std::cout << number << " is not a prime number\n";
}
```

### problem 13: generating the first 50 prime numbers

prints the first 50 prime numbers, formatted 10 numbers per row using nested loops and modular printing:

```cpp
const int number_of_primes = 50;
const int primes_per_line = 10;

int count = 0;
int number = 2;

std::cout << "the first 50 prime numbers are:\n";

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
        std::cout << number << "\t";

        if (count % primes_per_line == 0) {
            std::cout << "\n";
        }
    }
    number++;
}
```

---

## loop flow control: break vs continue

- **`break`**: terminates the loop immediately and jumps out of the block.
- **`continue`**: stops the current pass and jumps directly to the next iteration.

```cpp
for (int i = 1; i <= 5; i++) {
    if (i == 3) break; // stops when i == 3 (prints 1, 2)
    std::cout << i << " ";
}

for (int i = 1; i <= 5; i++) {
    if (i == 3) continue; // skips 3, continues with 4, 5 (prints 1, 2, 4, 5)
    std::cout << i << " ";
}
```
