# strings

char vs string, indexes, length, looping over a string, and reading full lines with getline. all code uses `using namespace std;`.

---

## using namespace std

```cpp
#include <iostream>
#include <string>
using namespace std;
```

with `using namespace std;` you can write `string`, `cout`, `cin` and `getline` instead of `std::string`, `std::cout` and so on. that's how we write it in class.

in big projects, and especially in header files (`.h`), people usually skip `using namespace std;` and write `std::` every time. the reason is that two libraries can have something with the same name, and then the compiler doesn't know which one you mean. for single-file programs like these it's fine.

---

## char vs string

- `char`: one character in single quotes, `'a'`. 1 byte.
- `string`: text in double quotes, `"emre"`. needs `#include <string>`.

```cpp
#include <iostream>
#include <string>
using namespace std;

int main() {
    char ch = 'a';
    cout << ch << endl;   // a

    string name = "emre";
    cout << name << endl; // emre
    return 0;
}
```

---

## indexes and length

the characters of a string are numbered starting from 0:

```text
string name = "emre";

index:      0    1    2    3
character:  e    m    r    e
```

- `name[0]` is the first character.
- `name.length()` is the number of characters (4 here). `name.size()` does the same.
- the last character is `name[name.length() - 1]`, because counting starts at 0.

```cpp
#include <iostream>
#include <string>
using namespace std;

int main() {
    string name = "emre";

    cout << name[0] << endl;                   // e
    cout << name[2] << endl;                   // r
    cout << name.length() << endl;             // 4
    cout << name[name.length() - 1] << endl;   // e
    cout << "there are " << name.length() << " characters inside my name" << endl;
    return 0;
}
```

---

## looping over a string

with an index:

```cpp
#include <iostream>
#include <string>
using namespace std;

int main() {
    string name = "emre";

    for (int i = 0; i < name.length(); i++) {
        cout << name[i] << endl; // name[0], name[1], name[2], name[3]
    }
    return 0;
}
```

`i < name.length()` and not `<=`, because the last index is `length() - 1`.

without an index (range-based for, c++11):

```cpp
for (char ch : name) {
    cout << ch << " "; // e m r e
}
```

---

## cin vs getline

`cin >>` stops reading at the first space, so it only gets one word. `getline(cin, text)` reads the whole line, spaces included.

```cpp
#include <iostream>
#include <string>
using namespace std;

int main() {
    string message;
    cout << "Enter a line of text = " << endl;
    getline(cin, message);

    cout << "you entered: \"" << message << "\"" << endl; // you entered: "emreye selam"
    return 0;
}
```

with `cin >> message` and the same input, `message` would only be `emreye`.

### the cin.ignore() problem

if you use `cin >>` for a number and then `getline`, the enter key you pressed after the number (`\n`) is still waiting in the input. `getline` reads that right away and you get an empty string. `cin.ignore()` throws that leftover `\n` away.

```cpp
#include <iostream>
#include <string>
using namespace std;

int main() {
    int age;
    cout << "enter your age: ";
    cin >> age;
    cin.ignore(); // removes the leftover enter

    string surname;
    cout << "enter your surname = ";
    getline(cin, surname);

    cout << surname << " " << age << endl;
    return 0;
}
```

---

## common mistakes

- `'hello'` is wrong. single quotes are only for one character. text goes in double quotes: `"hello"`.
- `name[5]` on `"emre"` goes past the end of the string. c++ doesn't stop you, you just get garbage or a crash. `name.at(5)` checks the index and throws an `out_of_range` error instead.
- `string s = "hello " + "world";` doesn't compile, two quoted texts can't be added with `+`. one side has to be a `string` first: `string s = "hello "; s = s + "world";`
