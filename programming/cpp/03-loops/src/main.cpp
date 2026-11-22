#include <iostream>

int main() {
    // 1. for loop execution and trace demonstration
    std::cout << "--- 1. for loop state trace ---\n";
    int i;
    for (i = 1; i <= 3; i++) {
        std::cout << "iteration pass: hello " << i << "\n";
    }
    std::cout << "value of loop variable i after termination: " << i << "\n\n";

    // 2. while loop accumulator (sum of numbers 1 to 5)
    std::cout << "--- 2. while loop accumulator ---\n";
    int count = 1;
    int total_sum = 0;
    while (count <= 5) {
        total_sum += count;
        count++;
    }
    std::cout << "sum of integers from 1 to 5: " << total_sum << "\n\n";

    // 3. do-while loop (guaranteed single pass)
    std::cout << "--- 3. do-while post-condition loop ---\n";
    int retry_count = 0;
    do {
        std::cout << "executing pass " << retry_count << " (evaluates condition after body)\n";
        retry_count++;
    } while (retry_count < 1);
    std::cout << "\n";

    // 4. break and continue control flow
    std::cout << "--- 4. break and continue demonstration ---\n";
    for (int k = 1; k <= 10; k++) {
        if (k == 4) {
            std::cout << "[skipping 4 via continue] ";
            continue;
        }
        if (k == 8) {
            std::cout << "\n[terminating at 8 via break]\n";
            break;
        }
        std::cout << k << " ";
    }
    std::cout << "\n\n";

    // 5. nested loops (2d coordinate grid)
    std::cout << "--- 5. nested loops (3x3 grid) ---\n";
    for (int row = 1; row <= 3; row++) {
        for (int col = 1; col <= 3; col++) {
            std::cout << "[" << row << "," << col << "] ";
        }
        std::cout << "\n";
    }

    return 0;
}
