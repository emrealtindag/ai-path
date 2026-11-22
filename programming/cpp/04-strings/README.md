# strings

character primitives, string memory representation, contiguous indexing, traversal patterns, and line extraction via getline with using namespace std.

---

## using namespace std in c++

in introductory c++ and university coursework, every program typically includes:

```cpp
#include <iostream>
#include <string>
using namespace std;
```

- **why classroom notes use `using namespace std;`**: it brings the standard library names (`cout`, `cin`, `string`, `getline`, `endl`) directly into the global scope. this eliminates the need to prefix every variable, type, and stream with `std::`, keeping handwritten notes, exam solutions, and algorithm code concise and readable.
- **difference in enterprise code**: in massive production systems or header files (`.h`), developers often avoid `using namespace std;` to prevent name collisions (namespace pollution). for single-file assignments, coursework, and competitive programming, `using namespace std;` is standard practice.

---

## char versus string

c++ distinguishes between single character primitives and dynamic string objects:

- **`char`**: fundamental 1-byte integer type storing a single ascii code enclosed in single quotes (`'a'`).
- **`string`**: standard library type provided by `<string>` that manages a contiguous, dynamically allocated array of characters enclosed in double quotes (`"emre"`).

```cpp
#include <iostream>
#include <string>
using namespace std;

int main() {
    char single_char = 'a';        // 1 byte on stack (ascii 97)
    string text = "emre";          // dynamic container managing 4 characters
    return 0;
}
```

---

## memory layout and array-style indexing

characters inside a `string` are stored contiguously in memory with **zero-based indexing**:

```text
string name = "emre";

index:        0      1      2      3
character:  ['e']  ['m']  ['r']  ['e']
byte size:   1 B    1 B    1 B    1 B
```

- **first character**: `name[0]` (returns `'e'`)
- **last character**: `name[name.length() - 1]` (returns `'e'`)
- **string length**: `name.length()` or `name.size()` (returns `4`)

```cpp
string name = "emre";

cout << "first character: " << name[0] << "\n";
cout << "total length: " << name.length() << "\n";
cout << "last character: " << name[name.length() - 1] << "\n";
```

---

## string traversal patterns

### 1. index-based traversal

accesses each character position using a standard counter loop:

```cpp
for (size_t i = 0; i < name.length(); i++) {
    cout << "character at index " << i << ": " << name[i] << "\n";
}
```

### 2. modern range-based for loop (c++11)

iterates directly over each character element without manual index arithmetic:

```cpp
for (char ch : name) {
    cout << ch << " ";
}
```

---

## user input: cin versus getline

standard extraction `cin >> str` stops reading as soon as it encounters a whitespace character (space, tab, newline). to capture entire sentences with spaces, use `getline()`.

```cpp
#include <iostream>
#include <string>
using namespace std;

string surname;

// cin >> surname;       // stops at the first space!
getline(cin, surname);   // reads the entire line including spaces
```

### the cin.ignore() trap

when reading numbers with `cin >> num` before a `getline()`, the trailing newline character `\n` remains in the input buffer. `getline()` immediately reads that leftover newline and returns an empty string. clear the buffer using `cin.ignore()`:

```cpp
int age;
cin >> age;
cin.ignore(); // discard trailing newline from stream buffer

string full_name;
getline(cin, full_name); // now reads input correctly
```

---

## common traps and best practices

- **single versus double quotes**: `'hello'` is invalid syntax; double quotes `"hello"` denote a string literal.
- **out-of-bounds access**: accessing `name[name.length()]` reads unallocated memory (or the null terminator) without throwing an exception. use `name.at(index)` if bounds checking is required.
- **string concatenation**: `string s = "hello " + "world";` fails because two string literals (`const char*`) cannot be added directly. at least one operand must be a `string` (e.g. `string s = string("hello ") + "world";` or `string s = "hello "; s += "world";`).
