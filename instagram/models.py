from django.db import models

class Post(models.Model):
    message = models.TextField()
    # ImageField 내부에서 기본적으로 pillow 라이브러리를 사용하므로 필히 설치 요함
    # upload_to:
    # 미지정시 settings.py의 MEDIA_URL에 지정된 경로로 파일 저장
    # 지정시 MEDIA_URL의 경로로 부터 하위 경로에 파일 저장
    # 기본적으로 대규모 서비스일 수록 폴더의 세분화가 이루어진다
    photo = models.ImageField(blank=True, upload_to='instagram/post/%Y/%m/%d')
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