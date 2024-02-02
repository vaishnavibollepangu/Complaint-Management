"""vacation URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from complaint_managementapp import views as v
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', v.index, name="index"),
    path('about/', v.about, name="about"),
    path('blog/', v.blog, name="blog"),
    path('blog_single/', v.blog_single, name="blog_single"),
    path('main/', v.main, name="main"),
    path('rooms/', v.rooms, name="rooms"),
    path('services/', v.services, name="services"),
    path('contact/', v.contact, name="contact"),
# Customer urls
    path('customer/', v.customer, name="customer"),
    path('customer_login/', v.customer_login, name="customer_login"),
    path('regpage/', v.regpage, name="regpage"),
    path('customer_home/', v.customer_home, name="customer_home"),
    path('customer_reg/', v.customer_reg, name="customer_reg"),
    path('customer_change/', v.customer_change, name="customer_change"),
    path('customer_display/', v.customer_display, name="customer_display"),
    path('customer_update/', v.customer_update, name="customer_update"),
    path('customer_delete/<int:id>', v.customer_delete, name="customer_delete"),
    path('customer_edit/<int:id>', v.customer_edit, name="customer_edit"),
    path('addcatagory_update/', v.addcatagory_update, name="addcatagory_update"),
    path('addcatagory_delete/<int:id>', v.addcatagory_delete, name="addcatagory_delete"),
    path('addcatagory_edit/<int:id>', v.addcatagory_edit, name="addcatagory_edit"),
    path('addcatagory/', v.addcatagory, name="addcatagory"),
    path('accept_addcatagory/<int:id>', v.accept_addcatagory, name="accept_addcatagory"),
    path('reject_addcatagory/<int:id>', v.reject_addcatagory, name="reject_addcatagory"),
    path('cancel_addcatagory/<int:id>', v.cancel_addcatagory, name="cancel_addcatagory"),
    path('view_update_status/', v.view_update_status, name="view_update_status"),
    path('customer_send_query/', v.customer_send_query, name="customer_send_query"),
    path('customer_view_replay/<int:id>', v.customer_view_replay, name="customer_view_replay"),
    path('customer_view_query/', v.customer_view_query, name="customer_view_query"),

    path('customer_viewcatagory/', v.customer_viewcatagory, name="customer_viewcatagory"),

    path('customer_logout/', v.customer_logout, name="customer_logout"),
# admin urls
    path('admin_login/', v.admin_login, name="admin_login"),
    path('admin_change/', v.admin_change, name="admin_change"),
    path('regpage/', v.regpage, name="regpage"),
    path('admin_home/', v.admin_home, name="admin_home"),

    path('admin_viewcontact/', v.admin_viewcontact, name="admin_viewcontact"),
    path('admin_viewcustomer/', v.admin_viewcustomer, name="admin_viewcustomer"),
    path('admin_viewcatagory/', v.admin_viewcatagory, name="admin_viewcatagory"),
    path('admin_viewquery/', v.admin_viewquery, name="admin_viewquery"),

    path('update_status/<int:id>', v.update_status, name="update_status"),

    path('admin_logout/', v.admin_logout, name="admin_logout"),

# solver urls
    path('solvers/', v.solvers, name="solvers"),
    path('solvers_login/', v.solvers_login, name="solvers_login"),
    path('solvers_regpage/', v.solvers_regpage, name="solvers_regpage"),
    path('solvers_reg/', v.solvers_reg, name="solvers_reg"),
    path('solver_home/', v.solver_home, name="solver_home"),
    path('solvers_edit/<int:id>', v.solvers_edit, name="solvers_edit"),
    path('solvers_update/', v.solvers_update, name="solvers_update"),
    path('solvers_delete/<int:id>', v.solvers_delete, name="solvers_delete"),

    path('solvers_change/', v.solvers_change, name="solvers_change"),
    path('solvers_display/', v.solvers_display, name="solvers_display"),
    path('solvers_view_query/', v.solvers_view_query, name="solvers_view_query"),
    path('solvers_replay/<int:id>', v.solvers_replay, name="solvers_replay"),

    path('solvers_logout/', v.solvers_logout, name="solvers_logout"),

]
