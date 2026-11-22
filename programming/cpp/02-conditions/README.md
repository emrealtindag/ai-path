# conditions

comparisons, true/false logic, truth tables, if / else if / else, switch, random numbers, characters, and the ternary operator. all code uses `using namespace std;`.

---

## comparison operators and boolalpha

- `=` assigns a value. `==` checks if two values are equal.
- `!=` not equal, `>`, `<`, `>=`, `<=`.
- a comparison gives `true` or `false`. by default `cout` prints them as `1` and `0`.
- `cout << boolalpha;` makes it print the words `true` and `false` instead.

```cpp
#include <iostream>
using namespace std;

int main() {
    int x = 2;
    int y = 2;

    cout << boolalpha;
    cout << (x == y) << endl;     // true
    cout << (x != y) << endl;     // false
    cout << (x > y) << endl;      // false
    cout << (x < y) << endl;      // false
    cout << (x >= y) << endl;     // true
    cout << (x <= y) << endl;     // true
    cout << (x % 2 == 0) << endl; // true
    return 0;
}
```

### problem 1: even or odd

```cpp
#include <iostream>
using namespace std;

int main() {
    int number;
    cout << "Enter a number = ";
    cin >> number;

    cout << "The remainder when you divide " << number << " by two is " << number % 2 << endl;
    cout << (number % 2 == 0) << endl; // 1 if even, 0 if odd

    if (number % 2 == 0)
        cout << number << " is an even number" << endl;
    else
        cout << number << " is an odd number" << endl;
    return 0;
}
```

---

## logic operators and truth tables

- `&&` (and): true only if both sides are true.
- `||` (or): true if at least one side is true.
- `^` (xor, exclusive or): true if exactly one side is true. if both are true, it's false.
- `!` (not): flips true to false and false to true.

| p | q | `p && q` | `p \|\| q` | `p ^ q` |
| :---: | :---: | :---: | :---: | :---: |
| T | T | T | T | F |
| T | F | F | T | T |
| F | T | F | T | T |
| F | F | F | F | F |

examples from class:

- `(3 == 3) && (4 != 3)` is true, both sides are true.
- `(3 == 3) || (3 == 4)` is true, the left side is enough.

### problem 2: divisible by 4 and / or 5

```cpp
#include <iostream>
using namespace std;

int main() {
    int number;
    cout << "enter a positive number" << endl;
    cin >> number;
    cout << boolalpha;

    cout << "is my number divisible by 4 and 5" << endl;
    cout << ((number % 4 == 0) && (number % 5 == 0)) << endl;

    cout << "is my number divisible by 4 or 5" << endl;
    cout << ((number % 4 == 0) || (number % 5 == 0)) << endl;

    cout << "is my number divisible by 4 or 5, but not both" << endl;
    cout << ((number % 4 == 0) ^ (number % 5 == 0)) << endl;
    return 0;
}
```

for 20: and is true, or is true, xor is false (it divides by both).

---

## if, else if, else

```cpp
if (condition) {
    // runs if condition is true
} else if (other_condition) {
    // runs if the first one was false and this one is true
} else {
    // runs if nothing above was true
}
```

### problem 3: circle area with a negative radius check

```cpp
#include <iostream>
#include <cmath>
using namespace std;

int main() {
    double radius;
    cout << "enter a positive radius number" << endl;
    cin >> radius;

    if (radius < 0) {
        cout << "we can't calculate the area with a negative number" << endl;
    } else {
        cout << "the area of the circle is " << 3.1415 * pow(radius, 2) << endl;
    }
    return 0;
}
```

### problem 4: rectangle or triangle area

```cpp
#include <iostream>
using namespace std;

int main() {
    int choice;
    double side1, side2;
    double height, base;

    cout << "Press one(1) for computing the area of a rectangle" << endl;
    cout << "Press two(2) for computing the area of a triangle" << endl;
    cout << "Dont press other buttons !!! " << endl;
    cin >> choice;

    if (choice == 1) {
        cout << "Welcome to the world of a rectangle " << endl;
        cout << "Enter the corresponding lengths = " << endl;
        cin >> side1 >> side2;
        cout << "The area is " << side1 * side2 << endl;
    } else if (choice == 2) {
        cout << "Welcome to the world of a triangle " << endl;
        cout << "Enter the height = " << endl;
        cin >> height;
        cout << "Enter the base = " << endl;
        cin >> base;
        cout << "The area is " << (height * base) / 2.0 << endl;
    } else {
        cout << "I said that dont pick other numbers, the program will end!!";
    }
    return 0;
}
```

### problem 5: formula that depends on x

$$y = \frac{x}{x^2 + 2} \quad \text{if } x < 5$$

$$y = \frac{x}{1 + \sqrt{x + 1}} \quad \text{if } x \ge 5$$

```cpp
#include <iostream>
#include <cmath>
using namespace std;

int main() {
    double x, y;
    cout << "enter a number for conditional formula = ";
    cin >> x;

    if (x < 5)
        y = x / (pow(x, 2) + 2);
    else
        y = x / (1 + sqrt(x + 1));

    cout << "y = " << y << endl;
    return 0;
}
```

### problem 6: 3-digit palindrome

a 3-digit number is a palindrome if the first and last digits are the same (171, 454).

- `number / 100` gives the first digit: 171 / 100 = 1
- `(number / 10) % 10` gives the middle digit: 17 % 10 = 7
- `number % 10` gives the last digit: 171 % 10 = 1

```cpp
#include <iostream>
#include <cmath>
using namespace std;

int main() {
    int number;
    cout << "Enter a three digit integer number from the keyboard = " << endl;
    cin >> number;
    number = abs(number); // absolute value, so -171 also works

    if ((number < 100) || (number > 999)) {
        cout << "The number is not a three-digit number !!!!" << endl;
    } else {
        int first_digit = number / 100;
        int last_digit = number % 10;

        if (first_digit == last_digit)
            cout << number << " is a palindrome number" << endl;
        else
            cout << number << " is not a palindrome number" << endl;
    }
    return 0;
}
```

### problem 7: quadratic equation

for $ax^2 + bx + c = 0$ the discriminant is $\Delta = b^2 - 4ac$:

- $\Delta > 0$: two different real roots
- $\Delta = 0$: two equal roots
- $\Delta < 0$: no real roots (two complex roots)

```cpp
#include <iostream>
#include <cmath>
using namespace std;

int main() {
    double a, b, c;
    cout << "Enter coefficients a, b and c: ";
    cin >> a >> b >> c;

    if (a == 0) {
        if (b != 0)
            cout << "Linear equation. Single root: x = " << -c / b << endl;
        else
            cout << "Invalid equation." << endl;
        return 0;
    }

    double delta = pow(b, 2) - 4 * a * c;

    if (delta > 0) {
        double x1 = (-b + sqrt(delta)) / (2 * a);
        double x2 = (-b - sqrt(delta)) / (2 * a);
        cout << "Two distinct real roots: x1 = " << x1 << " x2 = " << x2 << endl;
    } else if (delta == 0) {
        double x = -b / (2 * a);
        cout << "Two equal real roots: x1 = x2 = " << x << endl;
    } else {
        double realPart = -b / (2 * a);
        double imagPart = sqrt(-delta) / (2 * a);
        cout << "No real roots. Two complex roots:" << endl;
        cout << "x1 = " << realPart << " + " << imagPart << "i" << endl;
        cout << "x2 = " << realPart << " - " << imagPart << "i" << endl;
    }
    return 0;
}
```

### problem 8: letter grade

```cpp
#include <iostream>
using namespace std;

int main() {
    double grade;
    cout << "enter your grade" << endl;
    cin >> grade;

    if (grade > 100 || grade < 0)
        cout << "invalid grade" << endl;
    else if (grade >= 90)
        cout << "A+" << endl;
    else if (grade >= 80)
        cout << "A" << endl;
    else if (grade >= 70)
        cout << "B+" << endl;
    else if (grade >= 60)
        cout << "B" << endl;
    else if (grade >= 50)
        cout << "C+" << endl;
    else if (grade >= 40)
        cout << "C" << endl;
    else
        cout << "F" << endl;
    return 0;
}
```

### problem 9: bmi

bmi = weight / height², weight in kg and height in meters.

```cpp
#include <iostream>
#include <cmath>
using namespace std;

int main() {
    double weight, height, BMI;
    cout << "enter your weight and height" << endl;
    cin >> weight >> height;
    cout << "your weight " << weight << " your height " << height << endl;

    BMI = weight / pow(height, 2);

    if (BMI < 18.5)
        cout << "your BMI underweight" << endl;
    else if (BMI >= 18.5 && BMI < 25.0)
        cout << "your BMI normal" << endl;
    else if (BMI < 30.0)
        cout << "your BMI overweight" << endl;
    else
        cout << "your BMI obese" << endl;
    return 0;
}
```

### problem 10: smallest of three numbers

in class this was written with three separate `if`s. the note from class: with `else if`, once one condition is true the rest are not checked anymore.

here that is actually fine, because only one number can be the smallest. so `else if` works and does fewer checks. using `<=` instead of `<` also handles equal numbers. with `<` and an input like 3 3 5, none of the conditions are true and nothing gets printed.

```cpp
#include <iostream>
using namespace std;

int main() {
    int number_1, number_2, number_3;
    cout << "enter 3 numbers" << endl;
    cin >> number_1 >> number_2 >> number_3;

    if (number_1 <= number_2 && number_1 <= number_3)
        cout << "smallest one is " << number_1 << endl;
    else if (number_2 <= number_1 && number_2 <= number_3)
        cout << "smallest one is " << number_2 << endl;
    else
        cout << "smallest one is " << number_3 << endl;
    return 0;
}
```

separate `if`s are needed when more than one block is allowed to run, for example printing every number that is bigger than 10.

### problem 11: leap year

a year is a leap year if it divides by 4 and not by 100, or if it divides by 400.

```cpp
#include <iostream>
using namespace std;

int main() {
    int year;
    cout << "enter a year and I will tell you whether it is leap year or not" << endl;
    cin >> year;

    bool isLeapYear = ((year % 4 == 0) && (year % 100 != 0)) || (year % 400 == 0);
    cout << boolalpha << isLeapYear << endl;

    if (isLeapYear)
        cout << year << " is a leap year" << endl;
    else
        cout << year << " is not a leap year" << endl;
    return 0;
}
```

---

## random numbers

- `rand()` gives a random number. needs `#include <cstdlib>` (c standard library).
- `rand() % 2` gives 0 or 1, `rand() % 100` gives 0 to 99, `rand() % 101` gives 0 to 100.
- without `srand`, `rand()` gives the same numbers every time you run the program.
- `srand(time(0))` sets a different starting point on every run, based on the current time. needs `#include <ctime>`. call it once at the start of `main`.

### problem 12: guess 0 or 1

```cpp
#include <iostream>
#include <cstdlib>
#include <ctime>
using namespace std;

int main() {
    srand(time(0));
    int randomNumber = rand() % 2;
    int answer;

    cout << "Guess the generated number, just enter 0 or 1 = ";
    cin >> answer;

    if (randomNumber == answer)
        cout << "You have won!!";
    else
        cout << "You have lost!!";
    return 0;
}
```

### problem 13: 2-digit lottery

- `lottery / 10` gives the first digit: 89 / 10 = 8
- `lottery % 10` gives the second digit: 89 % 10 = 9

```cpp
#include <iostream>
#include <cstdlib>
#include <ctime>
using namespace std;

int main() {
    srand(time(0));
    int lottery = rand() % 100;
    int lotteryDigit1 = lottery / 10;
    int lotteryDigit2 = lottery % 10;

    int guess;
    cout << "enter just two digit number from the keyboard = ";
    cin >> guess;
    int guessDigit1 = guess / 10;
    int guessDigit2 = guess % 10;

    if (lottery == guess)
        cout << "you won 10000 dollars" << endl;
    else if ((lotteryDigit1 == guessDigit2) && (lotteryDigit2 == guessDigit1))
        cout << "you won 3000 dollars" << endl;
    else if ((lotteryDigit1 == guessDigit1) || (lotteryDigit1 == guessDigit2) ||
             (lotteryDigit2 == guessDigit1) || (lotteryDigit2 == guessDigit2))
        cout << "you won 1000 dollars" << endl;
    else
        cout << "you won nothing :(" << endl;
    return 0;
}
```

---

## switch

`switch` checks one value and jumps to the matching `case`. use it instead of a long chain of `if`s when you compare the same variable against many fixed values.

- `break` ends the switch. without it, the code keeps running into the next case (fall-through).
- `default` runs if no case matches.

### problem 14: chinese zodiac

```cpp
#include <iostream>
using namespace std;

int main() {
    int year;
    cout << "enter your birth year = ";
    cin >> year;
    int remainder = year % 12;

    switch (remainder) {
        case 0: cout << "monkey" << endl; break;
        case 1: cout << "rooster" << endl; break;
        case 2: cout << "dog" << endl; break;
        case 3: cout << "pig" << endl; break;
        case 4: cout << "rat" << endl; break;
        case 5: cout << "ox" << endl; break;
        case 6: cout << "tiger" << endl; break;
        case 7: cout << "rabbit" << endl; break;
        case 8: cout << "dragon" << endl; break;
        case 9: cout << "snake" << endl; break;
        case 10: cout << "horse" << endl; break;
        case 11: cout << "sheep" << endl; break;
    }
    return 0;
}
```

the same program can be written with 12 `else if (year % 12 == ...)` lines, switch is just shorter.

### problem 15: day of the week

```cpp
#include <iostream>
using namespace std;

int main() {
    int dayIndex; // 1 to 7
    cin >> dayIndex;

    switch (dayIndex) {
        case 1: cout << "monday" << endl; break;
        case 2: cout << "tuesday" << endl; break;
        case 3: cout << "wednesday" << endl; break;
        case 4: cout << "thursday" << endl; break;
        case 5: cout << "friday" << endl; break;
        case 6: cout << "saturday" << endl; break;
        case 7: cout << "sunday" << endl; break;
        default: cout << "invalid day index" << endl; break;
    }
    return 0;
}
```

### problem 16: weekday or weekend (cases without break)

cases with no code and no `break` fall into the next one, so cases 1 to 5 all end up at "weekdays". it works like an or.

```cpp
#include <iostream>
using namespace std;

int main() {
    int dayIndex;
    cin >> dayIndex;

    switch (dayIndex) {
        case 1:
        case 2:
        case 3:
        case 4:
        case 5:
            cout << "weekdays" << endl;
            break;
        case 6:
        case 7:
            cout << "weekend" << endl;
            break;
        default:
            cout << "invalid day index" << endl;
            break;
    }
    return 0;
}
```

### problem 17: calculator

```cpp
#include <iostream>
using namespace std;

int main() {
    double number1, number2;
    char x;

    cout << "enter numbers 1 and 2" << endl;
    cin >> number1 >> number2;
    cout << "enter a calculation operation +, -, /, *" << endl;
    cin >> x;

    switch (x) {
        case '+': cout << number1 << " + " << number2 << " = " << number1 + number2 << endl; break;
        case '-': cout << number1 << " - " << number2 << " = " << number1 - number2 << endl; break;
        case '*': cout << number1 << " * " << number2 << " = " << number1 * number2 << endl; break;
        case '/':
            if (number2 != 0)
                cout << number1 << " / " << number2 << " = " << number1 / number2 << endl;
            else
                cout << "can't divide by zero" << endl;
            break;
        default: cout << "invalid operation" << endl; break;
    }
    return 0;
}
```

### problem 18: number of days in a month

```cpp
#include <iostream>
using namespace std;

int main() {
    int monthIndex;
    int year;
    int numberOfDays = 0;

    cout << "Enter the month index and the year you want to evaluate: ";
    cin >> monthIndex >> year;

    switch (monthIndex) {
        case 1:
        case 3:
        case 5:
        case 7:
        case 8:
        case 10:
        case 12:
            numberOfDays = 31;
            break;
        case 4:
        case 6:
        case 9:
        case 11:
            numberOfDays = 30;
            break;
        case 2:
            if (((year % 4 == 0) && (year % 100 != 0)) || (year % 400 == 0))
                numberOfDays = 29;
            else
                numberOfDays = 28;
            break;
        default:
            cout << "Invalid month index" << endl;
            break;
    }

    if ((monthIndex >= 1) && (monthIndex <= 12))
        cout << "The number of the day that belongs to the certain month and year is " << numberOfDays << endl;
    else
        cout << "I can't calculate month and year" << endl;
    return 0;
}
```

### problem 19: rock, paper, scissors

`rand() % 3` gives 0, 1 or 2.

```cpp
#include <iostream>
#include <cstdlib>
#include <ctime>
using namespace std;

int main() {
    srand(time(0));
    int computerChoice = rand() % 3;
    int userChoice;

    cout << "enter your choice between 0 (scissor), 1 (rock), 2 (paper)" << endl;
    cin >> userChoice;

    cout << "the computer is ";
    switch (computerChoice) {
        case 0: cout << "scissor" << endl; break;
        case 1: cout << "rock" << endl; break;
        case 2: cout << "paper" << endl; break;
    }

    cout << "the user is ";
    switch (userChoice) {
        case 0: cout << "scissor" << endl; break;
        case 1: cout << "rock" << endl; break;
        case 2: cout << "paper" << endl; break;
    }

    if (computerChoice == userChoice) {
        cout << "no winner..." << endl;
    } else {
        bool win = (userChoice == 0 && computerChoice == 2) ||
                   (userChoice == 1 && computerChoice == 0) ||
                   (userChoice == 2 && computerChoice == 1);
        if (win)
            cout << "you won" << endl;
        else
            cout << "you lost" << endl;
    }
    return 0;
}
```

---

## characters and ascii codes

every `char` is stored as a number (its ascii code). casting with `(int)` shows that number.

```cpp
#include <iostream>
using namespace std;

int main() {
    char ch = 'a';
    cout << ch << endl;       // a
    cout << (int)ch << endl;  // 97

    char ch2 = 'b';
    cout << (int)ch2 << endl; // 98

    char ch3 = 98;
    cout << ch3 << endl;      // b, a number can be stored as a char

    char ch4 = '?';
    cout << (int)ch4 << endl; // 63

    char ch5 = 'A';
    cout << int(ch5) << endl; // 65

    char ch6 = '\u0041';      // unicode
    cout << ch6 << endl;      // A

    int value = '2' + '3';    // adds the codes, not the digits
    cout << value << endl;    // 101, because '2' is 50 and '3' is 51

    char ch7 = '2';
    cout << ch7 << endl;      // 2
    cout << (int)ch7 << endl; // 50
    return 0;
}
```

### problem 20: what kind of character is it

```cpp
#include <iostream>
using namespace std;

int main() {
    char ch = 'B';

    if (ch >= 'A' && ch <= 'Z')
        cout << "it is a capital letter" << endl;
    else if (ch >= 'a' && ch <= 'z')
        cout << ch << " is a lowercase letter" << endl;
    else if (ch >= '0' && ch <= '9')
        cout << ch << " is a digit" << endl;
    return 0;
}
```

this works because letters have codes in order: 'A' to 'Z' are 65 to 90, 'a' to 'z' are 97 to 122.

---

## cctype functions

`#include <cctype>` gives ready functions for characters:

- `islower(ch)`, `isupper(ch)`: check lowercase / uppercase.
- `tolower(ch)`, `toupper(ch)`: convert the letter. they return the ascii code, so use `(char)` to print the letter.

in c++ every number except 0 counts as true. `islower` returns 0 for false and some non-zero number for true, so it can go straight into an `if`.

```cpp
#include <iostream>
#include <cctype>
using namespace std;

int main() {
    char ch = 'b';
    cout << islower(ch) << endl; // non-zero (true)

    if (islower(ch))
        cout << ch << " lowercase letter" << endl;
    else
        cout << ch << " upper case letter" << endl;

    char ch1 = 'c';
    cout << isupper(ch1) << endl;        // 0, because c is lowercase

    char ch2 = 'C';
    cout << tolower(ch2) << endl;        // 99, the code of 'c'
    cout << (char)tolower(ch2) << endl;  // c

    char ch3 = 'd';
    cout << toupper(ch3) << endl;        // 68, the code of 'D'
    cout << (char)toupper(ch3) << endl;  // D
    return 0;
}
```

---

## ternary operator ( ? : )

a short way to write a simple if / else that picks between two values:

```text
condition ? value_if_true : value_if_false
```

```cpp
#include <iostream>
using namespace std;

int main() {
    int x = 10;
    int result;

    // long version
    if (x > 10)
        result = x + 20;
    else
        result = x - 20;

    // same thing with the ternary operator
    result = (x > 10) ? x + 20 : x - 20;
    cout << "result: " << result << endl; // -10, because 10 > 10 is false

    int number1 = 10;
    int number2 = 30;
    int max_value = (number1 > number2) ? number1 : number2;
    cout << "max: " << max_value << endl; // 30
    return 0;
}
```
