#include <iostream>
#include <string>

int main() {
    // 1. char primitive vs std::string
    char initial = 'e';
    std::string name = "emre";

    std::cout << "--- 1. basic string and char properties ---\n";
    std::cout << "single character: " << initial << " (sizeof: " << sizeof(initial) << " byte)\n";
    std::cout << "string content: " << name << "\n";
    std::cout << "string length (.length()): " << name.length() << "\n";
    std::cout << "string size (.size()): " << name.size() << "\n\n";

    // 2. contiguous array indexing
    std::cout << "--- 2. zero-based indexing ---\n";
    std::cout << "name[0]: " << name[0] << "\n";
    std::cout << "name[1]: " << name[1] << "\n";
    std::cout << "name[2]: " << name[2] << "\n";
    std::cout << "name[3]: " << name[3] << "\n";
    std::cout << "last character via [length - 1]: " << name[name.length() - 1] << "\n\n";

    // 3. index-based traversal loop
    std::cout << "--- 3. index loop traversal ---\n";
    for (size_t i = 0; i < name.length(); i++) {
        std::cout << "index " << i << " contains: " << name[i] << "\n";
    }
    std::cout << "\n";

    // 4. modern range-based for loop
    std::cout << "--- 4. modern range-based traversal ---\n";
    for (char c : name) {
        std::cout << c << " ";
    }
    std::cout << "\n\n";

    // 5. string modification
    std::string greeting = "hello";
    greeting += " world";
    std::cout << "--- 5. string concatenation ---\n";
    std::cout << "concatenated string: " << greeting << "\n";

    return 0;
}
