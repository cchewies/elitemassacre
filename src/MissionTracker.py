import Config

tracker = {}

def acceptMission(event):
  if not event['Name'] in Config.massacreNames: return
  if event['MissionID'] in tracker: return      # Already accepted
  tracker[event['MissionID']] = {}
  mission = tracker[event['MissionID']]
  mission['Timestamp'] = event['timestamp']
  mission['Faction'] = event['Faction']
  mission['Targets'] = event['KillCount']
  mission['Kills'] = 0
  mission['Reward'] = event['Reward']
  mission['Wing'] = event['Wing']

def processKill(event):
  for missionID in tracker.keys():
    mission = tracker[missionID]
    if event['timestamp'] > mission['Timestamp']:
      mission['Kills'] += 1

def completeMission(event):
  if not event['MissionID'] in tracker: return  # Already completed
  del tracker[event['MissionID']]

def factionView():
  factions = {}
  for missionID in tracker.keys():
    mission = tracker[missionID]
    if not mission['Faction'] in factions:
      factions[mission['Faction']] = []
    factions[mission['Faction']].append(mission)
  return factions