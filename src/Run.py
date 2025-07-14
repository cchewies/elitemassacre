import Config
import ReadJournal
import MissionTracker
import json

def runMassacreHelper():
  data = []
  while 1:
    data = ReadJournal.fetchJournalUpdate(data)
    accept = []
    complete = []

    for event in data:
      if event["event"] == "Missions":
        print(event["Active"])
      if event["event"] == "MissionAccepted":
        accept.append(event)
      if event["event"] == "MissionCompleted":
        complete.append(event)

    for event in accept:
      MissionTracker.acceptMission(event)
    for event in complete:
      MissionTracker.completeMission(event)

    print(json.dumps(MissionTracker.tracker, indent=2))

def main():
  runMassacreHelper()
  return

if __name__ == "__main__":
  main()