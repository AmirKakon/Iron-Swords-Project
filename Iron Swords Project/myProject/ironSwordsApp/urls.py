from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
from .views import HeroListView
from .views import kibbutz_stories, add_kibbutz_story, update_kibbutz_story, delete_kibbutz_story
from .views import add_nova_party_testimony, update_testimonial, delete_nova_party_testimony
from .views import testimonies_abductees, add_abductee_testimony, update_abductee_testimony, delete_abductee_testimony
from .views import abductee_details
from .views import edit_comment, delete_comment, light_candle


urlpatterns = [
    path('', views.home, name='home'),
    path('add-hero/', views.add_hero, name='add_hero'),
    path('login/', views.login_view, name='login'),
    path('transition/', views.transition, name='transition'),
    path('forgot-password/', views.forgot_password_view, name='forgot_password'),
    path('forgot-password-submit/', views.forgot_password_submit, name='forgot_password_submit'),
    path('create-account/', views.create_account_view, name='create_account'),
    path('register/', views.register, name='register'),
    path('hall-of-fame/', views.hall_of_fame, name='hall_of_fame'),
    path('join_form_for_hero/', views.join_form_for_hero, name='join_form_for_hero'),
    path('edit_hero/<int:hero_id>/', views.edit_hero, name='edit_hero'),
    path('delete_hero/<int:hero_id>/', views.delete_hero, name='delete_hero'),
    path('join_form/', views.join_form, name='join_form'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('heroes/', HeroListView.as_view(), name='hero_list'),

    path('transition/', views.transition, name='transition'),
    path('kibbutz_stories/', kibbutz_stories, name='kibbutz_stories'),
    path('add_kibbutz_story/', add_kibbutz_story, name='add_kibbutz_story'),
    path('delete_kibbutz_story/<int:story_id>/', delete_kibbutz_story, name='delete_kibbutz_story'),
    path('update_kibbutz_story/<int:story_id>/', update_kibbutz_story, name='update_kibbutz_story'),

    path('nova-party-evidence/<int:id>/', views.nova_party_evidence, name='nova_party_evidence'),
    path('nova-party-evidence/', views.nova_party_evidence, name='nova_party_evidence'),
    path('add_testimony/', add_nova_party_testimony, name='add_nova_party_testimony'),
    path('testimonial/edit/<int:pk>/', views.update_testimonial, name='update_testimonial'),
    path('delete_testimony/<int:testimony_id>/', views.delete_nova_party_testimony, name='delete_nova_party_testimony'),
    
    path('zaka_people/', views.zaka_people, name='zaka_people'),
    path('comment/edit/<int:comment_id>/', edit_comment, name='edit_comment'),
    path('delete_comment/<int:comment_id>/', delete_comment, name='delete_comment'),

    path('testimonies-abductees/', testimonies_abductees, name='testimonies-abductees'),
    path('add-abductee-testimony/', add_abductee_testimony, name='add_abductee_testimony'),
    path('update-abductee-testimony/<int:testimony_id>/', update_abductee_testimony, name='update_abductee_testimony'),
    path('delete-abductee-testimony/<int:testimony_id>/', delete_abductee_testimony, name='delete_abductee_testimony'),
    path('abductee/<int:id>/', abductee_details, name='abductee_details'),
    path('testimonies/', views.testimonies_abductees, name='testimonies-abductees'),
    path('testimonies/', views.testimonies_abductees, name='testimonies_abductees'),
   


    path('difficult-documents/', views.difficult_documents, name='difficult_documents'),
    path('difficult_documents_view/', views.difficult_documents_view, name='difficult_documents_view'),

    path('about/', views.about, name='about'),

    path('light-candle/', light_candle, name='light_candle'),
    path('candle-list/', light_candle, name='candle_list'),  


    # Class-based views
    path('hero/new/', views.HeroCreateView.as_view(), name='hero-create'),
    path('hero/<int:pk>/edit/', views.HeroUpdateView.as_view(), name='hero-update'),
    path('hero/<int:pk>/delete/', views.HeroDeleteView.as_view(), name='hero-delete'),
    path('hero/<int:hero_id>/', views.hero_detail, name='hero_detail'),
    
    ]