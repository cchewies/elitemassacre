import Config
import json
import os
import time

def obtainAllJournals():
  journals = []
  for journal in Config.dir.glob("Journal.*"):
    age = (time.time() - os.path.getmtime(journal)) / (60 * 60 * 24)
    if age < 8:
      print(f"Loaded journal with age {age} days")
      journals.append(str(journal))
  return journals

def readAllJournals():
  journals = obtainAllJournals()
  data = []
  for journal in journals:
    with open(journal, 'r') as file:
      data += [json.loads(line) for line in file if line.strip()]
  return data

def obtainLatestJournal():
  latest = ""
  for journal in Config.dir.glob("Journal.*"):
    if str(journal) > latest:
      latest = str(journal)
  return latest

def readLatestJournal():
  latest = obtainLatestJournal()
  with open(latest, 'r') as file:
    return [json.loads(line) for line in file if line.strip()]

def fetchJournalUpdate(data):
  while 1:
    check = readLatestJournal()
    if check != data: 
      print("Data updated!")
      return check

def main():
  fetchJournalUpdate()
  return

if __name__ == "__main__":
  main()