# strings

character primitives, std string memory representation, contiguous indexing, traversal patterns, and line extraction via getline.

---

## char versus std::string

c++ distinguishes between single character primitives and dynamic string objects:

- **`char`**: fundamental 1-byte integer type storing a single ascii code enclosed in single quotes (`'a'`).
- **`std::string`**: standard library container `<string>` managing a contiguous, dynamically allocated array of characters enclosed in double quotes (`"emre"`).

```cpp
char single_char = 'a';        // 1 byte on stack (ascii 97)
std::string text = "emre";     // dynamic container managing 4 characters
```

---

## memory layout and array-style indexing

characters inside a `std::string` are stored contiguously in memory with **zero-based indexing**:

```text
std::string name = "emre";

index:        0      1      2      3
character:  ['e']  ['m']  ['r']  ['e']
byte size:   1 B    1 B    1 B    1 B
```

- **first character**: `name[0]` (returns `'e'`)
- **last character**: `name[name.length() - 1]` (returns `'e'`)
- **string length**: `name.length()` or `name.size()` (returns `4`)

```cpp
std::string name = "emre";

std::cout << "first character: " << name[0] << "\n";
std::cout << "total length: " << name.length() << "\n";
std::cout << "last character: " << name[name.length() - 1] << "\n";
```

---

## string traversal patterns

### 1. index-based traversal

accesses each character position using a standard counter loop:

```cpp
for (size_t i = 0; i < name.length(); i++) {
    std::cout << "character at index " << i << ": " << name[i] << "\n";
}
```

### 2. modern range-based for loop (c++11)

iterates directly over each character element without manual index arithmetic:

```cpp
for (char ch : name) {
    std::cout << ch << " ";
}
```

---

## user input: cin versus getline

standard extraction `std::cin >> str` stops reading as soon as it encounters a whitespace character (space, tab, newline). to capture entire sentences with spaces, use `std::getline()`.

```cpp
#include <iostream>
#include <string>

std::string surname;

// cin >> surname;       // stops at the first space!
std::getline(std::cin, surname); // reads the entire line including spaces
```

### the cin.ignore() trap

when reading numbers with `cin >> num` before a `getline()`, the trailing newline character `\n` remains in the input buffer. `getline()` immediately reads that leftover newline and returns an empty string. clear the buffer using `std::cin.ignore()`:

```cpp
int age;
std::cin >> age;
std::cin.ignore(); // discard trailing newline from stream buffer

std::string full_name;
std::getline(std::cin, full_name); // now reads input correctly
```

---

## common traps and best practices

- **single versus double quotes**: `'hello'` is invalid syntax; double quotes `"hello"` denote a null-terminated string literal.
- **out-of-bounds access**: accessing `name[name.length()]` reads unallocated memory (or the null terminator) without throwing an exception. use `name.at(index)` if bounds checking is required.
- **string concatenation**: `std::string s = "hello " + "world";` fails because two string literals (`const char*`) cannot be added directly. at least one operand must be a `std::string`.
