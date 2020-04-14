"""certify URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls.static import static
from cert import views
from cert import quiz_flow
from cert import regression
from cert import certificates
from certify import settings

urlpatterns = static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + \
              static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + \
              [
                  path('admin/', admin.site.urls),
                  path('', views.index),
                  path('logout', views.log_me_out),
                  path('regression', regression.regression_start),
                  path('complete', regression.complete),
                  path('finish_regression', regression.finish_regression),
                  path('reply/<int:number>', quiz_flow.reply),
                  path('test_question/<int:number>', quiz_flow.test_question),
                  path('test_results/<int:number>', quiz_flow.test_results),
                  path('questions_list/<int:number>', quiz_flow.questions_list),
                  path('delete/<int:number>', views.delete_assignment),
                  path('send_email/<int:number>', views.send_email),
                  path('start_quiz', quiz_flow.start),
                  path('time_left', quiz_flow.time_left_http),
                  path('generate_certificate/<int:id>', certificates.generate),
              ]
