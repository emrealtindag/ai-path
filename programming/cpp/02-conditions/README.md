# control flow and branching

conditional execution, boolean logic, relational operators, and multi-way branch selection via if-else and switch statements.

---

## conditional selection: if, else if, else

conditional statements evaluate a boolean expression and direct the program instruction pointer along one of several execution paths.

```cpp
if (condition1) {
    // executed when condition1 evaluates to true
} else if (condition2) {
    // executed when condition1 is false and condition2 is true
} else {
    // executed when all preceding conditions are false
}
```

### relational and logical operators

| operator | meaning | example |
| :--- | :--- | :--- |
| `==`, `!=` | equality, inequality | `radius == 0.0` |
| `<`, `<=`, `>`, `>=` | ordering comparisons | `score >= 50` |
| `&&` | logical and (both true) | `(x > 0) && (x < 100)` |
| `\|\|` | logical or (either true) | `(day == 6) \|\| (day == 7)` |
| `!` | logical not (inversion) | `!is_valid` |

### short-circuit evaluation

boolean expressions evaluate left-to-right and terminate as soon as the outcome is determined:
- in `expr1 && expr2`, if `expr1` is `false`, `expr2` is **never executed**.
- in `expr1 || expr2`, if `expr1` is `true`, `expr2` is **never executed**.

this property protects against null dereferences and division by zero:

```cpp
if (denominator != 0 && (numerator / denominator) > 1) {
    // safe: division only occurs if denominator is non-zero
}
```

---

## multi-way selection: switch statement

when branching on an integral value (`int`, `char`, `enum`), the `switch` statement provides structured multi-path execution. the compiler frequently optimizes switches into a **jump table** (`O(1)` dispatch) rather than evaluating sequential comparisons (`O(n)`).

```cpp
switch (integral_expression) {
    case constant1:
        // statement
        break;
    case constant2:
        // statement
        break;
    default:
        // executed when no case matches
        break;
}
```

### jump table vs sequential checks

```text
switch (day_index)
       │
       ▼
[jump table index: 1..7]
┌───┬───────────────┬─────────────────────────────┐
│ 1 │ -> address_1  │ cout << "monday"; break;    │
│ 2 │ -> address_2  │ cout << "tuesday"; break;   │
│ 6 │ -> address_6  │ cout << "weekend"; break;   │
│ * │ -> default    │ cout << "invalid"; break;   │
└───┴───────────────┴─────────────────────────────┘
```

### intentional fall-through pattern

if a `case` lacks a `break;` statement, execution continues unconditionally into the subsequent case. while accidental omission is a notorious bug, intentional grouping allows multiple matching values:

```cpp
switch (day_index) {
    case 1:
    case 2:
    case 3:
    case 4:
    case 5:
        std::cout << "weekday\n";
        break;
    case 6:
    case 7:
        std::cout << "weekend\n";
        break;
    default:
        std::cout << "invalid day index\n";
        break;
}
```

---

## common traps and best practices

- **assignment inside condition**: writing `if (x = 5)` assigns `5` to `x`, evaluates to `true`, and overwrites your data. enable compiler warnings (`-Wall`) to catch this immediately.
- **floating-point switch**: `switch` only accepts integral or enum types. floating-point values (`float`, `double`) cannot be used in a `switch`.
- **unhandled default**: always supply a `default:` label in production code to handle corrupted, out-of-bounds, or unexpected state transitions cleanly.
