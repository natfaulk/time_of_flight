class PhaseDetector:
  def __init__(self, alpha):
    self.value = 0
    self.alpha = alpha

  def calculate(self, a, b):
    current = a * b
    history = (1 - self.alpha) * self.value

    self.value = history + current * self.alpha

    return self.value
