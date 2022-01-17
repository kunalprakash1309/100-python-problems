# Question
# Write a function to compute 5/0 and use try/except to catch the exceptions.

from logging import exception
from tkinter import EXCEPTION


try:
    5/0
except Exception as e:
    print(e)