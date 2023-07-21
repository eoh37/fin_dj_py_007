from django.db import models


class TBL_Usuario(models.Model):
    payroll = models.CharField(max_length=10)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class TBL_Video(models.Model):
    name = models.CharField(max_length=50)
    extension = models.CharField(max_length=5)
    size = models.IntegerField()

    def __str__(self):
        return self.name


class TBL_Video_Usuario(models.Model):
    user_id = models.ForeignKey(
        TBL_Usuario, on_delete=models.CASCADE, related_name="video_user_id"
    )
    video_id = models.ForeignKey(
        TBL_Video, on_delete=models.CASCADE, related_name="video_video_id"
    )

    def __str__(self):
        return f"user_id: {self.user_id}, video_id: {self.video_id}"
