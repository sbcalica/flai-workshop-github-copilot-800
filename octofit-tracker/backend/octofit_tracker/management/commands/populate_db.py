from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from datetime import date, timedelta
from bson import ObjectId


class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        self.stdout.write('Clearing existing data...')
        
        # Delete existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()
        
        self.stdout.write(self.style.SUCCESS('Existing data cleared'))
        
        # Create Teams
        self.stdout.write('Creating teams...')
        team_marvel = Team.objects.create(
            name='Team Marvel',
            description='Heroes from the Marvel Universe'
        )
        team_dc = Team.objects.create(
            name='Team DC',
            description='Heroes from the DC Universe'
        )
        self.stdout.write(self.style.SUCCESS(f'Created teams: {team_marvel.name}, {team_dc.name}'))
        
        # Create Marvel Users
        self.stdout.write('Creating Marvel users...')
        iron_man = User.objects.create(
            name='Tony Stark',
            email='ironman@marvel.com',
            password='arc_reactor',
            team_id=str(team_marvel._id)
        )
        captain_america = User.objects.create(
            name='Steve Rogers',
            email='captainamerica@marvel.com',
            password='super_soldier',
            team_id=str(team_marvel._id)
        )
        black_widow = User.objects.create(
            name='Natasha Romanoff',
            email='blackwidow@marvel.com',
            password='red_room',
            team_id=str(team_marvel._id)
        )
        thor = User.objects.create(
            name='Thor Odinson',
            email='thor@marvel.com',
            password='mjolnir',
            team_id=str(team_marvel._id)
        )
        hulk = User.objects.create(
            name='Bruce Banner',
            email='hulk@marvel.com',
            password='gamma_ray',
            team_id=str(team_marvel._id)
        )
        
        # Create DC Users
        self.stdout.write('Creating DC users...')
        batman = User.objects.create(
            name='Bruce Wayne',
            email='batman@dc.com',
            password='dark_knight',
            team_id=str(team_dc._id)
        )
        superman = User.objects.create(
            name='Clark Kent',
            email='superman@dc.com',
            password='kryptonite',
            team_id=str(team_dc._id)
        )
        wonder_woman = User.objects.create(
            name='Diana Prince',
            email='wonderwoman@dc.com',
            password='lasso_truth',
            team_id=str(team_dc._id)
        )
        flash = User.objects.create(
            name='Barry Allen',
            email='flash@dc.com',
            password='speed_force',
            team_id=str(team_dc._id)
        )
        aquaman = User.objects.create(
            name='Arthur Curry',
            email='aquaman@dc.com',
            password='trident',
            team_id=str(team_dc._id)
        )
        
        marvel_heroes = [iron_man, captain_america, black_widow, thor, hulk]
        dc_heroes = [batman, superman, wonder_woman, flash, aquaman]
        all_heroes = marvel_heroes + dc_heroes
        
        self.stdout.write(self.style.SUCCESS(f'Created {len(all_heroes)} users'))
        
        # Create Activities
        self.stdout.write('Creating activities...')
        activity_types = ['Running', 'Cycling', 'Swimming', 'Weight Training', 'Yoga', 'Boxing', 'HIIT']
        activity_count = 0
        
        for hero in all_heroes:
            for i in range(5):  # 5 activities per hero
                activity_type = activity_types[i % len(activity_types)]
                duration = 30 + (i * 10)
                calories = duration * 8
                activity_date = date.today() - timedelta(days=i)
                
                Activity.objects.create(
                    user_id=str(hero._id),
                    activity_type=activity_type,
                    duration=duration,
                    calories=calories,
                    date=activity_date,
                    notes=f'{hero.name} completed {activity_type}'
                )
                activity_count += 1
        
        self.stdout.write(self.style.SUCCESS(f'Created {activity_count} activities'))
        
        # Create Leaderboard entries
        self.stdout.write('Creating leaderboard entries...')
        leaderboard_data = [
            (superman, team_dc, 3500, 25, 1),
            (flash, team_dc, 3200, 23, 2),
            (thor, team_marvel, 3000, 22, 3),
            (captain_america, team_marvel, 2800, 20, 4),
            (wonder_woman, team_dc, 2750, 19, 5),
            (iron_man, team_marvel, 2600, 18, 6),
            (batman, team_dc, 2500, 17, 7),
            (black_widow, team_marvel, 2400, 16, 8),
            (hulk, team_marvel, 2300, 15, 9),
            (aquaman, team_dc, 2200, 14, 10),
        ]
        
        for hero, team, calories, activities, rank in leaderboard_data:
            Leaderboard.objects.create(
                user_id=str(hero._id),
                team_id=str(team._id),
                total_calories=calories,
                total_activities=activities,
                rank=rank
            )
        
        self.stdout.write(self.style.SUCCESS(f'Created {len(leaderboard_data)} leaderboard entries'))
        
        # Create Workouts
        self.stdout.write('Creating workout suggestions...')
        workouts = [
            {
                'name': 'Super Soldier Circuit',
                'description': 'High-intensity circuit training for peak performance',
                'activity_type': 'HIIT',
                'difficulty': 'Hard',
                'duration': 45,
                'calories_estimate': 500
            },
            {
                'name': 'Asgardian Strength Builder',
                'description': 'Heavy weight training for maximum strength',
                'activity_type': 'Weight Training',
                'difficulty': 'Hard',
                'duration': 60,
                'calories_estimate': 450
            },
            {
                'name': 'Speedster Cardio Blast',
                'description': 'Fast-paced running intervals',
                'activity_type': 'Running',
                'difficulty': 'Medium',
                'duration': 30,
                'calories_estimate': 350
            },
            {
                'name': 'Amazonian Warrior Yoga',
                'description': 'Flexibility and balance training',
                'activity_type': 'Yoga',
                'difficulty': 'Easy',
                'duration': 45,
                'calories_estimate': 200
            },
            {
                'name': 'Dark Knight Boxing',
                'description': 'Combat training and conditioning',
                'activity_type': 'Boxing',
                'difficulty': 'Hard',
                'duration': 50,
                'calories_estimate': 550
            },
            {
                'name': 'Atlantean Swimming',
                'description': 'Endurance swimming workout',
                'activity_type': 'Swimming',
                'difficulty': 'Medium',
                'duration': 40,
                'calories_estimate': 400
            },
            {
                'name': 'Web-Slinger Agility',
                'description': 'Agility and flexibility training',
                'activity_type': 'HIIT',
                'difficulty': 'Medium',
                'duration': 35,
                'calories_estimate': 380
            },
            {
                'name': 'Infinity Stone Cycling',
                'description': 'Long-distance cycling adventure',
                'activity_type': 'Cycling',
                'difficulty': 'Easy',
                'duration': 60,
                'calories_estimate': 420
            }
        ]
        
        for workout_data in workouts:
            Workout.objects.create(**workout_data)
        
        self.stdout.write(self.style.SUCCESS(f'Created {len(workouts)} workout suggestions'))
        
        self.stdout.write(self.style.SUCCESS('Database population completed successfully!'))
        self.stdout.write(self.style.SUCCESS(f'Summary:'))
        self.stdout.write(f'  - Teams: {Team.objects.count()}')
        self.stdout.write(f'  - Users: {User.objects.count()}')
        self.stdout.write(f'  - Activities: {Activity.objects.count()}')
        self.stdout.write(f'  - Leaderboard entries: {Leaderboard.objects.count()}')
        self.stdout.write(f'  - Workouts: {Workout.objects.count()}')
