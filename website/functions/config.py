import os
secret = os.environ['FIREBASEKEY']
import pyrebase


firebaseConf = {
     'apiKey': secret,
     'authDomain': 'cspickmymeals.firebaseapp.com',
     'databaseURL': 'https://cspickmymeals-default-rtdb.firebaseio.com',
     'projectId': 'cspickmymeals',
     'storageBucket': 'cspickmymeals.appspot.com',
     'messagingSenderId': '906324121880',
     'appId': '1:906324121880:web:9ff3c7693d9b124192266d',
     'measurementId': 'G-DVZP5XDVHR'
}