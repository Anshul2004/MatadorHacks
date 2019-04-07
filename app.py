from flask import Flask, redirect, render_template, session, url_for, request
from functools import wraps
import pyrebase, json

app = Flask(__name__)
app.secret_key = 'ji23ri23rf2nif3nif23ionf3nio2f3'

#-------------------------------------------------------
# Firebase
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

def collect_info(database, name=None):
    if name is None:
        return db.child(database).get().val()
    else:
        return db.child(database).child(name).get().val()

def add_info(data, name, database):
    db.child(database).child(name).set(data)

def edit_info(data, name, database):
    db.child(database).child(name).update(data)

def remove_info(name, database):
    db.child(database).remove(name)

#-------------------------------------------------------

def logged_in():
    return 'user' in session

@app.route('/', methods=['GET'])
def home_page():
    if logged_in():
        return render_template('main-home.html', logged_in=logged_in(), type=session['user']['type'])
    else:
        return render_template('main-home.html', logged_in=logged_in())


@app.route('/login', methods=['GET', 'POST'])
def login_page():
    if request.method == 'GET':
        # Already Logged In
        if logged_in():
            return render_template('main-home.html', logged_in=logged_in(), type=session['user']['type'])

        # Log in
        else:
            return render_template('log-in.html', error=False, logged_in=logged_in())

    elif request.method == 'POST':
        data = {
            'username': request.form.get('username'),
            'password': request.form.get('password')
        }

        error = None
        try:
            student = collect_info('students', data['username'])
            if student is None:
                raise ValueError

            else:
                if student['password'] != data['password']:
                    error = True

        except ValueError:
            staff = collect_info('staffs', data['username'])
            if staff['password'] != data['password']:
                error = True
        except:
            error = True

        if error:
            return render_template('log-in.html', error=True, logged_in=logged_in())

        else:
            students_data = collect_info('students')
            staffs_data = collect_info('staffs')

            if students_data is not None and data['username'] in students_data:
                session['user'] = {
                    'type': 'student',
                    'name': data['username']
                }

            elif staffs_data is not None and data['username'] in staffs_data:
                session['user'] = {
                    'type': 'staff',
                    'name': data['username']
                }
            
            return redirect(url_for('home_page'))

@app.route('/signup', methods=['GET', 'POST'])
def signup_page():
    if request.method == 'GET':
        # Already Logged In
        if logged_in():
            return render_template('home.html', logged_in=logged_in(), type=session['user']['type'])

        # Sign up
        else:
            return render_template('sign-up.html', errors=False, logged_in=logged_in())

    elif request.method == 'POST':
        data = {
            'first name': request.form.get('firstname'),
            'last name': request.form.get('lastname'),
            'email': request.form.get('email'),
            'username': request.form.get('username'),
            'password': request.form.get('password'),
            'school': request.form.get('school')
        }
        
        
        errors = {
            'email': None,
            'username': None,
            'school': None,
            'total': None
        }

        if request.form.get('type') == 'student':
            students = collect_info('students')
            if students is not None:
                for user in students:
                    if collect_info('students', user)['email'] == data['email']:
                        errors['email'] = True
                        errors['total'] = True
                    if collect_info('students', user)['username'] == data['username']:
                        errors['username'] = True
                        errors['total'] = True

        elif request.form.get('type') == 'staff':
            staffs = collect_info('staffs')
            if staffs is not None:
                for user in staffs:
                    if collect_info('staffs', user)['email'] == data['email']:
                        errors['email'] = True
                        errors['total'] = True
                    if collect_info('staffs', user)['username'] == data['username']:
                        errors['username'] = True
                        errors['total'] = True
                    if collect_info('staffs', user)['school'] == data['school']:
                        errors['school'] = True
                        errors['total'] = True


        # Values are not unique
        if errors['total']:
            return render_template('sign-up.html', errors=errors, logged_in=logged_in(), type=request.form.get('type'))

        # Input to Firebase
        if request.form.get('type') == 'student':
            add_info(data, data['username'], 'students')
        elif request.form.get('type') == 'staff':
            add_info(data, data['username'], 'staffs')

        # Redirect
        return render_template('signup-thankyou.html', logged_in=logged_in(), type=request.form.get('type'))


@app.route('/logout', methods=['GET'])
def logout():
    if request.method == 'GET':
        if logged_in():
            del session['user']
            return redirect(url_for('home_page'))


@app.route('/create-club', methods=['GET', 'POST'])
def create_club_page():
    if request.method == 'GET':
        if logged_in():
            return render_template('create.html', logged_in=logged_in(), type=session['user']['type'])

        else:
            return render_template('create.html', logged_in=logged_in())

    elif request.method == 'POST':
        #if logged_in():
        if True:
            data = {
                'name': request.form.get('name'),
                'president': request.form.get('president'),
                'purpose': request.form.get('purpose'),
                'email': request.form.get('email'),
                'advisor': request.form.get('advisor')
            }
            data['clubcode'] = data['name'].replace(' ', '-')
        
            clubs = collect_info('clubs')

            error = None
            
            if clubs is not None:
                for item in clubs:
                    if collect_info('clubs', item)['name'] == data['name']:
                        error = True

            # Values are not unique
            if error:
                return render_template('sign-up.html', error=error, logged_in=logged_in(), type=session['user']['type'])

            # Input to Firebase
            add_info(data, data['name'], 'clubs')

            # Redirect
            return render_template('club-thankyou.html', clubcode=data['name'].replace(' ', '-'), logged_in=logged_in(), type=session['user']['type'])


@app.route('/clubs', methods=['GET'])
def clubs_page():
    if request.method == 'GET':
        clubs_data = {}
        for club in collect_info('clubs'):
            temp = collect_info('clubs', club)
            clubs_data[club] = {
                'name': temp['name'],
                'president': temp['president'],
                'purpose': temp['purpose'],
                'email': temp['email'],
                'advisor': temp['advisor'],
                'clubcode': temp['clubcode']
            }


        if len(clubs_data) == 0:
            clubs_data = None

        clubs_list = []
        for club in clubs_data:
            clubs_list.append(club)

        with open('search.json', 'r+') as f:
            clubs_json = json.load(f)

        if len(clubs_json) == len(clubs_list):
            same = 0
            clubs_list = clubs_json
        else:
            with open('search.json', 'r+') as f:
                json.dump(clubs_list, f)


        return render_template('clubs2.html', clubs=clubs_data, club_list=clubs_list, logged_in=logged_in(), \
            type=session['user']['type'], user_info=collect_info(session['user']['type'], session['user']['name']))

@app.route('/clubs/<clubcode>', methods=['GET', 'POST'])
def clubs_individual_page(clubcode):
    clubname = clubcode.replace('-', ' ')

    if request.method == 'GET':
        # List of Clubs
        if clubname is None:
            pass

        # Club Page
        else:
            return render_template('clubs-page.html', info=collect_info('clubs', clubname), logged_in=logged_in(), \
                type=session['user']['type'], user_info=collect_info(session['user']['type']+'s', session['user']['name']))

    elif request.method == 'POST':
        data = {
            'name': request.form.get('name'),
            'comment': request.form.get('comment')
        }

        person_data = collect_info('students', session['user']['name'])
        
        # Club already exists
        if 'clubs' in person_data and data['name'] in person_data['clubs']:
            return 'hi'

        # Register for a club
        else:
            if 'clubs' not in person_data:
                person_data['clubs'] = [clubname]
            else:
                person_data['clubs'].append(clubname)

            clubs_data = collect_info('clubs', clubname)
            if 'people' in clubs_data:
                clubs_data['people'].append(session['user']['name'])
            else:
                clubs_data['people'] = [session['user']['name']]

        edit_info(person_data, session['user']['name'], 'students')
        edit_info(clubs_data, clubname, 'clubs')
        return render_template('club-thankyou.html', clubcode=clubs_data['clubcode'])


@app.route('/profile', methods=['GET'])
def profile_page():
    if request.method == 'GET':
        if logged_in():
            if session['user']['type'] == 'student':
                user_data = collect_info('students', session['user']['name'])

            elif session['user']['type'] == 'staff':
                user_data = collect_info('staffs', session['user']['name'])

            user_clubs_1 = None
            length = None
            if 'clubs' in user_data:
                user_clubs_1 = user_data['clubs'][1:-1]

                length = len(user_data['clubs'])

            return render_template('profile.html', user=user_data, logged_in=logged_in(), type=session['user']['type'], user_clubs=user_clubs_1, length=length)

if __name__ == '__main__':
    app.run(debug=True)