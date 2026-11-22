# loops

iteration mechanics, loop invariants, state tracing, and flow control via while, do-while, and for statements in c++.

---

## iteration mechanics and loop types

loops execute a block of statements repeatedly as long as a terminating boolean condition remains true.

### 1. while loop (pre-condition check)

evaluates the condition before each iteration. if the condition is initially false, the loop body executes zero times:

```cpp
int count = 0;
while (count < 5) {
    std::cout << count << " ";
    count++;
}
```

### 2. do-while loop (post-condition check)

evaluates the condition after the body executes. guarantees at least one execution pass:

```cpp
int input = 0;
do {
    // executes at least once regardless of initial input state
    input++;
} while (input < 3);
```

### 3. for loop (counter-controlled iteration)

packages loop state initialization, condition evaluation, and state update into a single unified construct:

```cpp
for (initialization; condition; increment_decrement) {
    // loop body
}
```

---

## execution lifecycle and trace table

understanding the exact sequence of evaluation is critical for avoiding off-by-one errors:

```text
       ┌── 1. initialization (runs once at start)
       │         ┌── 2. condition check (before each pass)
       │         │         ┌── 4. update (after each pass)
       ▼         ▼         ▼
for (int i = 1; i <= 3; i++) {
    // 3. body execution
    std::cout << "hello " << i << "\n";
}
// 5. after loop exit: i has value 4
```

### step-by-step state trace table

| step | variable `i` | condition `i <= 3` | action / output | next `i` via `i++` |
| :--- | :--- | :--- | :--- | :--- |
| initial | `1` | `1 <= 3` (true) | prints `"hello 1"` | `1 + 1 = 2` |
| pass 2 | `2` | `2 <= 3` (true) | prints `"hello 2"` | `2 + 1 = 3` |
| pass 3 | `3` | `3 <= 3` (true) | prints `"hello 3"` | `3 + 1 = 4` |
| exit check | `4` | `4 <= 3` (false) | loop terminates | loop ends |

> [!NOTE]
> if `i` is declared outside the loop (`int i; for (i = 1; ...)`), its post-loop value is `4`, representing the state that caused the condition to fail.

---

## loop flow control: break and continue

- **`break`**: immediately terminates the enclosing loop and transfers execution to the statement following the loop.
- **`continue`**: immediately skips the remaining statements in the current iteration and jumps directly to the update step (`i++`).

```cpp
for (int i = 1; i <= 10; i++) {
    if (i == 4) continue; // skips printing 4
    if (i == 8) break;    // terminates loop when reaching 8
    std::cout << i << " ";
}
// outputs: 1 2 3 5 6 7
```

---

## nested loops and grid traversal

inner loops execute completely for each single iteration of the outer loop. commonly used in matrix indexing and geometric rasterization:

```cpp
for (int row = 1; row <= 3; row++) {
    for (int col = 1; col <= 3; col++) {
        std::cout << "(" << row << "," << col << ") ";
    }
    std::cout << "\n";
}
```

---

## common traps and best practices

- **off-by-one errors**: using `<=` instead of `<` when indexing zero-based collections causes out-of-bounds memory corruption.
- **unsigned underflow**: writing `for (unsigned int i = 10; i >= 0; i--)` results in an infinite loop because unsigned types can never be negative; `0 - 1` wraps around to `4,294,967,295`.
- **missing state update**: forgetting `count++` inside a `while` loop leaves the condition perpetually true, freezing execution in an infinite loop.
