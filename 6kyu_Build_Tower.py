"""
Build Tower
Build a pyramid-shaped tower given a positive integer number of floors. A tower block is represented with "*" character.

For example, a tower with 3 floors looks like this:

[
  "  *  ",
  " *** ",
  "*****"
]
And a tower with 6 floors looks like this:

[
  "     *     ",
  "    ***    ",
  "   *****   ",
  "  *******  ",
  " ********* ",
  "***********"
]
"""

def tower_builder(n_floors):
    my_list = []
    num, space = 0, 1
    if n_floors > 0:
        while True:
            if num % 2 != 0:
                element = n_floors - space
                my_list.append(element*" " + num*"*" + element*" ")
                if len(my_list) == n_floors:
                    return my_list
                num = num + 1
                space = space + 1
            else:
                num = num + 1

    return my_list