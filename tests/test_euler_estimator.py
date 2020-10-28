from euler_estimator import EulerEstimator

euler = EulerEstimator(
                derivatives = [
                    (lambda x: 0.6*x[0] - 0.05*x[0]*x[1]),
                    (lambda x: -0.9*x[1] + 0.02*x[0]*x[1])
                    ],
                point = (0,(100,10))
            )
euler.plot([0,100], step_size = 0.001, filename = 'plot.png')