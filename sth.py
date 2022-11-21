import math
import numpy as np
import pandas as pd

def make_table(c, A, b):
    xb = [[x] + eq for eq, x in zip(A, b)]
    z =  c
    return [z] + xb


def straight(table):
    z = []
    for i in range(len(table)):
        z.append(table[i][0])
    # print(z)

    return all(x >= 0 for x in z)

# def plus_elem(table):
#     z = []
#     column = next(i for i,v in enumerate(z) if v < 0)
#     print(column)
#     return any(x > 0 for x in column)

def dual(table):
    z = table[0]
    # print(z)
    return all(x > 0 for x in z[:-1])


def get_position(table):
    z = table[0]
    column = next(i for i,v in enumerate(z) if v < 0 and i != 0)
    restrictions = []
    for i in range(len(table)):
        restrictions.append(table[i][column])
    row = next(i for i, v in enumerate(restrictions) if v > 0)

    return row, column


def step(table, pivot_position):
    new_table = [[] for eq in table]
    print(pivot_position)
    
    i, j = pivot_position
    print(table[i][j])
    print(table[0][j])
    pivot_value = table[i][j]
    new_table[i] = np.array(table[i]) / pivot_value
    
    for eq_i, eq in enumerate(table):
        if eq_i != i:
            multiplier = np.array(new_table[i]) * table[eq_i][j]
            new_table[eq_i] = np.array(table[eq_i]) - multiplier
   
    return new_table

def is_basic(column):
    return sum(column) == 1 and len([c for c in column if c == 0]) == len(column) - 1



def simplex(c, A, b):
    table = make_table(c, A, b)
    print(pd.DataFrame(table))
    i = 0
    while straight(table):
        if dual(table):
            break
        print(straight(table))
        pivot_position = get_position(table)
        table = step(table, pivot_position)
        print(pd.DataFrame(table))
        if i > 5:
            break
        i += 1
    if not straight(table):
        print("нет решения")
    return table


if __name__ == '__main__':


    c = [-26, 0, -1, -4, 1, -7, 0, 0, 0]
    A = [[2, 1, 1, -1, 1, 1, 0, 0], [-4, -2, 1, 1, 3, 0, 1, 0], [2, 2, 2, -1, 3, 0, 0, 1]]
    b = [5, 9, 12]

    
    k = make_table(c, A, b)
    print(pd.DataFrame(k))
    pivot_position = get_position(k)
    
    table2 = step(k, pivot_position)
    print(pd.DataFrame(table2))
    pos = get_position(table2)
    table3 = step(table2, pos)
    print(pd.DataFrame(table3))
    pos1 = get_position(table3)
    table4 = step(table3, pos1)
    print(pd.DataFrame(table4))
    pos2 = get_position(table4)
    table5 = step(table4, pos2)
    print(pd.DataFrame(table5))
