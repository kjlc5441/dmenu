from django.urls import path
from . import views

urlpatterns = [

    path('<int:list_id>',views.list_note),
    
    path('add',views.add_note),
    path('addB',views.add_noteB),
    path('addC',views.add_noteC),

    path('mod_note/<int:note_id>',views.mod_note),
    path('mod_noteB/<int:note_id>',views.mod_noteB),
    path('mod_noteC/<int:note_id>',views.mod_noteC),

    path('del_note/<int:note_id>',views.del_note),
    path('del_noteB/<int:note_id>',views.del_noteB),
    path('del_noteC/<int:note_id>',views.del_noteC),

    path('store',views.add_store),
    path('mod_store',views.mod_store)


]