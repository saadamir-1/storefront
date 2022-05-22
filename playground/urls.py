from django.urls import path, register_converter
from . import views

class FloatUrlParameterConverter:
    regex = '[0-9]+\.?[0-9]+'

    def to_python(self, value):
        return float(value)

    def to_url(self, value):
        return str(value)

register_converter(FloatUrlParameterConverter, 'float')

urlpatterns = [
    path('hello/<str:startYear>/<str:endYear>/<str:region>', views.run_project),
    path('map/<str:startYear>/<str:endYear>/<str:region>/<float:a1>/<float:a2>/<float:b2>/<float:c1>/<float:c2>/<float:d1>/<float:d2>/', views.run_project_map)
]