import Config
import ReadJournal
import MissionTracker
import json

def loadAllJournals():
  accept = []
  complete = []
  journals = ReadJournal.readAllJournals()
  for event in journals:
    if event['event'] == "MissionAccepted":
      accept.append(event)
    if event['event'] == "MissionCompleted":
      complete.append(event)

  for event in accept:
    MissionTracker.acceptMission(event)
  for event in complete:
    MissionTracker.completeMission(event)

def runMassacreHelper():
  loadAllJournals()
  data = []
  while 1:
    accept = []
    complete = []
    data = ReadJournal.fetchJournalUpdate(data)

    for event in data:
      if event['event'] == "MissionAccepted":
        accept.append(event)
      if event['event'] == "MissionCompleted":
        complete.append(event)
      if event['event'] == "MissionAbandoned":
        complete.append(event)
      if event['event'] == "MissionFailed":
        complete.append(event)

    for event in accept:
      MissionTracker.acceptMission(event)
    for event in complete:
      MissionTracker.completeMission(event)

    factions = MissionTracker.factionView()
    for faction in factions:
      s = f"{faction}: "
      for mission in factions[faction]:
        s += f"{mission['Targets']} "
      print(s)

def main():
  runMassacreHelper()
  return

if __name__ == "__main__":
  main()