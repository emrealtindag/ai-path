#include <iostream>
#include <cmath>
#include <cctype>

using namespace std;

int main() {
    // 1. 3-digit palindrome checker
    cout << "--- 1. palindrome check ---\n";
    int num = 171;
    int first_digit = num / 100;
    int last_digit = num % 10;
    cout << num << " is palindrome: " << (first_digit == last_digit ? "true" : "false") << "\n\n";

    // 2. quadratic equation solver (discriminant)
    cout << "--- 2. quadratic equation discriminant ---\n";
    double a = 1.0, b = -5.0, c = 6.0;
    double delta = pow(b, 2) - 4 * a * c;
    cout << "equation: " << a << "x^2 + " << b << "x + " << c << " = 0\n";
    cout << "delta: " << delta << "\n";
    if (delta > 0) {
        double r1 = (-b + sqrt(delta)) / (2 * a);
        double r2 = (-b - sqrt(delta)) / (2 * a);
        cout << "roots: x1 = " << r1 << ", x2 = " << r2 << "\n\n";
    }

    // 3. leap year verification
    cout << "--- 3. leap year check ---\n";
    int year = 2024;
    bool is_leap = ((year % 4 == 0) && (year % 100 != 0)) || (year % 400 == 0);
    cout << "year " << year << " is leap year: " << (is_leap ? "true" : "false") << "\n\n";

    // 4. chinese zodiac switch statement
    cout << "--- 4. chinese zodiac ---\n";
    int birth_year = 2004;
    cout << "birth year " << birth_year << " zodiac sign: ";
    switch (birth_year % 12) {
        case 0: cout << "monkey\n\n"; break;
        case 1: cout << "rooster\n\n"; break;
        case 2: cout << "dog\n\n"; break;
        case 3: cout << "pig\n\n"; break;
        case 4: cout << "rat\n\n"; break;
        case 5: cout << "ox\n\n"; break;
        case 6: cout << "tiger\n\n"; break;
        case 7: cout << "rabbit\n\n"; break;
        case 8: cout << "dragon\n\n"; break;
        case 9: cout << "snake\n\n"; break;
        case 10: cout << "horse\n\n"; break;
        case 11: cout << "sheep\n\n"; break;
    }

    // 5. days in a month with leap year logic inside switch
    cout << "--- 5. days in a month (february check) ---\n";
    int month = 2;
    int test_year = 2024;
    cout << "month " << month << " in year " << test_year << " has: ";
    switch (month) {
        case 1: case 3: case 5: case 7: case 8: case 10: case 12:
            cout << "31 days\n\n";
            break;
        case 4: case 6: case 9: case 11:
            cout << "30 days\n\n";
            break;
        case 2:
            if (((test_year % 4 == 0) && (test_year % 100 != 0)) || (test_year % 400 == 0)) {
                cout << "29 days (leap year)\n\n";
            } else {
                cout << "28 days\n\n";
            }
            break;
    }

    // 6. cctype character classification
    cout << "--- 6. cctype functions ---\n";
    char ch = 'b';
    cout << "character: " << ch << "\n";
    cout << "islower: " << (islower(ch) ? "true" : "false") << "\n";
    cout << "toupper: " << static_cast<char>(toupper(ch)) << "\n\n";

    // 7. ternary operator
    cout << "--- 7. ternary operator ---\n";
    int n1 = 10, n2 = 30;
    int max_val = (n1 > n2) ? n1 : n2;
    cout << "max of " << n1 << " and " << n2 << " is: " << max_val << "\n";

    return 0;
}
