import matplotlib.pyplot as plt
from .nco import NCO
from .phaseDetector import PhaseDetector
from utils.constants import SAMPLE_RATE
from utils.log import Log
from utils.utilities import wrapAngle
import math

AVERAGE_FACTOR = 0.0001
KP = 200


class PLL:
  def __init__(self, freq):
    self.freq = freq
    self.nco = NCO(freq)
    self.pd = PhaseDetector(AVERAGE_FACTOR)
    self.adjust_phase = 0
  
  def tick(self, sample):
    self.nco.tick()
    ncoSample = self.nco.getOutput()

    diff = self.pd.calculate(ncoSample, sample)

    adjust = diff * KP
    self.adjust_phase = adjust
    # self.adjust_phase = wrapAngle(self.adjust_phase)

    self.nco.setPhaseOffset(self.adjust_phase)
    
    Log.add('input', sample)
    # Log.add('ncof', self.freq + self.adjust_f)
    Log.add('adjust_phase', self.adjust_phase)
    Log.add('output', ncoSample)
    Log.add('output90', self.nco.getOutput90())

  def getPhaseoffset(self):
    return self.adjust_phase
    


# def run():


#   nco = NCO(30e3)

#   samples = []

#   for i in range(1000):
#     samples.append(nco.getOutput())

#     nco.tick()

#   xpoints = [i / SAMPLE_RATE for i in range(len(samples))]

#   plt.plot(xpoints, samples)
#   plt.show()


