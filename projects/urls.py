from django.urls import path
from projects import views
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('projects/', views.ProjectListView.as_view(), name='projects'),
    path('partner/', views.PartnerListView.as_view(), name='partner'),
    path('investor/', views.InvestorListView.as_view(), name='investor'),
    path('projects/all_projects', views.Allprojects, name='all_projects'),
    path('projects/engagement_projects', views.Engprojects, name='eng_projects'),
    path('projects/my_projects', views.Myprojects, name='my_projects'),
    path('project/<int:pk>', views.ProjectDetailView.as_view(), name='project-detail'),
    path('partner/<int:pk>', views.PartnerDetailView.as_view(), name='partner-detail'),
    path('investor/<int:pk>', views.InvestorDetailView.as_view(), name='investor-detail'),
    path('projects/search_project', views.Search, name='search_project'),
    path('projects/search_earlyproject', views.MyEarlySearch, name='my_earlysearch'),
    path('projects/my_search', views.MySearch, name='my_search'),
    path('projects/my_keysearch', views.MyKeySearch, name='my_keysearch'),


]


urlpatterns += [
    path('project/create/', views.ProjectCreate.as_view(), name='project_create'),
    path('project/<int:pk>/update/', views.ProjectUpdate.as_view(), name='project_update'),
    path('pcompanies/create/', views.PcompaniesCreate.as_view(), name='pcompanies_create'),
    path('pcompanies/<int:pk>/update/', views.PcompaniesUpdate.as_view(), name='pcompanies_update'),
    path('projectn/<int:pk>/update/', views.ProjectnUpdate.as_view(), name='projectn_update'),
    path('project/<int:pk>/delete/', views.ProjectDelete.as_view(), name='project_delete'),
    path('dialouge/<int:pk>/delete/', views.DialougeDelete.as_view(), name='dialouge_delete'),
    path('partner/create/', views.PartnerCreate.as_view(), name='partner_create'),
    path('partner/<int:pk>/update/', views.PartnerUpdate.as_view(), name='partner_update'),
    path('partner/<int:pk>/delete/', views.PartnerDelete.as_view(), name='partner_delete'),
    path('investor/create/', views.InvestorCreate.as_view(), name='investor_create'),
    path('investor/<int:pk>/update/', views.InvestorUpdate.as_view(), name='investor_update'),
    path('dialouge/new/', views.dialouge_new, name='dialouge_nw'),
    path('ds/new/', views.ds_new, name='ds_nw'),
    path('doc/new/', views.doc_new, name='doc_nw'),


]
