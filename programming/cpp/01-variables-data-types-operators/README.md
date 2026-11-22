# variables, data types, and operators

core syntax, fundamental types, memory sizes, arithmetic operators, type casting, and stream i/o formatting derived from university lecture problems in c++.

---

## program anatomy and escape sequences

every executable c++ program requires a translation unit with an entry point `main()`. standard i/o is accessed via `<iostream>`.

### problem 1: formatted console output and escape characters

special characters format output alignment without adding extra libraries:
- `\n`: newline character (moves cursor to the next line).
- `\t`: horizontal tab character (inserts 4 to 8 space columns).
- `\"` and `\'`: escape quotes inside string literals.

```cpp
#include <iostream>
using namespace std;

int main() {
    cout << "Three\n" << "Two\n" << "One\n";
    cout << "\"Emre\"" << endl;
    cout << "\'Altindag\'" << endl;
    cout << "Emre\tAltindag" << endl; // tab indentation
    return 0;
}
```

---

## identifiers, case sensitivity, and variable rules

variable names (identifiers) must follow strict naming rules:
- must begin with a letter (`a-z`, `A-Z`) or underscore (`_`).
- cannot start with a digit (`3my_first = 50;` is invalid syntax).
- c++ is strictly **case-sensitive**: `my_Variable` and `my_variable` reference two completely distinct memory locations.

---

## fundamental data types and memory allocation

| type | byte size | typical value range | usage |
| :--- | :--- | :--- | :--- |
| `int` | 4 bytes | -2,147,483,648 to 2,147,483,647 | whole numbers, counts |
| `double` | 8 bytes | ~15 decimal digits of precision | standard floating-point |
| `float` | 4 bytes | ~7 decimal digits of precision | memory-constrained floats |
| `char` | 1 byte | -128 to 127 (ascii 0 to 127) | single characters in single quotes `'a'` |
| `bool` | 1 byte | `true` (1) or `false` (0) | conditional flags |

### problem 2: polygon side reassignment and decimal arithmetic

demonstrating variable mutability and sequential floating-point calculations:

```cpp
int sides = 7;
cout << "a heptagon has " << sides << " sides.\n";

sides = 10;
cout << "a decagon has " << sides << " sides.\n";

sides = 12;
cout << "a dodecagon has " << sides << " sides.\n";

double i = 50.0;
double k = i + 55.125;   // 105.125
double j = k + 1.0;      // 106.125
cout << "i = " << i << ", j = " << j << ", k = " << k << "\n";
```

---

## integer division and type casting

when both operands are integers, the division operator `/` drops the decimal part completely. to preserve decimals, at least one operand must be a float or double.

### problem 3: division precision rules

```cpp
cout << 8 / 3 << "\n";         // outputs 2 (integer truncation)
cout << (float)8 / 3 << "\n";  // outputs 2.66667 (c-style cast)
cout << 8.0 / 3 << "\n";       // outputs 2.66667 (double literal / int)
cout << 8 / 3.0 << "\n";       // outputs 2.66667 (int / double literal)
cout << 8.0 / 3.0 << "\n";     // outputs 2.66667 (double / double)

// modern c++ type-safe static_cast:
double num = 1.125;
cout << static_cast<int>(num) << "\n"; // outputs 1 (truncates to int)
```

---

## mathematical functions with cmath

the `<cmath>` library provides mathematical operations such as square root (`sqrt`) and power (`pow`).

### problem 4: circle area computation

```cpp
#include <cmath>

double radius;
cout << "enter circle radius: ";
cin >> radius;

double area = 3.14 * pow(radius, 2);
cout << "circle area is: " << area << "\n";
```

### problem 5: complex formula with cube root

evaluating the formula:
$$y = x + \frac{\sqrt{x + 4}}{x^2 + \sqrt[3]{x + 2}}$$

to calculate cube root with `pow`, the exponent must be `1.0 / 3.0` (using `1 / 3` results in integer division `0` and evaluates to $x^0 = 1$!):

```cpp
double x, y;
cout << "enter x: ";
cin >> x;

y = x + (sqrt(x + 4.0) / (pow(x, 2) + pow(x + 2.0, 1.0 / 3.0)));
cout << "y = " << y << "\n";
```

---

## time and unit conversions

### problem 6: total seconds to minutes and remainder seconds

using integer division and modulo `%` for time conversions:

```cpp
int total_seconds;
cout << "enter total seconds: ";
cin >> total_seconds;

int minutes = total_seconds / 60;
int remaining_seconds = total_seconds % 60;

cout << total_seconds << " seconds is " << minutes << " minutes and " << remaining_seconds << " seconds.\n";
```

### problem 7: fahrenheit to celsius conversion with constants

using `const` to declare immutable parameters:

```cpp
const int BASE = 32;
double celsius;
cout << "enter celsius: ";
cin >> celsius;

// 9.0 / 5.0 must be written with floating-point literals
double fahrenheit = (9.0 / 5.0) * celsius + BASE;
cout << "fahrenheit: " << fahrenheit << "\n";
```

---

## stream formatting with iomanip

the `<iomanip>` header formats decimal precision and table alignments:

### problem 8: purchase tax calculation with 2 decimal precision

```cpp
#include <iomanip>

double purchase_amount = 150.0;
double tax = purchase_amount * 0.10;

cout << fixed << setprecision(2);
cout << "tax amount to pay: $" << tax << "\n"; // outputs 15.00
```

---

## prefix vs postfix increment and decrement operators

- **`++x` (prefix)**: increments the variable first, then returns the newly updated value.
- **`x++` (postfix)**: returns the original value for evaluation first, then increments the variable afterwards.

### problem 9: prefix vs postfix tracing

```cpp
int i = 1;
int j = ++i; // i becomes 2, j is assigned 2
cout << "i: " << i << ", j: " << j << "\n"; // i: 2, j: 2

int x = 1;
int y = x++; // y is assigned 1, then x becomes 2
cout << "x: " << x << ", y: " << y << "\n"; // x: 2, y: 1
```

---

## comprehensive problem: triangle angles from 3 2d points via law of cosines

given 3 vertex coordinates $(x_1, y_1), (x_2, y_2), (x_3, y_3)$, compute the side lengths $a, b, c$ and all internal angles in degrees using the law of cosines:

$$\cos(A) = \frac{b^2 + c^2 - a^2}{2bc}, \quad \cos(B) = \frac{a^2 + c^2 - b^2}{2ac}, \quad \cos(C) = \frac{a^2 + b^2 - c^2}{2ab}$$

```cpp
#include <iostream>
#include <cmath>
#include <iomanip>

using namespace std;

int main() {
    double x1 = 1.0, y1 = 1.0;
    double x2 = 4.0, y2 = 1.0;
    double x3 = 1.0, y3 = 5.0;

    // calculate side lengths via distance formula
    double a = sqrt(pow(x3 - x2, 2) + pow(y3 - y2, 2)); // side opposite to vertex 1
    double b = sqrt(pow(x3 - x1, 2) + pow(y3 - y1, 2)); // side opposite to vertex 2
    double c = sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2)); // side opposite to vertex 3

    // law of cosines
    double cos_A = (pow(b, 2) + pow(c, 2) - pow(a, 2)) / (2 * b * c);
    double cos_B = (pow(a, 2) + pow(c, 2) - pow(b, 2)) / (2 * a * c);
    double cos_C = (pow(a, 2) + pow(b, 2) - pow(c, 2)) / (2 * a * b);

    const double PI = acos(-1.0);
    double angle_A = acos(cos_A) * (180.0 / PI);
    double angle_B = acos(cos_B) * (180.0 / PI);
    double angle_C = acos(cos_C) * (180.0 / PI);

    cout << fixed << setprecision(2);
    cout << "side a: " << a << ", side b: " << b << ", side c: " << c << "\n";
    cout << "angle A: " << angle_A << " deg\n";
    cout << "angle B: " << angle_B << " deg\n";
    cout << "angle C: " << angle_C << " deg\n";
    return 0;
}
```
