# Quiz 2: Lecture 1 + Lecture 0 review (2 Nov 2026)

**Score: 6.0 / 12.** Closed book.

| # | Topic | Mark |
|---|---|---|
| 1 | Return value (retake) | 0 |
| 2 | Parameter vs argument (retake) | 0.5 |
| 3 | What input() returns (retake) | 0.5 |
| 4 | String times number (retake) | 1 |
| 5 | = vs == | 1 |
| 6 | elif vs second if | 1 |
| 7 | % remainder | 0.5 |
| 8 | and / or truth values | 0 |
| 9 | Range check (and vs or) | 0.5 |
| 10 | Normalising input, security reason | 0.5 |
| 11 | __name__ guard | 0.5 |
| 12 | Access control with and / or | 0 |

## Correct answers
1. A value a function hands back to the code that called it. `convert("7:30")` returns 7.5.
2. `time` is the parameter (a placeholder in the def line). `"7:30"` is the argument (the value passed in).
3. It returns what the user typed, as a string (`str`).
4. `"7" * 3` is `777`. `int("7") * 3` is `21`.
5. `=` assigns a value. `==` compares two values and gives True or False.
6. First: `A`. Second: `A` then `B`.
7. `%` gives the remainder only. `7 % 2` is 1. `10 % 5` is 0.
8. `5 > 3 and 2 > 4` is False. `5 > 3 or 2 > 4` is True.
9. A. B is true for times OUTSIDE the range.
10. Normalising once means every comparison sees one canonical form. Attackers exploit gaps between what is checked and what is used (Admin vs admin, a trailing space).
11. It runs main() only when the file is run directly. `__name__` is "__main__" then. When imported it is the module name, so main() does not run.
12. `or` lets any logged in user in, or any admin. Admin access needs both: `logged_in and is_admin`. This is broken access control (OWASP A01).
