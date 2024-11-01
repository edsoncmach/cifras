from django.urls import path
from chords.views import ChordView, ChordCreate, CategoryCreate, LiturgicalTimeCreate, MassCreate
from chords.views import ChordUpdate, CategoryUpdate, LiturgicalTimeUpdate, MassUpdate
from chords.views import ChordDelete, CategoryDelete, LiturgicalTimeDelete
from chords.views import ChordList, CategoryList, LiturgicalTimeList, MassList

urlpatterns = [
    #list
    path('list/category/', CategoryList.as_view(), name = 'list-category'),
    path('list/liturgical-time/', LiturgicalTimeList.as_view(), name = 'list-liturgical-time'),
    path('list/mass/', MassList.as_view(), name = 'list-mass'),
    path('list/chords/', ChordList.as_view(), name = 'list-chords'),
    
    #create
    path('create/category/', CategoryCreate.as_view(), name = 'create-category'),
    path('create/liturgical-time/', LiturgicalTimeCreate.as_view(), name = 'create-liturgical-time'),
    path('create/chord/', ChordCreate.as_view(), name = 'create-chord'),
    path('create/mass/', MassCreate.as_view(), name = 'create-mass'),
    
    #update
    path('update/category/<int:pk>', CategoryUpdate.as_view(), name = 'update-category'),
    path('update/liturgical-time/<int:pk>', LiturgicalTimeUpdate.as_view(), name = 'update-liturgical-time'),
    path('update/chord/<int:pk>', ChordUpdate.as_view(), name = 'update-chord'),
    path('update/mass/<int:pk>', MassUpdate.as_view(), name = 'update-mass'),
    
    #delete
    path('delete/category/<int:pk>', CategoryDelete.as_view(), name = 'delete-category'),
    path('delete/liturgical-time/<int:pk>', LiturgicalTimeDelete.as_view(), name = 'delete-liturgical-time'),
    path('delete/chord/<int:pk>', ChordDelete.as_view(), name = 'delete-chord'),
]
