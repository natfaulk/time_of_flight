class Log:
  log = {}

  def add(name, value):
    if name in Log.log:
      Log.log[name].append(value)
    else:
      Log.log[name] = [value]
  
  def get(name):
    return Log.log[name]
