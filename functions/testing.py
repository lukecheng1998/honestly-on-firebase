from firebase import firebase

firebase = firebase.FirebaseApplication("https://honestly-on-firebase.firebaseio.com/", None)
data = {
    'results': '',
    'textfield': 'google'
}
result = firebase.post('/searches', data)