from django.db import models

class Post(models.Model):
    message = models.TextField()
    # ImageField 내부에서 기본적으로 pillow 라이브러리를 사용하므로 필히 설치 요함
    photo = models.ImageField(blank=True)
    is_public = models.BooleanField(default=False, verbose_name='공개 여부')
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # admin 페이지에서 보여줄 대표 텍스트(list_display가 정의되어있지 않아야함)
    def __str__(self) -> str:
        return self.message

    # 하위에서처럼 커스텀 컬럼도 생성할 수 있다. -> list_display에서 메소드명만 추가하면 노출된다.
    def message_length(self) -> str:
        return len(self.message)
    # 커스텀 컬럼명 변경
    message_length.short_description = "메세지 글자수"