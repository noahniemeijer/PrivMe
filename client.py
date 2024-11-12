import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

import asyncio
import json

cred = credentials.Certificate('cred.json')
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://privme-1be9c-default-rtdb.europe-west1.firebasedatabase.app/'
})


def send_message():
    while True:
        ref = db.reference("/")
        ref.set({})
        msg = str(input())
        ref.push(msg)

send_message()



