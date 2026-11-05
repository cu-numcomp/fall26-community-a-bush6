from scipy import optimize

def f(x):
    return (x**3 - 1)

sol = optimize.root_scalar(f, bracket=[0, 3], method='brentq')
sol.root, sol.iterations, sol.function_calls



#root = 1.0
#iterations = 10
#function calls = 11



# Source: SciPy official documentation
# scipy.optimize.root_scalar Examples
# https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.root_scalar.html
