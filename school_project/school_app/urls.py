from django.urls import path,include
from.import views

urlpatterns = [
    path('login',views.login1,name='login1'),
    path('regteacher',views.regteacher,name='regteacher'),
    path('studregister',views.studregister,name='studregister'),
    path('studview',views.studentview,name='studview'),
    path('approve/<int:sid>',views.approve,name='approve'),
    path('viewteacher',views.viewteacher,name='viewteacher'),
    path('viewstudent',views.viewstudent,name='viewstudent'),
    path('editteacher/<int:eid>',views.editteacher,name='editteacher'),
    path('editstudents/<int:eid>',views.editstudents,name='editstudents'),
    path('deletestudents/<int:did>',views.deletestudents,name='deletestudents'),
    path('deleteteacher/<int:did>',views.deleteteacher,name='deleteteacher'),
    path('',views.Homepage,name='homepage'),
    path('adminhome',views.adminhome,name='adminhome'),
    path('teacherhome',views.teacherhome,name='teacherhome'),
    path('studhome',views.studenthome,name='studenthome'),
    path('managestudent',views.managestudent,name='managestudent'),
    path('studviewteacher',views.studviewteacher,name='studviewteacher'),
    path('logout',views.logout,name='logout'),
    path('studprofile',views.studprofile,name='studprofile'),
    path('editstudprofile',views.editstudprofile,name='editstudprofile'),
    path('editstudprofile1',views.editstudprofile1,name='editstudprofile1'),
    path('Teacherprofile',views.teacherprofile,name='teacherprofile'),
    path('Editteacherprofile',views.Editteacherprofile,name='editteacherprofile'),
    path('editteacherprofile1',views.Editteacherprofile1,name='editteacherprofile1'),
    path('home',views.Home,name='home'),


 

]