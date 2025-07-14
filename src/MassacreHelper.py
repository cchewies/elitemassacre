import Config
import ReadJournal
import MissionTracker
import json

def loadAllJournals():
  journals = ReadJournal.readAllJournals()
  for event in journals:
    if event['event'] == "MissionAccepted":
      MissionTracker.acceptMission(event)
    if event['event'] == "MissionCompleted":
      MissionTracker.completeMission(event)
    if event['event'] == "MissionAbandoned":
      MissionTracker.completeMission(event)
    if event['event'] == "MissionFailed":
      MissionTracker.completeMission(event)
    if event['event'] == "Bounty":
      MissionTracker.processKill(event)

def runMassacreHelper():
  loadAllJournals()
  data = []
  while 1:
    data = ReadJournal.fetchJournalUpdate(data)

    for event in data:
      if event['event'] == "MissionAccepted":
        MissionTracker.acceptMission(event)
      if event['event'] == "MissionCompleted":
        MissionTracker.completeMission(event)
      if event['event'] == "MissionAbandoned":
        MissionTracker.completeMission(event)
      if event['event'] == "MissionFailed":
        MissionTracker.completeMission(event)
      if event['event'] == "Bounty":
        MissionTracker.processKill(event)

    print("================== NEW EVENT ==================")
    factions = MissionTracker.factionView()
    for faction in factions:
      s = f"{faction}: "
      for mission in factions[faction]:
        if mission['Kills'] < mission['Targets']:
          s += f"{mission['Kills']}/{mission['Targets']} "
      print(s)

def main():
  runMassacreHelper()
  return

if __name__ == "__main__":
  main()