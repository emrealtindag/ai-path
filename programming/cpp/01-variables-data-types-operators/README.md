# variables, data types, and operators

notes from the first weeks of class: printing to the screen, comments, variables, types, division rules, cmath, iomanip, and increment/decrement operators. all code uses `using namespace std;`.

---

## first program and using namespace std

```cpp
#include <iostream>
using namespace std;

int main() {
    std::cout << "Hello World!\n"; // works with or without using namespace std
    cout << "emre selam!\n";       // works only because of using namespace std
    return 0;
}
```

- `#include <iostream>` adds the library that has `cout` and `cin`.
- `int main()` is where the program starts.
- without `using namespace std;` you have to write `std::cout`. with it, just `cout`.
- same idea in opencv: after `using namespace cv;` you can write `Mat` instead of `cv::Mat`.
- `return 0;` means the program finished without errors.

---

## comments

the compiler skips comments. they are only for the person reading the code.

```cpp
#include <iostream>
using namespace std;

int main() {
    int my_variable = 50; // single line comment: assigned 50 to my first variable

    /* multi-line comment:
       cout << "this line does not run";
       cout << "this one doesn't either"; */

    cout << my_variable << endl;
    return 0;
}
```

---

## going to a new line: endl vs \n

```cpp
cout << "Hello" << endl << endl; // way 1: every endl moves one line down (2 lines here)
cout << "Hello World\n";         // way 2: \n inside the string
```

both look the same on the screen. the difference is that `endl` also flushes the output buffer and `\n` doesn't.

---

## escape characters

- `\n`: new line
- `\t`: tab (a few spaces)
- `\"` and `\'`: print quotes inside a string

### problem 1: three two one and quotes

```cpp
#include <iostream>
using namespace std;

int main() {
    cout << "Three\n" << "Two\n" << "One\n";
    cout << " \"Emre\" " << endl;     // "Emre"
    cout << " \'Altindag\' " << endl; // 'Altindag'
    cout << "Emre\tAltindag" << endl; // Emre    Altindag
    cout << "Emre\nAltindag" << endl; // Emre and Altindag on two lines
    return 0;
}
```

### problem 2: roses are red

```cpp
#include <iostream>
using namespace std;

int main() {
    cout << "Roses are red,\n\tViolets are blue,\n"
         << "Sugar is sweet,\n\tBut I have \"commitment issues\",\n\t"
         << "So I'd rather just be friends\n\tAt this point in our " << "relationship.\n";

    cout << "Emre Altindag " << endl;
    cout << "Emre" << " Altindag" << endl;
    return 0;
}
```

output:

```text
Roses are red,
        Violets are blue,
Sugar is sweet,
        But I have "commitment issues",
        So I'd rather just be friends
        At this point in our relationship.
Emre Altindag
Emre Altindag
```

### problem 3: text vs math inside cout

anything inside quotes is printed as text. without quotes it gets calculated.

```cpp
#include <iostream>
using namespace std;

int main() {
    cout << "Welcome " << "to " << "C++ " << endl;
    cout << "25 and 45 are added " << "25 + 45" << endl; // 25 and 45 are added 25 + 45
    cout << "25 and 45 are added " << 25 + 45 << endl;   // 25 and 45 are added 70
    return 0;
}
```

---

## variable names

- has to start with a letter or `_`.
- can't start with a digit: `int 3my_first = 50;` gives an error.
- c++ is case sensitive: `my_Variable` and `my_variable` are two different variables.

### problem 4: four operations on one variable

```cpp
#include <iostream>
using namespace std;

int main() {
    int my_variable = 50;
    cout << "I am very happy because I learned how to define a variable :)" << endl;
    cout << "My first variable is " << my_variable << endl;
    cout << "Double of variable is " << my_variable * 2 << endl;
    cout << my_variable + my_variable << endl;
    cout << my_variable << " + " << my_variable << " = " << my_variable + my_variable << endl; // 50 + 50 = 100
    cout << my_variable << " - " << my_variable << " = " << my_variable - my_variable << endl; // 50 - 50 = 0
    cout << my_variable << " * " << my_variable << " = " << my_variable * my_variable << endl; // 50 * 50 = 2500
    cout << my_variable << " / " << my_variable << " = " << my_variable / my_variable << endl; // 50 / 50 = 1
    return 0;
}
```

---

## data types

- `int`: whole numbers, 4 bytes.
- `double`: decimal numbers, 8 bytes, about 15 digits.
- `float`: decimal numbers, 4 bytes, about 7 digits.
- `char`: one character in single quotes like `'a'`, 1 byte.
- `bool`: `true` or `false`, 1 byte.
- `string`: text in double quotes like `"emre"`, needs `#include <string>`.

### problem 5: changing a variable's value

a variable can get a new value later. the old value is gone.

```cpp
#include <iostream>
using namespace std;

int main() {
    int sides = 7;
    cout << "A heptagon has " << sides << " sides." << endl;

    sides = 10;
    cout << "A decagon has " << sides << " sides." << endl;

    sides = 12;
    cout << "A dodecagon has " << sides << " sides." << endl;

    double i = 50.0;
    double k = i + 55.125; // 105.125
    double j = k + 1.0;    // 106.125
    cout << " i= " << i << " j= " << j << " k= " << k << endl;
    return 0;
}
```

---

## reading input with cin

```cpp
double radius;
cout << "enter the radius: ";
cin >> radius;
```

when the program reaches `cin >>` it stops and waits for you to type something. if there is no `cin` at all, the program runs to the end right away and you only see "press any key to close this window".

---

## integer division and casting

- `int / int` gives an `int`. the decimal part is cut off.
- `double / int`, `int / double`, `double / double` all give a `double`.

### problem 6: division rules

```cpp
#include <iostream>
using namespace std;

int main() {
    int x = 100;
    int y = 50;
    cout << x << " / " << y << " = " << x / y << endl;           // 2
    cout << y << " / " << x << " = " << y / x << endl;           // 0, int / int cuts the decimals
    cout << y << " / " << x << " = " << (double)y / x << endl;   // 0.5

    cout << 8 / 3 << endl;        // 2
    cout << (float)8 / 3 << endl; // 2.66667
    cout << 8.0 / 3 << endl;      // 2.66667
    cout << 8 / 3.0 << endl;      // 2.66667
    cout << 8.0 / 3.0 << endl;    // 2.66667

    cout << 1 / 5 << endl;           // 0
    cout << 1.0 / 5 << endl;         // 0.2
    cout << (double)1 / 5 << endl;   // 0.2

    double number = 1.125;
    cout << (int)number << endl;              // 1
    cout << static_cast<int>(number) << endl; // 1, same job as (int)
    return 0;
}
```

`static_cast<int>(...)` and `(int)` do the same thing here: they convert the type (int, float, double).

---

## remainder with %

`%` gives the remainder of a division:

- `10 / 2 = 5`
- `10 % 2 = 0`
- `number % 2` is `0` when the number is even.

### problem 7: seconds to minutes

```cpp
#include <iostream>
using namespace std;

int main() {
    int seconds;
    cout << "Enter an integer for seconds: ";
    cin >> seconds;

    int minutes = seconds / 60;
    int remaining_seconds = seconds % 60;

    cout << seconds << " seconds is " << minutes << " minutes and " << remaining_seconds << " seconds" << endl;
    return 0;
}
```

---

## cmath

`#include <cmath>` gives `sqrt` (square root) and `pow` (power).

```cpp
cout << "sqrt of 36 is " << sqrt(36) << endl;       // 6
cout << "2^3 = " << pow(2, 3) << endl;              // 8
cout << "8^(1/3) = " << pow(8, 1.0 / 3.0) << endl;  // 2
cout << pow(8, 1 / 3) << endl;                      // 1, because 1 / 3 is int division = 0 and 8^0 = 1
```

for a cube root the exponent has to be `1.0 / 3.0`, not `1 / 3`.

### problem 8: circle area

```cpp
#include <iostream>
#include <cmath>
using namespace std;

int main() {
    double radius;
    double area;

    cout << "Enter the radius of your circle = ";
    cin >> radius;

    // area = radius * radius * 3.14; // long way
    area = pow(radius, 2) * 3.14;

    cout << "The area of the circle is " << area << endl;
    return 0;
}
```

### problem 9: formula with square root and cube root

$$y = x + \frac{\sqrt{x + 4}}{x^2 + \sqrt[3]{x + 2}}$$

```cpp
#include <iostream>
#include <cmath>
using namespace std;

int main() {
    double x, y;
    cout << "enter a number = ";
    cin >> x;

    y = x + (sqrt(x + 4) / (pow(x, 2) + pow(x + 2, 1.0 / 3)));
    cout << "y = " << y << endl;
    return 0;
}
```

---

## const

`const` makes a value fixed. it can't be changed later in the program.

### problem 10: celsius to fahrenheit

```cpp
#include <iostream>
using namespace std;

int main() {
    const int BASE = 32;
    double celsius;
    double fahrenheit;

    cout << "enter celsius number = ";
    cin >> celsius;

    fahrenheit = (9.0 / 5.0) * celsius + BASE; // 9 / 5 would be 1 (int division)
    cout << "result of fahrenheit " << fahrenheit << endl;
    return 0;
}
```

---

## iomanip: setprecision and fixed

### problem 11: printing pi with different precision

```cpp
#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    double pi = 3.141592653589793;

    cout << "Default: " << pi << endl;                  // 3.14159

    cout << fixed << setprecision(2);
    cout << "Fixed (2 decimal places): " << pi << endl; // 3.14

    cout << setprecision(5);
    cout << "Fixed (5 decimal places): " << pi << endl; // 3.14159
    return 0;
}
```

- by default `cout` shows 6 digits in total.
- `setprecision(n)` without `fixed` counts all digits: `setprecision(2)` on pi prints `3.1`.
- with `fixed` it counts only the digits after the decimal point.
- once you set them, `fixed` and `setprecision` stay on for every `cout` after that.

### problem 12: tax with 2 decimals using int()

another way to keep 2 decimals without iomanip: multiply by 100, cut the decimals with `int()`, then divide by `100.0`.

```cpp
#include <iostream>
using namespace std;

int main() {
    double purchase_amount;
    double tax;

    cout << "enter purchase amount: ";
    cin >> purchase_amount;

    tax = int(purchase_amount * 0.10 * 100) / 100.0;
    // cout << fixed << setprecision(2); // the iomanip way

    cout << "tax amount you should pay is " << tax << endl;
    return 0;
}
```

- `int()` cuts the decimals, it doesn't round. 12.349 becomes 12.34.
- the `* 100` matters: `int(purchase_amount * 0.10) / 100.0` gives 0.15 for 150 instead of 15.
- dividing by `100.0` (not `100`) keeps the result a double.

---

## compound operators

```cpp
number = number * 2;  // same as number *= 2;
number = number + 2;  // same as number += 2;
number = number % 2;  // same as number %= 2;  (remainder after dividing by 2)
```

### problem 13: number of students

```cpp
#include <iostream>
using namespace std;

int main() {
    int numberOfStudents = 36;
    cout << "First week there are " << numberOfStudents << " students.." << endl;

    numberOfStudents += 10;
    // numberOfStudents = numberOfStudents + 10; // same thing
    cout << "After Add Drop Week we are " << numberOfStudents << " students.." << endl; // 46
    return 0;
}
```

---

## increment and decrement: prefix vs postfix

- `x = x + 1`, `x += 1`, `++x` and `x++` all add 1 to x.
- the difference only shows when you assign the result somewhere:
  - `++x` (prefix): increase first, then use the new value.
  - `x++` (postfix): use the old value first, then increase.
- same rule for `--x` and `x--`.

### problem 14: tracing the values

```cpp
#include <iostream>
using namespace std;

int main() {
    int i = 1;
    int j = ++i;   // i becomes 2, j gets 2
    cout << "i= " << i << " j= " << j << endl; // i= 2 j= 2

    int x = 1;
    int y = x++;   // y gets 1, then x becomes 2
    cout << "x= " << x << " y= " << y << endl; // x= 2 y= 1

    int m = 2;
    int n = m--;   // n gets 2, then m becomes 1
    cout << "m= " << m << " n= " << n << endl; // m= 1 n= 2

    int p = 2;
    int r = --p;   // p becomes 1, r gets 1
    cout << "p= " << p << " r= " << r << endl; // p= 1 r= 1
    return 0;
}
```

---

## homework: triangle angles from three points

the user enters three points (x1, y1), (x2, y2), (x3, y3). first find the side lengths with the distance formula, then the angles with the law of cosines:

$$a = \sqrt{(y_3 - y_2)^2 + (x_3 - x_2)^2}$$

$$\cos(A) = \frac{b^2 + c^2 - a^2}{2bc}, \quad \cos(B) = \frac{a^2 + c^2 - b^2}{2ac}, \quad \cos(C) = \frac{a^2 + b^2 - c^2}{2ab}$$

`acos` returns radians, so multiply by `180 / PI` to get degrees. `acos(-1)` gives pi.

```cpp
#include <iostream>
#include <cmath>
#include <iomanip>
using namespace std;

int main() {
    double cos_A, cos_B, cos_C;
    double x1, x2, x3, y1, y2, y3, a, b, c;

    cout << "enter x1: ";
    cin >> x1;
    cout << "enter y1: ";
    cin >> y1;
    cout << "enter x2: ";
    cin >> x2;
    cout << "enter y2: ";
    cin >> y2;
    cout << "enter x3: ";
    cin >> x3;
    cout << "enter y3: ";
    cin >> y3;

    a = sqrt(pow(y3 - y2, 2) + pow(x3 - x2, 2));
    b = sqrt(pow(y3 - y1, 2) + pow(x3 - x1, 2));
    c = sqrt(pow(y2 - y1, 2) + pow(x2 - x1, 2));

    cout << fixed << setprecision(2);
    cos_A = (pow(b, 2) + pow(c, 2) - pow(a, 2)) / (2 * b * c);
    cos_B = (pow(a, 2) + pow(c, 2) - pow(b, 2)) / (2 * a * c);
    cos_C = (pow(a, 2) + pow(b, 2) - pow(c, 2)) / (2 * a * b);

    const double PI = acos(-1);
    double angle_A = acos(cos_A) * (180 / PI);
    double angle_B = acos(cos_B) * (180 / PI);
    double angle_C = acos(cos_C) * (180 / PI);

    cout << "angle A: " << angle_A << " angle B: " << angle_B << " angle C: " << angle_C << endl;
    return 0;
}
```
