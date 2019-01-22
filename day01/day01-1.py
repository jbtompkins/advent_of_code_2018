import numpy as np

freqs = np.genfromtxt('input.csv')

end_freq = np.sum(freqs)
print(end_freq)
