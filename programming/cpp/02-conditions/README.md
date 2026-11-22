# conditions

decision structures, boolean logic, relational comparisons, truth tables, if-else chains, switch jump tables, and classroom algorithmic problems in c++ (all examples assume using namespace std;).

---

## relational operators, equality, and boolalpha

relational expressions compare operands and evaluate to boolean values (`true` or `false`).
- `==`: equality comparison (evaluates whether left and right values are equal).
- `=`: assignment operator (stores right-hand value into the left-hand variable).
- `!=`: not equal.
- `>`, `<`, `>=`, `<=`: inequality comparisons.

by default, c++ output streams print `1` for true and `0` for false. the `boolalpha` manipulator forces the stream to print literal `"true"` or `"false"`.

```cpp
#include <iostream>
using namespace std;

int main() {
    int x = 2, y = 2;
    cout << boolalpha;
    cout << (x == y) << "\n"; // true
    cout << (x != y) << "\n"; // false
    cout << (x > y)  << "\n"; // false
    cout << (x <= y) << "\n"; // true
    cout << (x % 2 == 0) << "\n"; // true
    return 0;
}
```

---

## boolean logic operators and truth tables

compound logical expressions combine boolean conditions using three primary operators:

1. **logical and (`&&`)**: evaluates to `true` only if **both** operands are true.
2. **logical or (`||`)**: evaluates to `true` if **at least one** operand is true.
3. **bitwise / logical xor (`^`)**: evaluates to `true` if **exactly one** operand is true (exclusive or; false if both are true or both are false).

### truth tables

| p | q | p && q (and) | p \|\| q (or) | p ^ q (xor) |
| :---: | :---: | :---: | :---: | :---: |
| true | true | true | true | false |
| true | false | false | true | true |
| false | true | false | true | true |
| false | false | false | false | false |

### problem 1: divisibility tests using and, or, and xor

evaluating whether a number is divisible by 4 and/or 5:

```cpp
#include <iostream>
using namespace std;

int main() {
    int number;
    cout << "enter a positive number: ";
    cin >> number;

    cout << boolalpha;
    cout << "divisible by 4 and 5: " << ((number % 4 == 0) && (number % 5 == 0)) << "\n";
    cout << "divisible by 4 or 5: "  << ((number % 4 == 0) || (number % 5 == 0)) << "\n";
    // xor rule: divisible by either 4 or 5, but NOT both simultaneously!
    cout << "divisible by 4 xor 5: " << ((number % 4 == 0) ^ (number % 5 == 0)) << "\n";
    return 0;
}
```

---

## if, else if, else chains and input validation

### problem 2: circle area calculation with negative radius guard

```cpp
#include <iostream>
#include <cmath>
using namespace std;

int main() {
    double radius;
    cout << "enter a positive radius: ";
    cin >> radius;

    if (radius < 0) {
        cout << "we cannot calculate the area with a negative number.\n";
    } else {
        double area = 3.1415 * pow(radius, 2);
        cout << "the area of the circle is: " << area << "\n";
    }
    return 0;
}
```

### problem 3: shape area selector (rectangle vs triangle)

```cpp
#include <iostream>
using namespace std;

int main() {
    int choice;
    cout << "select shape (1: rectangle, 2: triangle): ";
    cin >> choice;

    if (choice == 1) {
        double side1, side2;
        cout << "enter two sides: ";
        cin >> side1 >> side2;
        cout << "rectangle area: " << (side1 * side2) << "\n";
    } else if (choice == 2) {
        double base, height;
        cout << "enter base and height: ";
        cin >> base >> height;
        cout << "triangle area: " << (base * height) / 2.0 << "\n";
    } else {
        cout << "invalid selection: program terminates.\n";
    }
    return 0;
}
```

### problem 4: 3-digit palindrome number checker

checks whether a 3-digit integer reads identically forwards and backwards (e.g. 171, 454):

```cpp
#include <iostream>
#include <cmath>
using namespace std;

int main() {
    int number;
    cout << "enter a three-digit integer: ";
    cin >> number;

    number = abs(number);

    if (number < 100 || number > 999) {
        cout << "error: number is not 3 digits.\n";
    } else {
        int first_digit = number / 100;
        int last_digit = number % 10;

        if (first_digit == last_digit) {
            cout << number << " is a palindrome number\n";
        } else {
            cout << number << " is not a palindrome number\n";
        }
    }
    return 0;
}
```

### problem 5: finding smallest of three numbers (independent if vs else if)

when evaluating multiple non-exclusive or distinct conditions, chained `else if` stops after the first true match. separate `if` blocks allow evaluating all relevant criteria:

```cpp
#include <iostream>
using namespace std;

int main() {
    int n1, n2, n3;
    cout << "enter three distinct integers: ";
    cin >> n1 >> n2 >> n3;

    if (n1 < n2 && n1 < n3) {
        cout << "smallest is: " << n1 << "\n";
    }
    if (n2 < n1 && n2 < n3) {
        cout << "smallest is: " << n2 << "\n";
    }
    if (n3 < n1 && n3 < n2) {
        cout << "smallest is: " << n3 << "\n";
    }
    return 0;
}
```

### problem 6: quadratic equation solver (discriminant delta)

solves $a x^2 + b x + c = 0$ using discriminant $\Delta = b^2 - 4ac$:

```cpp
#include <iostream>
#include <cmath>
using namespace std;

int main() {
    double a, b, c;
    cout << "enter coefficients a, b, c: ";
    cin >> a >> b >> c;

    if (a == 0.0) {
        if (b != 0.0) {
            cout << "linear equation root: x = " << (-c / b) << "\n";
        } else {
            cout << "invalid equation (no variables).\n";
        }
    } else {
        double delta = pow(b, 2) - 4 * a * c;

        if (delta > 0.0) {
            double x1 = (-b + sqrt(delta)) / (2 * a);
            double x2 = (-b - sqrt(delta)) / (2 * a);
            cout << "two distinct real roots: x1 = " << x1 << ", x2 = " << x2 << "\n";
        } else if (delta == 0.0) {
            double x = -b / (2 * a);
            cout << "one repeated real root: x1 = x2 = " << x << "\n";
        } else {
            double real_part = -b / (2 * a);
            double imag_part = sqrt(-delta) / (2 * a);
            cout << "two complex roots: " << real_part << " +- " << imag_part << "i\n";
        }
    }
    return 0;
}
```

### problem 7: letter grade scale

```cpp
#include <iostream>
using namespace std;

int main() {
    double grade;
    cout << "enter your grade: ";
    cin >> grade;

    if (grade > 100.0 || grade < 0.0) {
        cout << "invalid grade entered.\n";
    } else if (grade >= 90.0) {
        cout << "A+\n";
    } else if (grade >= 80.0) {
        cout << "A\n";
    } else if (grade >= 70.0) {
        cout << "B+\n";
    } else if (grade >= 60.0) {
        cout << "B\n";
    } else if (grade >= 50.0) {
        cout << "C+\n";
    } else if (grade >= 40.0) {
        cout << "C\n";
    } else {
        cout << "F (fail)\n";
    }
    return 0;
}
```

### problem 8: bmi (body mass index) calculation

formula: $\text{BMI} = \text{weight} / \text{height}^2$ (weight in kg, height in meters):

```cpp
#include <iostream>
#include <cmath>
using namespace std;

int main() {
    double weight, height;
    cout << "enter weight (kg) and height (m): ";
    cin >> weight >> height;

    double bmi = weight / pow(height, 2);

    if (bmi < 18.5) {
        cout << "your bmi is underweight\n";
    } else if (bmi < 25.0) {
        cout << "your bmi is normal\n";
    } else if (bmi < 30.0) {
        cout << "your bmi is overweight\n";
    } else {
        cout << "your bmi is obese\n";
    }
    return 0;
}
```

### problem 9: leap year determination

a year is a leap year if:
- divisible by 4 AND not divisible by 100, OR
- divisible by 400.

```cpp
#include <iostream>
using namespace std;

int main() {
    int year;
    cout << "enter year: ";
    cin >> year;

    bool is_leap = ((year % 4 == 0) && (year % 100 != 0)) || (year % 400 == 0);

    if (is_leap) {
        cout << year << " is a leap year\n";
    } else {
        cout << year << " is not a leap year\n";
    }
    return 0;
}
```

---

## random numbers and game algorithms

### problem 10: 2-digit lottery game

generates a pseudo-random 2-digit target (`rand() % 100`) seeded with system time:

```cpp
#include <iostream>
#include <cstdlib>
#include <ctime>
using namespace std;

int main() {
    srand(time(0));
    int lottery = rand() % 100;
    int lot_d1 = lottery / 10;
    int lot_d2 = lottery % 10;

    int guess;
    cout << "enter two-digit guess: ";
    cin >> guess;

    int g_d1 = guess / 10;
    int g_d2 = guess % 10;

    if (lottery == guess) {
        cout << "exact match: you won $10,000!\n";
    } else if (g_d1 == lot_d2 && g_d2 == lot_d1) {
        cout << "all digits match: you won $3,000!\n";
    } else if (g_d1 == lot_d1 || g_d1 == lot_d2 || g_d2 == lot_d1 || g_d2 == lot_d2) {
        cout << "one digit matches: you won $1,000!\n";
    } else {
        cout << "no match: you won nothing.\n";
    }
    return 0;
}
```

---

## switch statements and multi-way branching

`switch` inspects an integral or character expression and jumps directly to matching `case` labels. omitting `break` produces **fall-through**, where execution continues into subsequent cases.

### problem 11: chinese zodiac (year % 12)

```cpp
#include <iostream>
using namespace std;

int main() {
    int year;
    cout << "enter birth year: ";
    cin >> year;

    switch (year % 12) {
        case 0: cout << "monkey\n"; break;
        case 1: cout << "rooster\n"; break;
        case 2: cout << "dog\n"; break;
        case 3: cout << "pig\n"; break;
        case 4: cout << "rat\n"; break;
        case 5: cout << "ox\n"; break;
        case 6: cout << "tiger\n"; break;
        case 7: cout << "rabbit\n"; break;
        case 8: cout << "dragon\n"; break;
        case 9: cout << "snake\n"; break;
        case 10: cout << "horse\n"; break;
        case 11: cout << "sheep\n"; break;
    }
    return 0;
}
```

### problem 12: days of the week and intentional fall-through

using fall-through without `break` to group multiple cases into a single logical branch:

```cpp
#include <iostream>
using namespace std;

int main() {
    int day_index;
    cout << "enter day index (1-7): ";
    cin >> day_index;

    switch (day_index) {
        case 1:
        case 2:
        case 3:
        case 4:
        case 5:
            cout << "weekdays\n";
            break;
        case 6:
        case 7:
            cout << "weekend\n";
            break;
        default:
            cout << "invalid day index\n";
            break;
    }
    return 0;
}
```

### problem 13: basic four-operation calculator via switch

```cpp
#include <iostream>
using namespace std;

int main() {
    double num1, num2;
    char op;
    cout << "enter two numbers: ";
    cin >> num1 >> num2;
    cout << "enter operator (+, -, *, /): ";
    cin >> op;

    switch (op) {
        case '+': cout << num1 + num2 << "\n"; break;
        case '-': cout << num1 - num2 << "\n"; break;
        case '*': cout << num1 * num2 << "\n"; break;
        case '/':
            if (num2 != 0) cout << num1 / num2 << "\n";
            else cout << "error: division by zero\n";
            break;
        default:
            cout << "invalid operator\n";
            break;
    }
    return 0;
}
```

### problem 14: days in a month (february leap year inside switch)

```cpp
#include <iostream>
using namespace std;

int main() {
    int month, year;
    cout << "enter month (1-12) and year: ";
    cin >> month >> year;

    int days = 0;

    switch (month) {
        case 1: case 3: case 5: case 7: case 8: case 10: case 12:
            days = 31;
            break;
        case 4: case 6: case 9: case 11:
            days = 30;
            break;
        case 2:
            if (((year % 4 == 0) && (year % 100 != 0)) || (year % 400 == 0)) {
                days = 29;
            } else {
                days = 28;
            }
            break;
        default:
            cout << "invalid month index\n";
            break;
    }

    if (month >= 1 && month <= 12) {
        cout << "month " << month << " in year " << year << " has " << days << " days.\n";
    }
    return 0;
}
```

### problem 15: rock, paper, scissors game

```cpp
#include <iostream>
#include <cstdlib>
#include <ctime>
using namespace std;

int main() {
    srand(time(0));
    int user_choice;
    cout << "enter choice (0: scissors, 1: rock, 2: paper): ";
    cin >> user_choice;

    int comp_choice = rand() % 3;

    if (user_choice == comp_choice) {
        cout << "no winner (draw)!\n";
    } else {
        bool user_won = (user_choice == 0 && comp_choice == 2) ||
                        (user_choice == 1 && comp_choice == 0) ||
                        (user_choice == 2 && comp_choice == 1);

        if (user_won) {
            cout << "you won!\n";
        } else {
            cout << "you lost!\n";
        }
    }
    return 0;
}
```

---

## character handling, ascii codes, and cctype

characters store 1-byte numeric ascii codes:
- `'a'` = 97, `'b'` = 98, `'?'` = 63, `'A'` = 65, `'Z'` = 90
- `'2'` = 50, `'3'` = 51
- unicode escape: `char ch = '\u0041';` represents `'A'`.
- adding character literals performs arithmetic on their ascii codes: `'2' + '3'` evaluates to $50 + 51 = 101$.

### manual character range checks

```cpp
#include <iostream>
using namespace std;

int main() {
    char ch = 'B';

    if (ch >= 'A' && ch <= 'Z') {
        cout << ch << " is an uppercase letter\n";
    } else if (ch >= 'a' && ch <= 'z') {
        cout << ch << " is a lowercase letter\n";
    } else if (ch >= '0' && ch <= '9') {
        cout << ch << " is a digit\n";
    }
    return 0;
}
```

### cctype library functions

the `<cctype>` header provides character classification and case transformation:
- **`islower(ch)`**: returns non-zero if lowercase, 0 if false.
- **`isupper(ch)`**: returns non-zero if uppercase, 0 if false.
- **`tolower(ch)`**: returns lowercase ascii code (cast back with `(char)tolower(ch)`).
- **`toupper(ch)`**: returns uppercase ascii code (cast back with `(char)toupper(ch)`).

> **core evaluation principle in c++:** any non-zero value evaluates to boolean `true` (1); only zero evaluates to `false` (0).

```cpp
#include <iostream>
#include <cctype>
using namespace std;

int main() {
    char ch1 = 'c';
    cout << "isupper('c'): " << isupper(ch1) << "\n"; // outputs 0 (false)

    char ch2 = 'C';
    cout << "tolower('C') char: " << (char)tolower(ch2) << "\n"; // 'c'

    char ch3 = 'd';
    cout << "toupper('d') char: " << (char)toupper(ch3) << "\n"; // 'D'
    return 0;
}
```

---

## ternary conditional operator (? :)

the ternary operator provides concise inline conditional assignments:
$$\text{condition} \; ? \; \text{expression\_if\_true} \; : \; \text{expression\_if\_false}$$

```cpp
#include <iostream>
using namespace std;

int main() {
    int x = 10;
    int result = (x > 0) ? x + 20 : x - 20;
    cout << "result: " << result << "\n"; // 30

    int number1 = 10;
    int number2 = 30;
    int max_val = (number1 > number2) ? number1 : number2;
    cout << "max value: " << max_val << "\n"; // 30
    return 0;
}
```
