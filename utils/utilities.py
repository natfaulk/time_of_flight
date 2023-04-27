import math

def clamp(val, min, max):
  if val <= min:
    return min

  if val >= max:
    return max

  return val

# wrap an angle between - and + pi
def wrapAngle(val):
  return (val + math.pi) % (2 * math.pi) - math.pi
  