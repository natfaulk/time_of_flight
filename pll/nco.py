from utils.constants import SAMPLE_RATE
import math

class NCO:
  def __init__(self, freq):
    self.sampletime = 0
    # self.phase = 0
    self.freq = freq
    self.phaseoffset = 0

    self.updateOutput()

  def updateOutput(self):
    self.output = math.sin((self.sampletime / SAMPLE_RATE) * 2 * math.pi * self.freq + self.phaseoffset)
    self.output90 = math.sin((self.sampletime / SAMPLE_RATE) * 2 * math.pi * self.freq + self.phaseoffset - math.pi / 2)
    
    
    # self.phase += 2 * math.pi * self.freq / SAMPLE_RATE
    # self.output = math.sin(self.phase)
    # self.output90 = math.sin(self.phase - math.pi / 2)

  def tick(self):
    self.sampletime += 1
    self.updateOutput()

  def getOutput(self):
    return self.output
  
  def getOutput90(self):
    return self.output90

  def setPhaseOffset(self, phaseoffset):
    self.phaseoffset = phaseoffset
  
