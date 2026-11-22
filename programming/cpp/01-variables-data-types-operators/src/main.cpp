#include <iostream>
#include <iomanip>
#include <cmath>

int main() {
    // 1. stream output and variable initialization
    int x = 100;
    int y = 50;

    std::cout << "--- 1. basic arithmetic ---\n";
    std::cout << x << " + " << y << " = " << (x + y) << "\n";
    std::cout << x << " - " << y << " = " << (x - y) << "\n";
    std::cout << x << " * " << y << " = " << (x * y) << "\n";
    std::cout << x << " / " << y << " = " << (x / y) << "\n\n";

    // 2. integer division vs type casting
    int num1 = 8;
    int num2 = 3;

    std::cout << "--- 2. division and type casting ---\n";
    std::cout << "integer division 8 / 3: " << (num1 / num2) << "\n";
    std::cout << "c-style cast (double)8 / 3: " << ((double)num1 / num2) << "\n";
    std::cout << "modern static_cast: " << (static_cast<double>(num1) / num2) << "\n";
    std::cout << "float literal 8.0 / 3: " << (8.0 / 3) << "\n\n";

    // 3. formatted output using iomanip
    double purchase_amount = 150.0;
    double tax_rate = 0.10;
    double tax = purchase_amount * tax_rate;

    std::cout << "--- 3. stream formatting (<iomanip>) ---\n";
    std::cout << std::fixed << std::setprecision(2);
    std::cout << "purchase amount: $" << purchase_amount << "\n";
    std::cout << "calculated tax (10%): $" << tax << "\n";
    std::cout << "total amount: $" << (purchase_amount + tax) << "\n\n";

    // 4. math functions (<cmath>)
    double radius = 4.0;
    double area = 3.14159 * std::pow(radius, 2);
    std::cout << "--- 4. cmath library usage ---\n";
    std::cout << "circle radius: " << radius << "\n";
    std::cout << "circle area: " << area << "\n";

    return 0;
}
