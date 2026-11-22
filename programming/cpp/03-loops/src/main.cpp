#include <iostream>
#include <iomanip>

int main() {
    // 1. for loop execution and trace
    std::cout << "--- 1. for loop trace ---\n";
    int i;
    for (i = 1; i <= 3; i++) {
        std::cout << "hello " << i << "\n";
    }
    std::cout << "value of i after loop exit: " << i << "\n\n";

    // 2. while loop: sum and mean calculation
    std::cout << "--- 2. while loop mean calculation ---\n";
    int counter = 0;
    int x = 1;
    int sum = 0;
    while (x <= 10) {
        sum += x;
        x++;
        counter++;
    }
    double mean = static_cast<double>(sum) / counter;
    std::cout << "sum: " << sum << ", count: " << counter << ", mean: " << mean << "\n\n";

    // 3. gcd (greatest common divisor) calculation
    std::cout << "--- 3. greatest common divisor (gcd) ---\n";
    int num1 = 24, num2 = 36;
    int gcd = 1;
    int f = 2;
    while (f <= num1 && f <= num2) {
        if (num1 % f == 0 && num2 % f == 0) {
            gcd = f;
        }
        f++;
    }
    std::cout << "gcd of " << num1 << " and " << num2 << " is: " << gcd << "\n\n";

    // 4. power computation via for loop (no cmath pow)
    std::cout << "--- 4. base^power calculation ---\n";
    int base = 2, power = 8;
    int product = 1;
    for (int p = 1; p <= power; p++) {
        product *= base;
    }
    std::cout << base << "^" << power << " = " << product << "\n\n";

    // 5. harmonic and alternating series
    std::cout << "--- 5. series summation ---\n";
    int n = 6;
    double harmonic_sum = 0.0;
    double alt_sum = 0.0;
    int sign = 1;
    for (int k = 1; k <= n; k++) {
        harmonic_sum += (1.0 / k);
        alt_sum += (1.0 / k) * sign;
        sign = -sign;
    }
    std::cout << "harmonic sum (1..6): " << harmonic_sum << "\n";
    std::cout << "alternating sum (1 - 1/2 + 1/3 - ...): " << alt_sum << "\n\n";

    // 6. prime number checker
    std::cout << "--- 6. prime number check ---\n";
    int test_num = 29;
    bool is_prime = true;
    for (int d = 2; d < test_num; d++) {
        if (test_num % d == 0) {
            is_prime = false;
            break;
        }
    }
    std::cout << test_num << " is prime: " << (is_prime ? "true" : "false") << "\n\n";

    // 7. first 50 prime numbers (10 per line)
    std::cout << "--- 7. first 50 prime numbers ---\n";
    const int target_primes = 50;
    const int per_line = 10;
    int prime_count = 0;
    int candidate = 2;

    while (prime_count < target_primes) {
        bool prime_flag = true;
        for (int div = 2; div <= candidate / 2; div++) {
            if (candidate % div == 0) {
                prime_flag = false;
                break;
            }
        }
        if (prime_flag) {
            prime_count++;
            std::cout << candidate << "\t";
            if (prime_count % per_line == 0) {
                std::cout << "\n";
            }
        }
        candidate++;
    }

    return 0;
}
