from random import random

def generate_color():
    return [random() for _ in range(3)]

def to_rgb(color):
    return [int(color[i]*255) for i in range(3)]

def from_rgb(color):
    return [color[i]/255 for i in range(3)]