class BiologicalNeuralNetwork:
    def __init__(self, neurons, synapses):
        self.neurons = neurons
        self.synapses = synapses

    def get_derivatives(self):
        derivatives = []
        for i in range(len(self.neurons)):
            synaps_senders = [y for x,y in self.synapses if x == i]

            if i in [y for x,y in self.synapses]:
                derivatives.append(lambda t, x, i=i, n=self.neurons[i]: n.dV(
                    t, x[i*4:(i+1)*4]) + sum(x[p*4] for p in synaps_senders)/n.C)
            else:
                derivatives.append((lambda t, x, i=i, n=self.neurons[i]: n.dV(t, x[i*4:(i+1)*4])))

            derivatives.append(lambda t, x, i=i, n=self.neurons[i]: n.dn_dt(t, x[i*4:(i+1)*4]))
            derivatives.append(lambda t, x, i=i, n=self.neurons[i]: n.dm_dt(t, x[i*4:(i+1)*4]))
            derivatives.append(lambda t, x, i=i, n=self.neurons[i]: n.dh_dt(t, x[i*4:(i+1)*4]))
            
        return derivatives

    def get_starting_point(self):
        point = (0,[])
        for neuron in self.neurons:
            point[1].append(0)
            point[1].append(neuron.n_0)
            point[1].append(neuron.m_0)
            point[1].append(neuron.h_0)
        return point
