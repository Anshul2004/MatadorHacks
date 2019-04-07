import pyrebase

pyrebase_config = {
    "apiKey": "AIzaSyBMg9AajqEe3CEU4pECCV_qigNyr_iNeYM",
    "authDomain": "matadorhacks2019-48013.firebaseapp.com",
    "databaseURL": "https://matadorhacks2019-48013.firebaseio.com",
    "projectId": "matadorhacks2019-48013",
    "storageBucket": "matadorhacks2019-48013.appspot.com",
    "messagingSenderId": "68907136805",
    "serviceAccount": "matadorhacks2019-48013-firebase-adminsdk-81n5i-712fc25364.json"
}

firebase = pyrebase.initialize_app(pyrebase_config)
db = firebase.database()

db.child("test").push("test")