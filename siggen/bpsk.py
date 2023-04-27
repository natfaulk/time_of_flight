import numpy as np
import math

from utils.constants import SAMPLE_RATE
from .siggen import generateSignal


def encodeBits(bits, frequency, codeToCarrierRatio, initialphaseoffset = 0):
  t1Cycle = 1 / frequency
  t1Bit = t1Cycle * codeToCarrierRatio
  
  samples = np.array([])
  for bit in bits:
    phaseoffset = initialphaseoffset + bit * math.pi
    newsamples = generateSignal(t1Bit, frequency, 1, phaseoffset)
    samples = np.concatenate((samples, newsamples))

  return samples
    
