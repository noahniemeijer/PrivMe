import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# Initialize Firebase Admin SDK
cred = credentials.Certificate('cred.json')
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://privme-1be9c-default-rtdb.europe-west1.firebasedatabase.app/'
})

def receive_message(event):
    data = event.data
    if isinstance(data, dict):
        for key, message in data.items():
            print(f"{message}")
    elif isinstance(data, str):
        print(f"{data}")

ref = db.reference("/")
ref.listen(receive_message)
