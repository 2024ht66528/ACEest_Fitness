import json
from app import app

def test_home():
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200
    assert b"ACEest Fitness" in response.data or b"Welcome" in response.data

def test_add_workout_success():
    client = app.test_client()
    response = client.post('/add_workout', 
                           data=json.dumps({"workout": "Pushups", "duration": 20}),
                           content_type='application/json')
    assert response.status_code == 201
    assert b"Pushups" in response.data

def test_add_workout_failure():
    client = app.test_client()
    response = client.post('/add_workout', 
                           data=json.dumps({"workout": ""}),
                           content_type='application/json')
    assert response.status_code == 400

def test_view_workouts():
    client = app.test_client()
    client.post('/add_workout', 
                data=json.dumps({"workout": "Squats", "duration": 15}),
                content_type='application/json')
    response = client.get('/workouts')
    assert response.status_code == 200
    assert b"Squats" in response.data
