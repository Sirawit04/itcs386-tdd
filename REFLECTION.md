# Reflection (Part B)

## 1. Tests and production code
I wrote 9 tests in test_kitchen.py and kitchen.py has 40 non-blank lines of production code. The ratio is about 4.4 lines of production code per test, or roughly 0.2 tests per line. The whole suite (Part 0 and Part A) is 40 passing tests.

## 2. Longest red bar
The longest red bar was step A7, mixed addition (grams plus ounces). It needed Converter, Quantity.reduce and Sum.reduce to exist before the test could pass, so the bar stayed red across several small edits. The other long red was in A3, when test_kitchen.py failed at collection because a stray escape sequence from my terminal was pasted into the first line. That was a tooling mistake, not a design problem. I reset the two unpushed commits and redid A3, so it shows up twice in my history.

## 3. Fake It, Triangulate, Obvious Implementation
- Fake It: A1 (multiplication) and A4 returned a constant at first. Right choice, it made the bar green in seconds and showed the test could pass.
- Triangulate: A2 added a second example so the constant could no longer pass and I had to generalise (amount * multiplier). Right choice, I was not yet sure what the general form was.
- Obvious Implementation: the real __eq__ (A4), Sum.reduce (A6) and the rate conversion (A8) were typed directly. Right choice, they were one or two lines, and each went green first time.

## 4. Test list
Still open: __hash__. Defining __eq__ made Quantity unhashable, so it cannot be a dict key or set member. Nothing needs that yet, so I would not implement it next. I would implement conversion in the other direction (ounces from grams) next, because a real recipe needs both. I would delete __hash__ if the system stays as it is, since it is speculation.

## 5. Quantity.reduce
Probably not. On paper I would have put conversion only in Converter and kept Quantity a plain value. The tests pushed me to the "expression + reduce" shape, where Quantity and Sum both answer reduce(converter, unit). It works, and it let Sum and Quantity be used the same way, but I would not have drawn it myself. (This is my honest view after the exercise, not a measured result.)

## 6. Part 0 versus Part A
Writing tests after the code (Part 0) felt like checking homework: I read the code and picked inputs I already knew would pass, so the only surprises were the bugs in shipping.py. Writing tests first (Part A) felt slower at the start but safer later, because each step was small and I always knew what to do next. The tests that shaped the design were test_mixed_addition and test_sum_times. They forced Sum to exist and forced Quantity.reduce to take a converter. In Part 0 no test changed the design, because the design was already fixed.
