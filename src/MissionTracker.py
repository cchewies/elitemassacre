import Config

tracker = {}

def acceptMission(event):
  if not event['Name'] in Config.massacreNames: return
  if event['MissionID'] in tracker: return      # Already accepted
  tracker[event['MissionID']] = {}
  mission = tracker[event['MissionID']]
  mission['Faction'] = event['Faction']
  mission['Targets'] = event['KillCount']
  mission['Reward'] = event['Reward']

def completeMission(event):
  if not event['Name'] in Config.massacreNames: return
  if not event['MissionID'] in tracker: return  # Already completed
  del tracker[event['MissionID']]