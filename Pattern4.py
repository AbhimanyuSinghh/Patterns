"""
inverted triangle  pattern
        *
      * *
    * * *
  * * * *
* * * * *

"""

for i in range(6):
    for j in range(i, 6-i):
        print(" ", end= " ")
    for k in range(i):
        print('*', end=" ")
    print()