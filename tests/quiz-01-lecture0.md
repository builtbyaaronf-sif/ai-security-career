# Quiz 1: Lecture 0 (29 Oct 2026)

**Score: 5.0 / 10.** Closed book.

| # | Topic | Mark |
|---|---|---|
| 1 | Return value | 0 |
| 2 | int vs float | 1 |
| 3 | String times number | 0.5 |
| 4 | f string syntax | 1 |
| 5 | print("name") vs print(name) | 1 |
| 6 | Parameter vs argument | 0 |
| 7 | What input() returns | 0 |
| 8 | Operator precedence | 0.5 |
| 9 | str.replace | 1 |
| 10 | MemoryError and unbounded input | 0 |

## Correct answers
1. A function hands a value back to the code that called it. `input()` returns the typed text.
2. int is a whole number (7). float has a decimal point (7.5).
3. `"5" * 3` is `"555"`. `int("5") * 3` is `15`.
4. No space between `f` and the quote: `f"Hello, {name}"`.
5. `print("name")` prints the word name. `print(name)` prints the value stored in the variable.
6. Parameter: the name in the `def` line. Argument: the value passed in the call.
7. input() returns what the user typed, as a string.
8. `**` is done before `*`: 2 ** 2 = 4, then 3 * 4 = 12.
9. Replaces every space with `...` and returns a new string. The original is unchanged.
10. `"84" * (300000000 ** 2)` asks for 90 quadrillion repeats and runs out of memory. User input controlling the amount of work is a denial of service weakness (unbounded consumption).
