import matplotlib.pyplot as plt
import numpy as np
import math


def taylor_series(n_value: int, argument: float) -> None:
    # 100 linearly spaced numbers
    x = np.linspace(-np.pi/4,np.pi/4,200)
    y = np.zeros(len(x))

    a = 0
    arg_radians = (math.pi / 180) * argument
    result = 0
    passed1 = False
    passed2 = False
    passed3 = False

    # setting up multiplier (it will change as we differentiate bc of (8x) in sin and cos.)
    multiplier = 4

    #setting up the plot
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    ax.set_ylim([-5,5])

    # creating row and checking for accuracy as needed for task.
    for n in range(1, n_value):
        if n % 2 == 0:
            np.add(y, (multiplier*math.cos(8*a)*x**n)/math.factorial(n), out=y, casting="unsafe")
            result += (multiplier*math.cos(8*a)*arg_radians**n)/math.factorial(n)
            # if its even n, means the derriviation will change the sign.
            multiplier *= (-1)
        else:
            # if odd - than its sinus. Multiplier is responsible for the sign.
            # np.add with flag "unsafe" addition allows us to procceed to work with larger n's.
            np.add(y, (multiplier*math.sin(8*a)*x**n)/math.factorial(n), out=y, casting="unsafe")
            result += (multiplier*math.sin(8*a)*arg_radians**n)/math.factorial(n)
        multiplier *= 8

        # check for accuraccies as needed for task.
        if not passed1 and abs(result - math.sin(4 * arg_radians) ** 2) < 0.1:
            print(f"Accuracy is < 0.1 on n = {n}")
            ax.plot(x, y, label="Accuracy < 0.1", lw=4)
            passed1 = True
        elif not passed2 and abs(result - math.sin(4 * arg_radians) ** 2) < 0.001:
            print(f"Accuracy is < 0.001 on n = {n}")
            ax.plot(x, y, label="Accuracy < 0.001", lw=4)
            passed2 = True
        elif not passed3 and abs(result - math.sin(4 * arg_radians) ** 2) < 10**(-6):
            print(f"Accuracy is < 0.000001 on n = {n}")
            ax.plot(x, y, label="Accuracy < 0.000001", lw=4)
            passed3 = True

    # output differences in result in the end.
    print(f"My sin(4*x)**2 for x = {argument}°: ", result)
    print(f"Built-in sin(4*x)**2 for x  = {argument}°: ", math.sin(4*arg_radians)**2)
    print("difference: ", abs(result-math.sin(4*arg_radians)**2))



    # plot the functions
    ax.plot(x,y,color="r", label='Taylor sin(4*x )^2', lw=3)
    ax.plot(np.linspace(-np.pi/4,np.pi/4,200), np.sin(4*x)**2, color='b',  label='sin(4*x)^2 builtin')
    ax.legend()

    # show the plot
    plt.show()


if __name__ == "__main__":
    n_value = int(input("Enter the number of elements in Taylor series (>1): "))
    argument = float(input("Enter the argument for the function, to compare with built-in.\n"
                           "The value must be in degrees.\nYour argument: "))
    taylor_series(n_value, argument)