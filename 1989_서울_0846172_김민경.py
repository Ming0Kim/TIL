# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1UbswGHkkEE72I7EHPaQdXjMmaIy9TWJK
"""

T = int(input())
for i in range(1, T+1):
  b = input()
  if b == b[::-1]:
    print("#%d"%i, 1)
  else:
    print("#%d"%i, 0)