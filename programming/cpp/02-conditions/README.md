# conditions

decision structures, boolean logic, relational comparisons, if-else chains, switch statements, and classroom algorithmic problems in c++.

---

## relational operators and boolalpha

relational expressions evaluate to boolean values (`true` or `false`). by default, c++ streams print `1` for true and `0` for false. the `boolalpha` manipulator forces the stream to print literal `"true"` or `"false"`:

```cpp
#include <iostream>
using namespace std;

int x = 2, y = 2;
cout << boolalpha;
cout << (x == y) << "\n"; // true
cout << (x != y) << "\n"; // false
cout << (x > y)  << "\n"; // false
cout << (x <= y) << "\n"; // true
```

---

## if, else if, else chains and validation

### problem 1: shape area selector (rectangle vs triangle)

interactive menu that selects formula based on user input:

```cpp
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
    cout << "invalid selection.\n";
}
```

### problem 2: 3-digit palindrome number checker

checks whether a 3-digit number reads identically forwards and backwards (e.g. 171, 454):

```cpp
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
```

### problem 3: quadratic equation solver (discriminant delta)

solves $a x^2 + b x + c = 0$ using discriminant $\Delta = b^2 - 4ac$:

```cpp
#include <cmath>

double a, b, c;
cout << "enter coefficients a, b, c: ";
cin >> a >> b >> c;

if (a == 0.0) {
    if (b != 0.0) {
        cout << "linear equation root: " << (-c / b) << "\n";
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
        cout << "one repeated real root: x = " << x << "\n";
    } else {
        double real_part = -b / (2 * a);
        double imag_part = sqrt(-delta) / (2 * a);
        cout << "two complex roots: " << real_part << " +- " << imag_part << "i\n";
    }
}
```

### problem 4: letter grade scale

```cpp
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
```

### problem 5: bmi (body mass index) calculation

formula: $\text{BMI} = \text{weight} / \text{height}^2$ (weight in kg, height in meters):

```cpp
double weight, height;
cout << "enter weight (kg) and height (m): ";
cin >> weight >> height;

double bmi = weight / pow(height, 2);

if (bmi < 18.5) {
    cout << "underweight\n";
} else if (bmi < 25.0) {
    cout << "normal weight\n";
} else if (bmi < 30.0) {
    cout << "overweight\n";
} else {
    cout << "obese\n";
}
```

### problem 6: leap year determination

a year is a leap year if:
- divisible by 4 AND not divisible by 100, OR
- divisible by 400.

```cpp
int year;
cout << "enter year: ";
cin >> year;

bool is_leap = ((year % 4 == 0) && (year % 100 != 0)) || (year % 400 == 0);

if (is_leap) {
    cout << year << " is a leap year\n";
} else {
    cout << year << " is not a leap year\n";
}
```

---

## random numbers and game algorithms

### problem 7: lottery game (2-digit number matching)

generates a random 2-digit lottery number (`rand() % 100`) and evaluates cash prizes:

```cpp
#include <cstdlib>
#include <ctime>

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
```

---

## switch statements and multi-way branching

### problem 8: chinese zodiac (year % 12)

maps `year % 12` to its corresponding animal sign using `switch`:

```cpp
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
```

### problem 9: days in a month (handling february leap years inside switch)

groups months with 31 and 30 days using intentional fall-through, with leap year evaluation inside case 2:

```cpp
int month, year;
cout << "enter month (1-12) and year: ";
cin >> month >> year;

switch (month) {
    case 1: case 3: case 5: case 7: case 8: case 10: case 12:
        cout << "31 days\n";
        break;
    case 4: case 6: case 9: case 11:
        cout << "30 days\n";
        break;
    case 2:
        if (((year % 4 == 0) && (year % 100 != 0)) || (year % 400 == 0)) {
            cout << "29 days (leap year)\n";
        } else {
            cout << "28 days\n";
        }
        break;
    default:
        cout << "invalid month index\n";
        break;
}
```

### problem 10: rock, paper, scissors game

```cpp
int user_choice;
cout << "enter 0 (scissors), 1 (rock), 2 (paper): ";
cin >> user_choice;

int comp_choice = rand() % 3;

if (user_choice == comp_choice) {
    cout << "draw!\n";
} else if ((user_choice == 0 && comp_choice == 2) ||
           (user_choice == 1 && comp_choice == 0) ||
           (user_choice == 2 && comp_choice == 1)) {
    cout << "you won!\n";
} else {
    cout << "computer won!\n";
}
```

---

## character handling and cctype functions

characters store numeric ascii values:
- `'a'` = 97, `'b'` = 98, `'A'` = 65, `'Z'` = 90
- `'2' + '3'` performs arithmetic on ascii values: $50 + 51 = 101$.

the `<cctype>` library provides classification and case transformation:

```cpp
#include <cctype>

char ch = 'b';
cout << islower(ch); // true (non-zero)
cout << isupper(ch); // false (0)
cout << (char)toupper(ch); // converts 'b' to 'B'
```

---

## ternary conditional operator (? :)

compact single-line conditional assignment:

```cpp
int x = 10;
int result = (x > 0) ? x + 20 : x - 20;

int n1 = 10, n2 = 30;
int max_val = (n1 > n2) ? n1 : n2; // 30
```
