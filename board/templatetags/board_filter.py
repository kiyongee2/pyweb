# 빼기 필터 만들기
from django import template
register = template.Library()

@register.filter
def sub(value, arg):
    return value - arg

# 기존값에서 arg를 뺌
# 사용 - value|sub:3  (value-3)