import numpy
import matplotlib.pyplot as plt

x = numpy.array([-4, -5, 0, 3, 1])
y = numpy.array([-2, 5, 1, 0, 1])

print(numpy.corrcoef(x, y))