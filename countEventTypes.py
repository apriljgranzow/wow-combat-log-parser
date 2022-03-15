import re

def getEventType(line):
  return line.split('  ')[1].split(',')[0]

def splitEvent(line):
  pattern = re.compile()

with open("/Users/aprilgranzow/wow-combat-log-parser/logFiles/WoWCombatLog-031322_160329.txt") as file:
  combatLog = file.read()
  lines = combatLog.splitlines()
  print(map(getEventType, lines[0:10]))