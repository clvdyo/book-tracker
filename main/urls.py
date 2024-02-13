from django.urls import path
from main.views import show_main, create_book, show_xml, show_json, show_xml_by_book_id, show_json_by_book_id

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create_book', create_book, name='create_book'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<int:book_id>/', show_xml_by_book_id, name='show_xml_by_book_id'),
    path('json/<int:book_id>/', show_json_by_book_id, name='show_json_by_book_id'),
]