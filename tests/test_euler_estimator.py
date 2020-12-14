import sys
sys.path.append('src')
from euler_estimator import EulerEstimator

euler = EulerEstimator(derivatives = {'a':(lambda x: x['a']/2)}, point = (1,{'a':4}))

print("\n Testing starting point")
assert euler.point == (1,{'a':4}), 'Incorrect Starting point'
print("     passed")
 
print("\n Testing starting derivative")
assert euler.calc_derivative_at_point() == {'a':2}, "Expected: "+str({'a':2})+", Got: "+str(euler.calc_derivative_at_point())
print("     passed")
 
print("\n Testing point after first step")
euler.step_forward(0.1)
assert euler.point == (1.1, {'a':4.2}), 'Incorrect point after first step'
print("     passed")
 
print("\n Testing derivative after first step")
assert euler.calc_derivative_at_point() == {'a':2.1},'Incorrect derivative after first step'
print("     passed")
 
print("\n Testing point after 2nd step")
euler.step_forward(-0.5)
assert (round(euler.point[0],3),{item:round(euler.point[1][item],3) for item in euler.point[1]})== (0.6, {'a':3.15}), 'Incorrect point after 2nd step'
print("     passed")
 
print("\n Testing go_to_input")
euler.go_to_input(3, step_size = 0.5)
assert (round(euler.point[0],3),{item:round(euler.point[1][item],3) for item in euler.point[1]}) == (3, {'a':9.229}), 'Incorrect final result'
print("     passed")
 


euler = EulerEstimator(
                derivatives = {
    'susceptible': (lambda x: -0.0003*x['susceptible']*x['infected']),
    'infected': (lambda x: 0.0003*x['susceptible']*x['infected'] - 0.02*x['infected']),
    'recovered': (lambda x: 0.02*x['infected'])
},
point = (0, {'susceptible': 1000, 'recovered': 0, 'infected': 1}))

euler.plot([0,100], step_size = 0.001, filename = 'test_plot.png')