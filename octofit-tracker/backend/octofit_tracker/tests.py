from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class BasicModelTest(TestCase):
    def test_create_team(self):
        team = Team.objects.create(name='Marvel', description='Marvel Team')
        self.assertEqual(str(team), 'Marvel')
    def test_create_user(self):
        team = Team.objects.create(name='DC', description='DC Team')
        user = User.objects.create(name='Clark Kent', email='clark@dc.com', team=team)
        self.assertEqual(str(user), 'Clark Kent')
    def test_create_activity(self):
        team = Team.objects.create(name='Marvel', description='Marvel Team')
        user = User.objects.create(name='Tony Stark', email='tony@marvel.com', team=team)
        activity = Activity.objects.create(user=user, type='Running', duration=30, date='2023-01-01')
        self.assertEqual(str(activity), 'Tony Stark - Running')
    def test_create_workout(self):
        team = Team.objects.create(name='Marvel', description='Marvel Team')
        workout = Workout.objects.create(name='Cardio', description='Cardio workout')
        workout.suggested_for.add(team)
        self.assertEqual(str(workout), 'Cardio')
    def test_create_leaderboard(self):
        team = Team.objects.create(name='DC', description='DC Team')
        user = User.objects.create(name='Bruce Wayne', email='bruce@dc.com', team=team)
        leaderboard = Leaderboard.objects.create(user=user, score=100)
        self.assertEqual(str(leaderboard), 'Bruce Wayne: 100')
