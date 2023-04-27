from pll.pll import PLL
import math
from siggen.siggen import *
import matplotlib.pyplot as plt
from utils.constants import SAMPLE_RATE
from statistics import mean
from pytest import approx
from utils.utilities import wrapAngle
import numpy as np

def pllWithInitialPhase(initialPhase):
  SETTLING_TIME = round(2e-3 * SAMPLE_RATE)

  # currently a rather large setpoint error
  PHASE_TOLERANCE = 0.2

  # it is expected that when phase locked the input and output phases are
  # 90 degrees apart
  EXPECTED_PHASE = initialPhase + math.pi / 2

  LENGTH = 1e-2
  FREQ = 1e4
  samples = generateSignal(LENGTH, FREQ, 1, initialPhase)

  pll = PLL(FREQ)

  phaseOffset = []

  for sample in samples:
    pll.tick(sample)
    phaseOffset.append(pll.getPhaseoffset())

  samplesToCheck = phaseOffset[SETTLING_TIME:]
  samplesToCheckMean = mean(samplesToCheck)

  # plt.plot(phaseOffset)
  # plt.show()

  # need to check the angle, and also plus 2 pi and minus 2 pi as it can pull in the opposite way sometimes
  check = approx(EXPECTED_PHASE, abs=PHASE_TOLERANCE) == samplesToCheckMean
  checkPlus = approx(EXPECTED_PHASE + math.pi * 2, abs=PHASE_TOLERANCE) == samplesToCheckMean
  checkMinus = approx(EXPECTED_PHASE - math.pi * 2, abs=PHASE_TOLERANCE) == samplesToCheckMean

  assert check or checkMinus or checkPlus

def test_PLL_clean_signal_zero_phase():
  pllWithInitialPhase(0)

def test_PLL_clean_signal_90_deg_phase():
  pllWithInitialPhase(math.pi / 2)

def test_PLL_clean_signal_180_deg_phase():
  pllWithInitialPhase(math.pi)

def test_PLL_clean_signal_minus_180_deg_phase():
  pllWithInitialPhase(-math.pi)

def test_PLL_clean_signal_minus_90_deg_phase():
  pllWithInitialPhase(-math.pi / 2)


def test_PLL_clean_signal_small_increments():
  for i in np.arange(-math.pi, math.pi + 0.01, 0.1):
    pllWithInitialPhase(i)



  
# if __name__ == '__main__':
#   test_PLL_clean_signal_zero_phase()

