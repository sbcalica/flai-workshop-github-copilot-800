from django.contrib import admin
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """Admin configuration for User model"""
    list_display = ('name', 'email', 'team_id', 'created_at')
    list_filter = ('created_at', 'team_id')
    search_fields = ('name', 'email')
    readonly_fields = ('created_at',)
    ordering = ('-created_at',)


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    """Admin configuration for Team model"""
    list_display = ('name', 'description', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('name', 'description')
    readonly_fields = ('created_at',)
    ordering = ('-created_at',)


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    """Admin configuration for Activity model"""
    list_display = ('activity_type', 'user_id', 'duration', 'calories', 'date', 'created_at')
    list_filter = ('activity_type', 'date', 'created_at')
    search_fields = ('activity_type', 'user_id', 'notes')
    readonly_fields = ('created_at',)
    ordering = ('-created_at',)


@admin.register(Leaderboard)
class LeaderboardAdmin(admin.ModelAdmin):
    """Admin configuration for Leaderboard model"""
    list_display = ('rank', 'user_id', 'team_id', 'total_calories', 'total_activities', 'updated_at')
    list_filter = ('rank', 'updated_at')
    search_fields = ('user_id', 'team_id')
    readonly_fields = ('updated_at',)
    ordering = ('rank',)


@admin.register(Workout)
class WorkoutAdmin(admin.ModelAdmin):
    """Admin configuration for Workout model"""
    list_display = ('name', 'activity_type', 'difficulty', 'duration', 'calories_estimate', 'created_at')
    list_filter = ('activity_type', 'difficulty', 'created_at')
    search_fields = ('name', 'description', 'activity_type')
    readonly_fields = ('created_at',)
    ordering = ('-created_at',)
