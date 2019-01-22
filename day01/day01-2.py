import numpy as np

delta_freqs = np.genfromtxt('input.csv')

freqs = [0]
i = 0
duplicate_found = False
while duplicate_found == False:
  curr_freq = freqs[-1] + delta_freqs[i]
  if curr_freq in freqs:
    duplicate_found = True
    duplicate_freq = curr_freq
  freqs.append(curr_freq)
  i += 1
  if i == len(delta_freqs):
    i = 0
    print('frequency change beginning again')
    print('freq list length: '+str(len(freqs)))

print(duplicate_freq)
