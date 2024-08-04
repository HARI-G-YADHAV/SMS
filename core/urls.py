from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'students', StudentViewSet)
router.register(r'staff', StaffViewSet)
router.register(r'admissions', AdmissionViewSet)
router.register(r'grades', GradeViewSet)
router.register(r'subjects', SubjectViewSet)
router.register(r'exams', ExamViewSet)
router.register(r'results', ResultViewSet)
router.register(r'attendances', AttendanceViewSet)
router.register(r'timetables', TimetableViewSet)
router.register(r'result-publications', ResultPublicationViewSet)
router.register(r'class-schedules', ClassScheduleViewSet)
router.register(r'rooms', RoomViewSet)
router.register(r'events', EventViewSet)
router.register(r'event-staff', EventStaffViewSet)
router.register(r'user-subjects', UserSubjectViewSet)

urlpatterns = router.urls
