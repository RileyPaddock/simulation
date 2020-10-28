import math 
import matplotlib.pyplot as plt
from euler_estimator import EulerEstimator
class BiologicalNeuron:
    def __init__(self, stimulus = lambda t: 0):
        self.s_t = stimulus
        self.h_0 = 0.07 * (math.e**3 + 1)/((0.07 * (math.e**3 + 1))+1)
        self.n_0 = 1/(1.25*(math.e-1)+1)
        self.m_0 = 2.5/(2.5+4*(math.e**2.5 - 1))
        self.C = 1

    def an(self, t, x):
        return 0.01*(10-x[0])/(math.exp(0.1*(10-x[0]))-1)

    def Bn(self, t, x):
        return 0.125*math.exp(-x[0]/80)

    def am(self, t, x):
        return 0.1*(25-x[0])/(math.exp(0.1*(25-x[0]))-1)

    def Bm(self, t, x):
        return 4*math.exp(-x[0]/18)

    def ah(self, t, x):
        return 0.07 * math.exp(-x[0]/20)

    def Bh(self, t, x):
        return 1/(math.exp(0.1*(30-x[0]))+1)

    def dn_dt(self, t, x):
        return self.an(t, x)*(1 - x[1]) - self.Bn(t, x)*x[1]

    def dm_dt(self, t, x):
        return self.am(t, x)*(1 - x[2]) - self.Bm(t, x)*x[2]

    def dh_dt(self, t, x):
        return self.ah(t, x)*(1 - x[3]) - self.Bh(t, x)*x[3]
    def INa(self, t, x):
        return self.gna(t, x)*(x[0]-115)

    def gna(self, t, x):
        return 120 * x[2]**3 * x[3]

    def Ik(self, t, x):
        return self.gk(t, x)*(x[0]+12)

    def gk(self, t, x):
        return 36 * x[1]**4

    def IL(self, t, x):
        return self.gl(t, x)*(x[0]-10.6)

    def gl(self, t, x):
        return 0.3

    def dV(self, t, x):
        return (self.s_t(t) - self.INa(t, x) - self.Ik(t, x) - self.IL(t, x))

    def plot_activity(self):
        estimator = EulerEstimator(derivatives = [self.dV, self.dn_dt, self.dm_dt, self.dh_dt],
                point = (0, (0, self.n_0, self.m_0, self.h_0)))
        plt.plot([n/2 for n in range(160)], [self.s_t(n/2) for n in range(160)])

        estimator.plot([0, 80], step_size=0.02,filename="hodgen_huxley.png")