#include <iostream>
#include <cmath>

int main() {
    // 1. if-else conditional validation
    double radius = 3.5;

    std::cout << "--- 1. if-else validation ---\n";
    if (radius < 0.0) {
        std::cout << "error: negative radius cannot produce a valid area.\n";
    } else if (radius == 0.0) {
        std::cout << "point circle: area is 0.0\n";
    } else {
        double area = 3.14159 * std::pow(radius, 2);
        std::cout << "radius: " << radius << " -> circle area: " << area << "\n\n";
    }

    // 2. logical operators and short-circuit evaluation
    int temperature = 24;
    bool is_raining = false;

    std::cout << "--- 2. boolean logical conditions ---\n";
    if (temperature >= 20 && temperature <= 30 && !is_raining) {
        std::cout << "flight conditions optimal for autonomous drone test.\n\n";
    } else {
        std::cout << "weather conditions outside safe flight parameters.\n\n";
    }

    // 3. multi-way branching via switch statement
    int day_index = 3; // wednesday

    std::cout << "--- 3. switch-case day lookup ---\n";
    switch (day_index) {
        case 1: std::cout << "day 1: monday\n"; break;
        case 2: std::cout << "day 2: tuesday\n"; break;
        case 3: std::cout << "day 3: wednesday\n"; break;
        case 4: std::cout << "day 4: thursday\n"; break;
        case 5: std::cout << "day 5: friday\n"; break;
        case 6: std::cout << "day 6: saturday\n"; break;
        case 7: std::cout << "day 7: sunday\n"; break;
        default: std::cout << "invalid day index: " << day_index << "\n"; break;
    }

    // 4. intentional fall-through grouping (weekdays vs weekend)
    std::cout << "--- 4. switch-case intentional fall-through ---\n";
    switch (day_index) {
        case 1:
        case 2:
        case 3:
        case 4:
        case 5:
            std::cout << "day " << day_index << " falls on a weekday.\n";
            break;
        case 6:
        case 7:
            std::cout << "day " << day_index << " falls on a weekend.\n";
            break;
        default:
            std::cout << "invalid day input.\n";
            break;
    }

    return 0;
}
