# variables, data types, and operators

core syntax, fundamental types, memory sizes, arithmetic operators, type casting, compound assignments, and stream i/o formatting derived from university lecture problems in c++ (all examples assume using namespace std;).

---

## program anatomy, namespaces, and escape sequences

every executable c++ program requires a translation unit with an entry point `main()`. standard i/o is accessed via `<iostream>`.

### understanding namespaces and using namespace std

```cpp
#include <iostream>
using namespace std;
```

- **the `using namespace` mechanism**: brings standard identifiers into the global namespace. for instance, in opencv programming, instead of writing `cv::Mat` on every line, adding `using namespace cv;` allows writing `Mat` directly. similarly, `using namespace std;` lets us write `cout`, `cin`, and `endl` directly without repetitive `std::` prefixes.
- **`return 0;`**: standard exit code indicating successful process execution.

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

### problem 2: multi-line escape sequences and formatted poetry

demonstrates multi-line stream chaining with tab indents and escaped quotes:

```cpp
#include <iostream>
using namespace std;

int main() {
    cout << "Roses are red,\n\tViolets are blue,\n"
         << "Sugar is sweet,\n\tBut I have \"commitment issues\",\n\t"
         << "So I'd rather just be friends\n\tAt this point in our relationship.\n";
    cout << "Emre Altindag" << endl;
    cout << "Emre" << " Altindag" << endl;
    return 0;
}
```

### problem 3: string literals versus arithmetic evaluation

quoted expressions represent literal text, while bare expressions evaluate mathematically:

```cpp
#include <iostream>
using namespace std;

int main() {
    cout << "Welcome " << "to " << "C++" << endl;
    cout << "25 and 45 are added: " << "25 + 45" << endl; // prints text: 25 + 45
    cout << "25 and 45 are added: " << 25 + 45 << endl;    // evaluates arithmetic: 70
    return 0;
}
```

---

## identifiers, case sensitivity, and variable rules

variable names (identifiers) must follow strict naming rules:
- must begin with a letter (`a-z`, `A-Z`) or underscore (`_`).
- cannot start with a digit (`3my_first = 50;` is invalid syntax).
- c++ is strictly **case-sensitive**: `my_Variable` and `my_variable` reference two completely distinct memory locations.

### problem 4: variable assignment and arithmetic operations

defining an integer variable and evaluating arithmetic operations formatted with labels:

```cpp
#include <iostream>
using namespace std;

int main() {
    int my_variable = 50; // assigned 50 to integer variable
    cout << "my first variable is " << my_variable << endl;
    cout << "double of variable is " << my_variable * 2 << endl;
    cout << my_variable << " + " << my_variable << " = " << my_variable + my_variable << endl; // 100
    cout << my_variable << " - " << my_variable << " = " << my_variable - my_variable << endl; // 0
    cout << my_variable << " * " << my_variable << " = " << my_variable * my_variable << endl; // 2500
    cout << my_variable << " / " << my_variable << " = " << my_variable / my_variable << endl; // 1
    return 0;
}
```

---

## fundamental data types and memory allocation

| type | byte size | typical value range | usage |
| :--- | :--- | :--- | :--- |
| `int` | 4 bytes | -2,147,483,648 to 2,147,483,647 | whole numbers, counts |
| `double` | 8 bytes | ~15 decimal digits of precision | standard floating-point |
| `float` | 4 bytes | ~7 decimal digits of precision | memory-constrained floats |
| `char` | 1 byte | -128 to 127 (ascii 0 to 127) | single characters in single quotes `'a'` |
| `bool` | 1 byte | `true` (1) or `false` (0) | conditional flags |

### problem 5: polygon side reassignment and decimal arithmetic

demonstrating variable mutability, sequential reassignments, and console input:

```cpp
#include <iostream>
using namespace std;

int main() {
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

    // cin >> requires input and pauses the terminal before exit
    int radius;
    cout << "enter radius: ";
    cin >> radius;
    return 0;
}
```

---

## integer division and type casting

when both operands are integers, the division operator `/` drops the decimal part completely (truncation toward zero). to preserve decimals, at least one operand must be a float or double.

### problem 6: division precision rules

```cpp
#include <iostream>
using namespace std;

int main() {
    cout << 8 / 3 << "\n";         // outputs 2 (integer truncation)
    cout << (float)8 / 3 << "\n";  // outputs 2.66667 (c-style cast)
    cout << 8.0 / 3 << "\n";       // outputs 2.66667 (double literal / int)
    cout << 8 / 3.0 << "\n";       // outputs 2.66667 (int / double literal)
    cout << 8.0 / 3.0 << "\n";     // outputs 2.66667 (double / double)

    // c++ static_cast and c-style cast:
    double num = 1.125;
    cout << (int)num << "\n";               // outputs 1
    cout << static_cast<int>(num) << "\n";  // outputs 1 (type-safe static_cast)
    return 0;
}
```

---

## mathematical functions with cmath

the `<cmath>` library provides mathematical operations such as square root (`sqrt`) and power (`pow`).

### problem 7: circle area computation

```cpp
#include <iostream>
#include <cmath>
using namespace std;

int main() {
    double radius;
    cout << "enter circle radius: ";
    cin >> radius;

    double area = 3.14 * pow(radius, 2);
    cout << "circle area is: " << area << "\n";
    return 0;
}
```

### problem 8: complex formula with cube root

evaluating the formula:
$$y = x + \frac{\sqrt{x + 4}}{x^2 + \sqrt[3]{x + 2}}$$

to calculate cube root with `pow`, the exponent must be `1.0 / 3.0` (using `1 / 3` results in integer division `0` and evaluates to $x^0 = 1$):

```cpp
#include <iostream>
#include <cmath>
using namespace std;

int main() {
    double x, y;
    cout << "enter x: ";
    cin >> x;

    y = x + (sqrt(x + 4.0) / (pow(x, 2) + pow(x + 2.0, 1.0 / 3.0)));
    cout << "y = " << y << "\n";
    return 0;
}
```

---

## time and unit conversions

### problem 9: total seconds to minutes and remainder seconds

using integer division and modulo `%` for time conversions:

```cpp
#include <iostream>
using namespace std;

int main() {
    int total_seconds;
    cout << "enter total seconds: ";
    cin >> total_seconds;

    int minutes = total_seconds / 60;
    int remaining_seconds = total_seconds % 60;

    cout << total_seconds << " seconds is " << minutes << " minutes and " << remaining_seconds << " seconds.\n";
    return 0;
}
```

### problem 10: fahrenheit to celsius conversion with constants

using `const` to declare immutable parameters:

```cpp
#include <iostream>
using namespace std;

int main() {
    const int BASE = 32;
    double celsius;
    cout << "enter celsius: ";
    cin >> celsius;

    // 9.0 / 5.0 must be written with floating-point literals
    double fahrenheit = (9.0 / 5.0) * celsius + BASE;
    cout << "fahrenheit: " << fahrenheit << "\n";
    return 0;
}
```

---

## stream formatting with iomanip

the `<iomanip>` header formats decimal precision and stream output:

### problem 11: purchase tax calculation with 2 decimal precision

demonstrating fixed-point format and `setprecision` behavior:

```cpp
#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    double purchase_amount = 150.0;
    cout << "enter purchase amount: ";
    cin >> purchase_amount;

    double tax = purchase_amount * 0.10;

    cout << fixed << setprecision(2);
    cout << "tax amount you should pay is: " << tax << "\n"; // outputs formatted decimal (e.g. 15.00)
    return 0;
}
```

---

## compound assignment operators

compound operators combine arithmetic calculation with variable reassignment:
- `x += y` $\equiv$ `x = x + y`
- `x -= y` $\equiv$ `x = x - y`
- `x *= y` $\equiv$ `x = x * y`
- `x /= y` $\equiv$ `x = x / y`
- `x %= y` $\equiv$ `x = x % y` (remainder after division)

### problem 12: student enrollment update

```cpp
#include <iostream>
using namespace std;

int main() {
    int number_of_students = 36;
    cout << "first week there are " << number_of_students << " students.\n";

    number_of_students += 10; // number_of_students = number_of_students + 10
    cout << "after add/drop week we are " << number_of_students << " students.\n";

    int val = 10;
    val *= 2; // 20
    val %= 3; // 2
    cout << "val: " << val << "\n";
    return 0;
}
```

---

## prefix vs postfix increment and decrement operators

- **prefix (`++x`, `--x`)**: modifies the variable first, then returns the updated value.
- **postfix (`x++`, `x--`)**: returns the current value for evaluation first, then modifies the variable in memory.

### problem 13: prefix vs postfix tracing

```cpp
#include <iostream>
using namespace std;

int main() {
    // increment
    int i = 1;
    int j = ++i; // i becomes 2, j is assigned 2
    cout << "i: " << i << ", j: " << j << "\n"; // i: 2, j: 2

    int x = 1;
    int y = x++; // y is assigned 1, then x becomes 2
    cout << "x: " << x << ", y: " << y << "\n"; // x: 2, y: 1

    // decrement
    int m = 2;
    int n = m--; // n is assigned 2, then m becomes 1
    cout << "m: " << m << ", n: " << n << "\n"; // m: 1, n: 2

    int p = 2;
    int r = --p; // p becomes 1, then r is assigned 1
    cout << "p: " << p << ", r: " << r << "\n"; // p: 1, r: 1
    return 0;
}
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
