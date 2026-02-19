from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from datetime import date


class UserModelTest(TestCase):
    """Test User model"""
    
    def setUp(self):
        self.user = User.objects.create(
            name="Test User",
            email="test@example.com",
            password="password123"
        )
    
    def test_user_creation(self):
        """Test user is created successfully"""
        self.assertEqual(self.user.name, "Test User")
        self.assertEqual(self.user.email, "test@example.com")
        self.assertTrue(self.user._id)
    
    def test_user_str(self):
        """Test user string representation"""
        self.assertEqual(str(self.user), "Test User")


class TeamModelTest(TestCase):
    """Test Team model"""
    
    def setUp(self):
        self.team = Team.objects.create(
            name="Test Team",
            description="A test team"
        )
    
    def test_team_creation(self):
        """Test team is created successfully"""
        self.assertEqual(self.team.name, "Test Team")
        self.assertEqual(self.team.description, "A test team")
        self.assertTrue(self.team._id)
    
    def test_team_str(self):
        """Test team string representation"""
        self.assertEqual(str(self.team), "Test Team")


class ActivityModelTest(TestCase):
    """Test Activity model"""
    
    def setUp(self):
        self.activity = Activity.objects.create(
            user_id="507f1f77bcf86cd799439011",
            activity_type="Running",
            duration=30,
            calories=300,
            date=date.today(),
            notes="Morning run"
        )
    
    def test_activity_creation(self):
        """Test activity is created successfully"""
        self.assertEqual(self.activity.activity_type, "Running")
        self.assertEqual(self.activity.duration, 30)
        self.assertEqual(self.activity.calories, 300)
        self.assertTrue(self.activity._id)
    
    def test_activity_str(self):
        """Test activity string representation"""
        self.assertEqual(str(self.activity), "Running - 30 mins")


class LeaderboardModelTest(TestCase):
    """Test Leaderboard model"""
    
    def setUp(self):
        self.entry = Leaderboard.objects.create(
            user_id="507f1f77bcf86cd799439011",
            team_id="507f1f77bcf86cd799439012",
            total_calories=1000,
            total_activities=10,
            rank=1
        )
    
    def test_leaderboard_creation(self):
        """Test leaderboard entry is created successfully"""
        self.assertEqual(self.entry.total_calories, 1000)
        self.assertEqual(self.entry.total_activities, 10)
        self.assertEqual(self.entry.rank, 1)
        self.assertTrue(self.entry._id)
    
    def test_leaderboard_str(self):
        """Test leaderboard string representation"""
        self.assertEqual(str(self.entry), "Rank 1 - 1000 calories")


class WorkoutModelTest(TestCase):
    """Test Workout model"""
    
    def setUp(self):
        self.workout = Workout.objects.create(
            name="Morning Cardio",
            description="High intensity cardio workout",
            activity_type="Cardio",
            difficulty="Medium",
            duration=45,
            calories_estimate=400
        )
    
    def test_workout_creation(self):
        """Test workout is created successfully"""
        self.assertEqual(self.workout.name, "Morning Cardio")
        self.assertEqual(self.workout.difficulty, "Medium")
        self.assertEqual(self.workout.duration, 45)
        self.assertTrue(self.workout._id)
    
    def test_workout_str(self):
        """Test workout string representation"""
        self.assertEqual(str(self.workout), "Morning Cardio")


class APIEndpointsTest(APITestCase):
    """Test API endpoints"""
    
    def test_api_root(self):
        """Test API root endpoint is accessible"""
        response = self.client.get('/api/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('users', response.data)
        self.assertIn('teams', response.data)
        self.assertIn('activities', response.data)
        self.assertIn('leaderboard', response.data)
        self.assertIn('workouts', response.data)
    
    def test_users_list(self):
        """Test users list endpoint"""
        response = self.client.get('/api/users/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_teams_list(self):
        """Test teams list endpoint"""
        response = self.client.get('/api/teams/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_activities_list(self):
        """Test activities list endpoint"""
        response = self.client.get('/api/activities/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_leaderboard_list(self):
        """Test leaderboard list endpoint"""
        response = self.client.get('/api/leaderboard/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_workouts_list(self):
        """Test workouts list endpoint"""
        response = self.client.get('/api/workouts/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
