# variables, types, and operators

core syntax, fundamental data types, type casting, arithmetic operators, and stream i/o formatting in c++.

---

## program anatomy and stream i/o

every executable c++ program requires a translation unit with an entry point function `main()`. standard library stream facilities are included via `<iostream>`.

```cpp
#include <iostream>

int main() {
    std::cout << "hello world!\n";
    return 0;
}
```

- **`#include <iostream>`**: preprocessor directive injecting standard stream declarations.
- **`std::cout`**: buffered output stream writing to standard output (stdout).
- **`<<`**: stream insertion operator chaining sequential tokens into the stream.
- **`\n` versus `std::endl`**: `\n` outputs an ascii newline character (byte `0x0a`). `std::endl` writes a newline and explicitly flushes the stream buffer via `std::flush()`, incurring an unnecessary system call overhead in tight loops.

### namespace hygiene

the `using namespace std;` directive pulls all standard identifiers into the global namespace. while common in introductory code, it creates name collisions in production projects:

```cpp
// avoid in header files and production code:
using namespace std;

// preferred modern practice: explicit qualification
std::cout << "clean scoping\n";
```

---

## fundamental type system and memory layout

variables reside in stack memory with fixed bit-widths determined by the data type and target architecture:

| type | size (bytes) | value range | typical use |
| :--- | :--- | :--- | :--- |
| `bool` | 1 | `true` (1) or `false` (0) | conditional flags |
| `char` | 1 | -128 to 127 (or 0 to 255) | single ascii characters (`'a'`) |
| `int` | 4 | -2,147,483,648 to 2,147,483,647 | integer counts, loop indices |
| `float` | 4 | ~1.17e-38 to ~3.40e+38 (~7 decimals) | single-precision float |
| `double` | 8 | ~2.22e-308 to ~1.79e+308 (~15 decimals) | default scientific float |

### stack memory allocation model

```text
[stack frame: main()]
+-----------------------------+-------------------+
| variable name & type        | memory value      |
+-----------------------------+-------------------+
| int x                       | 100               |
| int y                       | 50                |
| double tax_rate             | 0.100000000000000 |
+-----------------------------+-------------------+
```

---

## operators and arithmetic rules

c++ evaluates expressions according to strict operator precedence and type promotion rules.

### integer division versus floating-point division

when both operands are integers, the division operator `/` performs integer division and truncates the fractional remainder:

```cpp
int a = 8;
int b = 3;

std::cout << a / b;        // outputs 2 (fractional part discarded)
std::cout << 8.0 / 3;      // outputs 2.66667 (floating-point division)
```

### type conversion (casting)

to retain precision, at least one operand must be converted to a floating-point type:

```cpp
// c-style cast (legacy):
std::cout << (double)a / b;           // outputs 2.66667

// modern c++ static_cast (type-safe, explicit):
std::cout << static_cast<double>(a) / b; // outputs 2.66667
```

---

## formatted i/o with iomanip and cmath

user input is captured using the stream extraction operator `>>` from `std::cin`. numeric output formatting requires the `<iomanip>` header.

```cpp
#include <iostream>
#include <iomanip>
#include <cmath>

double purchase_amount = 150.0;
double tax_rate = 0.10;
double tax = purchase_amount * tax_rate;

// format to exactly 2 decimal places:
std::cout << std::fixed << std::setprecision(2);
std::cout << "tax amount: " << tax << "\n"; // outputs 15.00

// power computation via <cmath>
double radius = 5.0;
double circle_area = 3.14159 * std::pow(radius, 2);
```

---

## common traps and best practices

- **uninitialized variables**: declaring `int x;` leaves memory filled with whatever garbage bits previously occupied that stack address. always initialize: `int x = 0;` or `int x{0};`.
- **floating-point equality**: never test float equality using `==` due to roundoff errors; test `std::abs(a - b) < epsilon`.
- **cin buffer remainder**: `cin >> x;` leaves newline characters in the stream buffer, causing subsequent `getline()` calls to read empty strings unless cleared with `cin.ignore()`.
