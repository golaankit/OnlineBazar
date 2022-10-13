
from django.contrib import admin
from django.urls import path
from mainApp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home),
    path('shop/<str:mc>/<str:sc>/<str:br>/',views.shop),
    path('login/',views.login),
    path('logout/',views.logout),
    path('signup/',views.signup),
    path('profile/',views.profilePage),
    path('updateprofile/', views.updateProfilePage),
    path('addproduct/', views.addproduct),
    path('deleteproduct/<int:num>/', views.deleteproduct),
    path('editproduct/<int:num>/', views.editproduct),
    path('singleproduct/<int:num>/',views.singleproduct),
    path('wishlist/<int:num>/',views.wishlist),
    path('deletewishlist/<int:num>/', views.deletewishlist),
    path('addtocart/',views.addtocart),
    path('cart/',views.cartPage),
    path('updatecart/<str:id>/<str:num>/', views.updatecart),
    path('deletecart/<str:id>/', views.deletecart),
    path('checkout/', views.checkout),
    path('confirmation/', views.confirmation),
    path('paymentSuccess/<str:rppid>/<str:rpoid>/<str:rpsid>/',views.paymentSuccess),
    path('paynow/<int:num>/', views.paynow),
    path('contact/', views.contact),
    path('forgetusername/', views.forgetusername),
    path('forgetotp/', views.forgetotp),
    path('forgetpassword/', views.forgetpassword),
    
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

