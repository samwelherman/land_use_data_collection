from django.urls import path
from . import views


urlpatterns = [
    path('', views.dashboard,name='test'),

    # path('downloadimage/<str:imageid>/$', views.download_image, name='download_image'),
    path('filter/<int:id>/', views.filter,name='filter'),
    path('mapview', views.mapView,name='mapview'),

    path('tablefilter', views.tableView,name='tablefilter'),
    path('tableview', views.tableView,name='tableview'),

    # path('chartview', views.chartView,name='chartview'),
    path('analyticfilter', views.analyticView,name='analyticfilter'),
    path('analyticview', views.analyticView,name='analyticview'),

]