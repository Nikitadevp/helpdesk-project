from django.urls import path
from .views import raise_ticket, resolve_ticket,dashboard, charts




urlpatterns = [
    path('raise-ticket/', raise_ticket, name='raise_ticket'),
    path('resolve-ticket/<str:ticket_no>/', resolve_ticket, name='resolve_ticket'),
    #path('', raise_ticket),
    #path('raise-ticket/', raise_ticket),

    #  Resolve Ticket Page
    #path("resolve-ticket/<str:ticket_no>/", resolve_ticket),
   #path("", dashboard, name="dashboard"),
    path("dashboard/", dashboard, name="dashboard"),

    path("charts/", charts, name="charts"),
    

   
    
    
]
