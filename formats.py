from scipy.io.wavfile import read as scipy_read
import numpy as np
from wavebuilder import wavebuilder

class Sinusoid(wavebuilder): #periodic
    def __init__(self, time, sample_rate, frequency):
      self.time = time
      self.sample_rate = sample_rate
      self.frequency = frequency
      
      #building sinusoid, result is put into (time, position) 2darray called value
      times = np.linspace(0, time, sample_rate * time, endpoint=False)
      self.value = [times, np.sin(times * frequency * 2 * np.pi)] #converts frequency values into ascending rads before taking the sine
      
    def __str__(self):
      return 'Time: ' + str(self.time) + ', Sample Rate: ' + str(self.sample_rate) + ', Frequency(s): ' + str(self.frequency) + ', Normalized: ' + str(self.normalize)
    
    def __len__(self):
      return int(self.time * self.sample_rate)
    
class Recording(wavebuilder): #non-periodic
  def __init__(self, path, normalize):
    self.path = path
    data = scipy_read(path)
    self.sample_rate = data[0]
    self.time = len(data[1]) / data[0]
    self.normalize = normalize
    self.value = [np.linspace(0, self.time, len(data[1]), endpoint=False), np.array(data[1])]
    
    if normalize:
      self.value[1] = self.value[1] / max(self.value[1])
        
  def __str__(self):
    return 'Time: ' + str(self.time) + ', Sample Rate: ' + str(self.sample_rate) + ', Path: ' + str(self.path) + ', Normalized: ' + str(self.normalize)
  
  def __len__(self):
    return len(self.value[1])