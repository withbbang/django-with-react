from django.contrib import admin
from .models import Post
from django.utils.safestring import mark_safe

# Register your models here.

# admin.site.register(Post) # admin 페이지에 모델 등록하는 방법 첫번째

# admin 페이지에 모델 등록하는 방법 두번째
# 커스텀할 수 있어서 확장성 면에서 좋다
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    # list_display: admin 페이지의 모델 리스트에 출력할 컬럼 지정(message_length: 커스텀 컬럼)
    list_display = ['photo_tag', 'id', 'message', 'message_length', 'is_public', 'create_at', 'updated_at']
    # list_display_links: admin 페이지의 모델 리스트에 링크를 걸고 싶은 컬럼 지정
    list_display_links = ['message']
    # list_filter: admin 페이지의 오른쪽에 단축 필터 UI 추가
    list_filter = ['create_at', 'is_public']
    # search_fields: admin 페이지의 검색 조건 UI 추가
    search_fields = ['message']

    def photo_tag(self, post):
        if post.photo:
            # mark_safe: 보안상 안전한 것을 보장한다는 의미로 해당 태그를 보여주는 메소드
            return mark_safe(f'<img src="{post.photo.url}" style="width: 50px;"/>')
        return None

    # models.py에서의 커스텀 컬럼은 호출하는 모든 곳에서 호출 가능 하지만
    # admin.py의 클래스에서의 커스텀 컬럼은 admin 페이지 내에서만 호출 가능하다.
    # def message_length(self, post) -> str:
    #     return len(post.message)