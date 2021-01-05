from reg_asistentes.viewsets import AsistenteViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('asistentes',AsistenteViewSet)
