"""
Push Here Agency signatures to every Gmail account in one go (Gmail API).

Setup (one time, Google Workspace admin):
  1. Google Cloud project > enable the Gmail API.
  2. Create a service account, download its JSON key as service-account.json.
  3. Admin console > Security > API controls > Domain-wide delegation:
     add the service account client ID with the scope
     https://www.googleapis.com/auth/gmail.settings.basic
  4. pip install google-api-python-client google-auth

Run:
  python push_signatures.py            # dry run, prints what would change
  python push_signatures.py --apply    # writes the signatures
"""
import json
import sys

from google.oauth2 import service_account
from googleapiclient.discovery import build

SCOPES = ["https://www.googleapis.com/auth/gmail.settings.basic"]
KEY_FILE = "service-account.json"
APPLY = "--apply" in sys.argv

team = json.load(open("signatures.json"))

for person in team:
    email = person["email"]
    creds = service_account.Credentials.from_service_account_file(
        KEY_FILE, scopes=SCOPES
    ).with_subject(email)
    gmail = build("gmail", "v1", credentials=creds, cache_discovery=False)

    if not APPLY:
        print(f"[dry run] {email}: {len(person['html'])} chars")
        continue

    gmail.users().settings().sendAs().patch(
        userId="me",
        sendAsEmail=email,
        body={"signature": person["html"]},
    ).execute()
    print(f"updated {email}")
