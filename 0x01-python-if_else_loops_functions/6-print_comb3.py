#!/usr/bin/python3
for i in range(10):
    for j in range(i,10):
        print(f'{i}{j}',end=',' if i != 9 or j != 9 else '\n')
