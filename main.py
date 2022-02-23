import matplotlib.pyplot as plt
import numpy as np
import math

# 100 linearly spaced numbers
x = np.linspace(-np.pi/4,np.pi/4,200)
y = np.zeros(len(x))

# the function, which is y = sin(x) here
builtin = np.sin(4*x)**2


number = int(input("Enter the number of elements in Taylor series: "))
argument = float(input("Enter the argument for the function, to compare with built-in.\n"
                       "The value must be in degrees.\nYour argument: "))
# My own sin(4*x)**2 using Taylor series
# multiplier = 4
# starting_y = (1/2) - math.cos(8*a)/2
# first_d = multiplier*math.sin(8*a)
# y += starting_y + first_d*x
a = 0
arg_radians = (math.pi / 180) * argument
result = 0
passed1 = False
passed2 = False
passed3 = False

multiplier = 4
# setting the axes at the centre
fig = plt.figure()
# plt.title("Function comparison")
ax = fig.add_subplot(1,1,1)
fig, ax = plt.subplots()
ax.set_ylim([-5,5])

# y = y + (1/2) - math.cos(8*0)/2 + 4*math.sin(8*0)*x + ((32*math.cos(8*0))*x**2)/2 + (-32*8*math.sin(8*0) * x**3)/6 + (-32*8*8*math.cos(0)*x**4)/24
for n in range(1,number):
    if n % 2 == 0:
        np.add(y, (multiplier*math.cos(8*a)*x**n)/math.factorial(n), out=y, casting="unsafe")
        result += (multiplier*math.cos(8*a)*arg_radians**n)/math.factorial(n)
        multiplier *= (-1)
    else:
        # Means sinus.
        np.add(y, (multiplier*math.sin(8*a)*x**n)/math.factorial(n), out=y, casting="unsafe")
        result += (multiplier*math.sin(8*a)*arg_radians**n)/math.factorial(n)

    multiplier *= 8

    if not passed1 and abs(result - math.sin(4 * arg_radians) ** 2) < 0.1:
        print(f"Accuracy is < 0.1 on n = {n}")
        ax.plot(x, y, label="Accuracy < 0.1", lw=4)
        passed1 = True
    elif not passed2 and abs(result - math.sin(4 * arg_radians) ** 2) < 0.001:
        print(f"Accuracy is < 0.001 on n = {n}")
        ax.plot(x, y, label="Accuracy < 0.001", lw=4)
        passed2 = True
    elif not passed3 and abs(result - math.sin(4 * arg_radians) ** 2) < 10**(-6):
        print(f"Accuracy is < 0.1 on n = {n}")
        ax.plot(x, y, label="Accuracy < 0.000001", lw=4)
        passed3 = True

print("My -  ", result)
print("Built-in - ", math.sin(4*arg_radians)**2)
print("difference: ", abs(result-math.sin(4*arg_radians)**2))



# plot the function
ax.plot(x,y,color="r", label='Taylor sin(4*x )^2', lw=3)
ax.plot(np.linspace(-np.pi/4,np.pi/4,200), np.sin(4*x)**2, color='b',  label='sin(4*x)^2 builtin')
ax.legend()

# show the plot
plt.show()