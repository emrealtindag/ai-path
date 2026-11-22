#include <iostream>
#include <iomanip>
#include <cmath>

using namespace std;

int main() {
    // 1. escape sequences
    cout << "--- 1. escape characters ---\n";
    cout << "Three\nTwo\nOne\n";
    cout << "\"Emre\"\t\'Altindag\'\n\n";

    // 2. arithmetic and division precision
    cout << "--- 2. division precision ---\n";
    cout << "8 / 3: " << 8 / 3 << "\n";
    cout << "(float)8 / 3: " << (float)8 / 3 << "\n";
    cout << "8.0 / 3: " << 8.0 / 3 << "\n";
    cout << "8.0 / 3.0: " << 8.0 / 3.0 << "\n";
    cout << "static_cast<int>(1.125): " << static_cast<int>(1.125) << "\n\n";

    // 3. time conversion (seconds to minutes and remaining seconds)
    cout << "--- 3. seconds conversion ---\n";
    int total_seconds = 135;
    int minutes = total_seconds / 60;
    int remaining_seconds = total_seconds % 60;
    cout << total_seconds << " seconds = " << minutes << " minutes and " << remaining_seconds << " seconds\n\n";

    // 4. complex formula evaluation with cube root
    cout << "--- 4. complex math formula ---\n";
    double x = 4.0;
    double y = x + (sqrt(x + 4.0) / (pow(x, 2) + pow(x + 2.0, 1.0 / 3.0)));
    cout << "for x = " << x << ", y = " << y << "\n\n";

    // 5. prefix vs postfix operator tracing
    cout << "--- 5. prefix vs postfix ---\n";
    int i = 1;
    int j = ++i;
    cout << "j = ++i -> i: " << i << ", j: " << j << "\n";

    int a = 1;
    int b = a++;
    cout << "b = a++ -> a: " << a << ", b: " << b << "\n\n";

    // 6. triangle angles from 3 points via law of cosines
    cout << "--- 6. triangle geometry (law of cosines) ---\n";
    double x1 = 1.0, y1 = 1.0;
    double x2 = 4.0, y2 = 1.0;
    double x3 = 1.0, y3 = 5.0;

    double side_a = sqrt(pow(x3 - x2, 2) + pow(y3 - y2, 2));
    double side_b = sqrt(pow(x3 - x1, 2) + pow(y3 - y1, 2));
    double side_c = sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2));

    double cos_A = (pow(side_b, 2) + pow(side_c, 2) - pow(side_a, 2)) / (2 * side_b * side_c);
    double cos_B = (pow(side_a, 2) + pow(side_c, 2) - pow(side_b, 2)) / (2 * side_a * side_c);
    double cos_C = (pow(side_a, 2) + pow(side_b, 2) - pow(side_c, 2)) / (2 * side_a * side_b);

    const double PI = acos(-1.0);
    double deg_A = acos(cos_A) * (180.0 / PI);
    double deg_B = acos(cos_B) * (180.0 / PI);
    double deg_C = acos(cos_C) * (180.0 / PI);

    cout << fixed << setprecision(2);
    cout << "sides: a = " << side_a << ", b = " << side_b << ", c = " << side_c << "\n";
    cout << "angles: A = " << deg_A << " deg, B = " << deg_B << " deg, C = " << deg_C << " deg\n";

    return 0;
}
