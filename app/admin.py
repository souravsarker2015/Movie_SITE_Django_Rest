from django.contrib import admin

from app.models import Stream, WatchList, Review


@admin.register(Stream)
class AdminRegister(admin.ModelAdmin):
    list_display = ['id', 'name', 'about', 'website_link']


@admin.register(WatchList)
class AdminWatchList(admin.ModelAdmin):
    list_display = ['id', 'title', 'story_line', 'platform', 'active', 'avg_rating', 'num_rating', 'created']


@admin.register(Review)
class AdminReview(admin.ModelAdmin):
    list_display = ['id', 'review_user', 'rating', 'description', 'watchlist', 'active', 'created', 'updated']
