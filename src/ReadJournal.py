import Config
import json

def obtainAllJournals():
  journals = []
  for journal in Config.dir.glob("Journal.*"):
    journals.append(str(journal))
  return journals

def obtainLatestJournal():
  latest = ""
  for journal in Config.dir.glob("Journal.*"):
    if str(journal) > latest:
      latest = str(journal)
  return latest

def fetchJournalUpdate(data):
  while 1:
    latest = obtainLatestJournal()
    with open(latest, 'r') as file:
      check = [json.loads(line) for line in file if line.strip()]

    if check != data: 
      print("Data updated!")
      return check

def main():
  fetchJournalUpdate()
  return

if __name__ == "__main__":
  main()