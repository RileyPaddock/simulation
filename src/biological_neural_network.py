class BiologicalNeuralNetwork:
    def __init__(self, neurons, synapses):
        self.neurons = neurons
        self.synapses = synapses

    def get_derivatives(self):
        derivatives = {}
        for i in range(len(self.neurons)):
            neuron = self.neurons[i]
            synaps_senders = [x for x,y in self.synapses if y == i]
            derivatives['V'+str(i)]= (lambda t, x, i=i, n=neuron, ss = synaps_senders:n.dV()(t, list(x.values())[i*4:(i+1)*4]) + sum([list(x.values())[p*4] for p in ss if list(x.values())[p*4]>50])/n.C)
            derivatives['n'+str(i)]=(lambda t, x, i=i, n=neuron: n.dn_dt(t, list(x.values())[i*4:(i+1)*4]))
            derivatives['m'+str(i)]=(lambda t, x, i=i, n=neuron: n.dm_dt(t, list(x.values())[i*4:(i+1)*4]))
            derivatives['h'+str(i)]=(lambda t, x, i=i, n=neuron: n.dh_dt(t, list(x.values())[i*4:(i+1)*4]))
        return derivatives

    def get_starting_point(self):
        point = [0,{}]
        for neuron in self.neurons:
            point[1]['V'+str(self.neurons.index(neuron))] = 0
            point[1]['n'+str(self.neurons.index(neuron))] = neuron.n_0
            point[1]['m'+str(self.neurons.index(neuron))] = neuron.m_0
            point[1]['h'+str(self.neurons.index(neuron))] = neuron.h_0
        print(point[1])
        return point
