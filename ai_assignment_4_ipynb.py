# -*- coding: utf-8 -*-
"""Ai assignment 4 ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/12o03sWiTf-TwzWAlHNiGICUT6YJ4wN9H
"""

E = {0, 1, 2, 3, 4, 5}
N = {2, 4, 6, 8}

Union = E | N
print("The Union of E and N is :",Union)

Intersection = E & N
print("The Intersection of E and N is :",Intersection)

Difference = N - E
print ("The Difference of E and N is :",Difference)

Symmetric_difference = E ^ N
print("The Symmetric Difference of E and N is :",Symmetric_difference)