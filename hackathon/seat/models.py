# seat/models.py
from django.db import models
from django.utils import timezone

class Bus(models.Model):
    bus_number = models.CharField(max_length=10, default="버스번호")
    route_name = models.CharField(max_length=100, default="노선정보")
    stops = models.ManyToManyField('Stop', related_name='buses')  # 정류장과의 다대다 관계

    def __str__(self):
        return self.bus_number

class Stop(models.Model):
    stop_name = models.CharField(max_length=100, default="정류장이름")
    location = models.CharField(max_length=255, default="위치")  # 예: "위도, 경도"

    def __str__(self):
        return self.stop_name

class Seat(models.Model):
    SEAT_STATUS_CHOICES = [
        ('available', 'Available'),
        ('occupied', 'Occupied'),
    ]

    seat_number = models.CharField(max_length=10, default="좌석")
    status = models.CharField(max_length=10, choices=SEAT_STATUS_CHOICES, default='available')
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE, related_name='seats')
    updated_at = models.DateTimeField(auto_now=True)  # 상태 변경 시간

    def __str__(self):
        return f"{self.bus.bus_number} - {self.seat_number}"
