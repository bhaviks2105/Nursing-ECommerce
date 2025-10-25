from django.contrib import admin
from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_view
from .froms import LoginForm,MyPasswordResetForm,PasswordChangeForm


urlpatterns = [
    path('', views.home),
    path('about/',   views.about,  name='about'),
    path('contact/', views.contact, name='contact'),
    path('category/<slug:val>/', views.CategoryView.as_view(), name='category'),
    path('category-title/<val>', views.CategoryTitle.as_view(), name='category-title'),
    path('product-detail/<int:pk>', views.ProductDetail.as_view(), name='product-detail'),
    path('profile/',views.ProfileView.as_view(),name='profile'),
    path('address/', views.address, name='address'),
    path('updateAddress/<int:pk>', views.UpdateAddress.as_view(), name='updateAddress'),
    path('add-to-cart/',views.add_to_cart,name='add-to-cart'),
    path('cart/',views.show_cart,name='showcart'),
    path('checkout/',views.checkout.as_view(),name='checkout'),
    path('payment_done/',views.payment_done,name='payment_done'),
    path('orders/',views.orders,name='orders'),
    path('search/',views.search,name="search"),


    path('pluscart/',views.plus_cart),
    path('minuscart/',views.minus_cart),
    path('removecart/',views.remove_cart),



                  # login
    path('registration/',views.CustomerRegistrationView.as_view(),name='customerregistration'),
    path('accounts/login/', auth_view. LoginView.as_view(template_name='plants/login.html', authentication_form=LoginForm), name='login'),
    path('password_reset/', auth_view. PasswordResetView.as_view(template_name='plants/password_reset.html', form_class=MyPasswordResetForm),name='password_reset'),
    path('logout/', auth_view.LogoutView.as_view(next_page='login'),name='logout'),

         ]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)