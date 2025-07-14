import Config as cf

def obtainLatestJournal():
  latest = ""
  for journal in cf.dir.glob("Journal.*"):
    # print(journal.stem)
    if journal.stem > latest:
      latest = journal.stem
  print(f"Latest: {latest}")
  return latest

def main():
  latest = obtainLatestJournal()
  return

if __name__ == "__main__":
  main()