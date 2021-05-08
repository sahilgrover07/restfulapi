
from leaderboardapi.viewsets import leaderBoardViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('leaderboard',leaderBoardViewset)


