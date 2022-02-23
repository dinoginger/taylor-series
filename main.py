import matplotlib.pyplot as plt
import numpy as np
import math
plt.style.use('seaborn-poster')


# 100 linearly spaced numbers
x = np.linspace(-np.pi/4,np.pi/4,200)
y = np.zeros(len(x))

# the function, which is y = sin(x) here
builtin = np.sin(4*x)**2


number = int(input("Enter number of elements in Taylor series"))
# My own sin(4*x)**2 using Taylor series
# multiplier = 4
# starting_y = (1/2) - math.cos(8*a)/2
# first_d = multiplier*math.sin(8*a)
# y += starting_y + first_d*x


a = 0
multiplier = 4
# y = y + (1/2) - math.cos(8*0)/2 + 4*math.sin(8*0)*x + ((32*math.cos(8*0))*x**2)/2 + (-32*8*math.sin(8*0) * x**3)/6 + (-32*8*8*math.cos(0)*x**4)/24
for n in range(1,number):
    if n % 2 == 0:
        y += (multiplier*math.cos(8*0)*x**n)/math.factorial(n)
        multiplier *= (-1)
    else:
        # Means sinus.
        y += (multiplier*math.sin(8*a)*x**n)/math.factorial(n)

    multiplier *= 8


# setting the axes at the centre
fig = plt.figure()
# plt.title("Function comparison")
ax = fig.add_subplot(1,1,1)
ax.margins(x=0, y=1)
plt.grid()
plt.title('Taylor series sin(4*x)**2 and built-in sin(4*x)**2')
plt.xlabel('x')
plt.ylabel('y')

# plot the function
plt.plot(x,y,color="r", label='sin(4*x )^2')
plt.plot(np.linspace(-np.pi/4,np.pi/4,200), np.sin(4*x)**2, color='b',  label='sin(4*x)^2 builtin')
plt.legend()

# show the plot
plt.show()