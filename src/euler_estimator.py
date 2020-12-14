import matplotlib.pyplot as plt
class EulerEstimator:
    def __init__(self,derivatives,point):
        self.derivatives = derivatives
        self.point = point

    def calc_derivative_at_point(self):
        derivatives = {}
        for item in self.derivatives:
            derivatives[item]=(self.derivatives[item](self.point[0],self.point[1]))
        return derivatives

    def step_forward(self, step_size):
        derivatives = self.calc_derivative_at_point()
        new_points = {item:(self.point[1][item] + (step_size*derivatives[item])) for item in derivatives}
        self.point = (self.point[0]+step_size, new_points)
        
    def go_to_input(self, stop_x, step_size):
        while abs(self.point[0]) < abs(stop_x):
            if self.point[0] + step_size <= stop_x:
                self.step_forward(step_size)
            else:
                step_size = (stop_x - self.point[0])
                self.step_forward(step_size)
        return self.point

    

    def plot(self, interval, step_size, filename):
        x_data = [round(interval[0]+i*step_size, 10)
                  for i in range(int((interval[1]-interval[0])/step_size)+1)]
        given_index = x_data.index(self.point[0])
        given_point = self.point
        y_data = []
        for x in x_data[:given_index][::-1]:
            self.go_to_input(x, step_size)
            y_data.insert(0, [self.point[1][item] for item in self.point[1]])
        self.point = given_point
        for x in x_data[given_index:]:
            self.go_to_input(x, step_size)
            y_data.append([self.point[1][item] for item in self.point[1]])
        plt.style.use('bmh')
        for y_vals in zip(*y_data):
            plt.plot(x_data, y_vals, zorder=1)
        plt.legend([item for item in self.derivatives])
        plt.savefig(filename)