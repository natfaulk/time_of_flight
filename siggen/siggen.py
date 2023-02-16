import matplotlib.pyplot as plt
import numpy as np
import math

# in samples per second
SAMPLE_RATE = 1e6

# time in seconds
# freq in hz
# amplitude is ??
# phase offset is in radians
# returns a sine wave with no DC component
def generateSignal(time, freq, amplitude, phaseoffset = 0):
  numberOfSamples = math.ceil(SAMPLE_RATE * time)

  return np.array([amplitude * math.sin((i / SAMPLE_RATE) * 2 * math.pi * freq + phaseoffset) for i in range(numberOfSamples)])

# amplitude is ??
def generateNoise(time, amplitude):
  numberOfSamples = math.ceil(SAMPLE_RATE * time)
  
  return np.random.normal(0, amplitude, numberOfSamples)

# for now -1 to +1 is the maximum range and anything above that is clipped
# quantise to a signed integer
def quantise(_samples, _bits):
  intmax = (2 ** (_bits - 1)) - 1
  intmin = -(2 ** (_bits - 1))

  out = []

  # to get from +1 to xbit max we need to do intx max * samples
  for s in _samples:
    val = round(s * intmax)
    val = max(val, intmin)
    val = min(val, intmax)
    out.append(val)
  
  return np.array(out)

def saveToFile(_samples, _bits):
  filename = f'rawbytes_{_bits}bit.bin'
  
  # could pack much more efficiently...
  outformat = np.uint8
  if _bits > 8:
    outformat = np.uint16
  elif _bits > 16:
    outformat = np.uint32

  with open(filename, 'wb') as binary_file:
    binary_file.write(_samples.astype(outformat))

if __name__ == '__main__':
  LENGTH = 0.01
  BITS = 8

  signal1 = generateSignal(LENGTH, 30e3, 0.5, math.pi / 4)
  signal2 = generateSignal(LENGTH, 26e3, 0.2)
  noise = generateNoise(LENGTH, 0.1)

  samples = signal1 + signal2 + noise
  samples8bit = quantise(samples, BITS)

  saveToFile(samples8bit, BITS)

  xpoints = [i / SAMPLE_RATE for i in range(len(samples))]

  plt.plot(xpoints, samples8bit)
  plt.show()

  print(samples8bit[:100])



