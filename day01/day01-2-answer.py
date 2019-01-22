# https://www.reddit.com/r/adventofcode/comments/a20646/2018_day_1_solutions/
# https://gist.github.com/CameronAavik/2cd37a899290da1e8ad43c6d51a28796
# Work in progress...

import numpy as np

freq_changes = np.genfromtxt('input.csv')
freq_shift = np.sum(freq_changes)

freqs = [0]
for i in range(len(freq_changes)):
  freqs.append(freqs[-1] + freq_changes[i])

duplicate_find = np.array(freqs) % freq_shift
print(freqs)
idx, = np.where(duplicate_find == 0)
for i in range(len(idx)):
  print(freqs[idx[i]])
