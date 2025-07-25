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

def runMassacreHelper():
  loadAllJournals()
  data = []
  while 1:
    data = ReadJournal.fetchJournalUpdate(data)
    MissionTracker.reset()

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

    print(f"================ Missions ({MissionTracker.getLen()}/20) ================")
    factions = MissionTracker.factionView()
    for faction in factions:
      hasActive = False
      targetsSum = 0
      s = f"{faction}: "
      for mission in factions[faction]:
        targetsSum += mission['Targets']
      for mission in factions[faction]:
        if mission['Kills'] < targetsSum:
          hasActive = True
          s += f"{mission['Kills']}/{mission['Targets']} "
      if hasActive: print(s)

def main():
  runMassacreHelper()
  return

if __name__ == "__main__":
  main()