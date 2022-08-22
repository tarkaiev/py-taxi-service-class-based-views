from django.urls import path

from .views import index, ManufacturerListView, CarListView, DriverListView, CarDetailView, DriverDetailView

urlpatterns = [
    path("", index, name="index"),
    path("manufacturers/", ManufacturerListView.as_view(), name="manufacturer-list-view"),
    path("cars/", CarListView.as_view(), name="car-list-view"),
    path("cars/<int:pk>/", CarDetailView.as_view(), name="car-detail"),
    path("drivers/", DriverListView.as_view(), name="driver-list-view"),
    path("drivers/<int:pk>/", DriverDetailView.as_view(), name="driver-detail.html"),
]

app_name = "taxi"
