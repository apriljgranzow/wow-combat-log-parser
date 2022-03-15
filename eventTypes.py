import re

def getEventType(line):
  return line.split('  ')[1].split(',')[0]

def getAllUniqueEventTypes(lines):
  events = set(map(getEventType, lines))
  return events

def getArgs(line):
  return line.split('  ')[1].split(',')[1:]

def splitEvent(line):
  pattern = re.compile()

def peakLines(lines, numLines=10):
  return lines[:numLines]

with open("/Users/aprilgranzow/wow-combat-log-parser/logFiles/WoWCombatLog-031322_160329.txt") as file:
  combatLog = file.read()
  lines = combatLog.splitlines()
  print(map(getArgs, peakLines(lines)))