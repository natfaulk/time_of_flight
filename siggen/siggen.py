import numpy as np
import math

from utils.constants import SAMPLE_RATE

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
