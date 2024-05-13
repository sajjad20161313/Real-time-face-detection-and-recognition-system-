import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://faceattendence-ec320-default-rtdb.firebaseio.com/",
    'storageBucket': "faceattendence-ec320.appspot.com"
})

ref = db.reference('Students')

data = {
    "20171446":
        {
            "name": "Animesh Singha",
            "Subject": "CSE",
            "starting_year": 2018,
            "total_attendance": 7,
            "Batch": "4th",
            "year": 4,
            "last_attendance_time": "2024-05-11 00:54:34"
        },
    "852741":
        {
            "name": "Emly Blunt",
            "Subject": "Economics",
            "starting_year": 2021,
            "total_attendance": 7,
            "Batch": "4th",
            "year": 1,
            "last_attendance_time": "2024-05-11 00:54:34"
        },
    "963852":
        {
            "name": "Elon Musk",
            "Subject": "Physics",
            "starting_year": 2020,
            "total_attendance": 7,
            "Batch": "4th",
            "year": 2,
            "last_attendance_time": "2024-05-11 00:54:34"
        },
    "20161313":
        {
            "name": "Sajjad Hossain",
            "Subject": "CSE",
            "starting_year": 2017,
            "total_attendance": 7,
            "Batch": "3rd",
            "year": 4,
            "last_attendance_time": "2024-05-11 00:54:34"
        }
}

for key, value in data.items():
    ref.child(key).set(value)
