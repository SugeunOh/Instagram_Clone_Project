from django.db import models
from ..users import models as user_models


class TimeStampedModel(models.Model):

    created_at = models.DateTimeField(auto_now_add=True)  # 모델이 생성된 날짜, 테이블이 생성될 때 현재 시간이 저장되도록 하는 속성.
    updated_at = models.DateTimeField(auto_now=True)      # 모델이 업데이트 된 날, 테이블이 업데이트 되었을 때 현재 시간이 저장되도록 하는 속성.

    class Meta:
        abstract = True  # abstract base class 임을 알림


class Image(TimeStampedModel):

    file = models.ImageField()                   # 이미지파일
    location = models.CharField(max_length=140)  # 촬영한 위치
    caption = models.TextField()                 # 이미지에 대한 설명


class Comment(TimeStampedModel):

    message = models.TextField()                 # 댓글 텍스트


class Like(TimeStampedModel):

    creator = models.ForeignKey(user_models)
