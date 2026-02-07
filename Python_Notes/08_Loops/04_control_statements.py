# Break Statement
'''Break statement immediately stops the loop and comes out of it.'''

for i in range(10):
    if(i == 5):
        break
    print("5 x", i, "=", 5*i)
'''Output: 
5 x 0 = 0
5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
5 x 4 = 20
As soon as i==5, the loop terminates'''

# Continue Statement
'''Continue statement skips the current iteration and moves to the next loop cycle.'''

for i in range(1, 6):
    if i == 3:
        continue
    print(i)
'''Output:
1
2
4
5
here, 3 is skipped, but the loop continues.'''

# NOTE:-
''' The main difference between break and continue statement is that, the break statement exits the loop whereas
the continue statement exits the particular iteration and moves on to next iteration.'''

# Pass Statement
'''pass does nothing.
It’s used when Python expects a statement syntactically, but you don’t want to write any code yet.

Why do we need pass?
Python does not allow empty blocks.

Used when:
- Writing code structure first
- Implementing later
- Creating empty functions/classes'''

i = 4
if i>0:
    pass 
print("HELLO")  # HELLO

