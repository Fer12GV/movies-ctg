from rest_framework.routers import SimpleRouter

from mdb.api.viewsets import ExampleViewset, MovieViewset

router = SimpleRouter()
router.register('movie', MovieViewset)
router.register('movierate', ExampleViewset)

urlpatterns = router.urls