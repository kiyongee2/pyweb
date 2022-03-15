from django.contrib.auth.models import User
from django.db import models

# 질문 모델
class Question(models.Model):
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()  # not null
    modify_date = models.DateTimeField(null=True, blank=True)  #null 허용, blank- 폼 데이터 null
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_question')  #User의 username와 외래키 설정
    voter = models.ManyToManyField(User, related_name='voter_question')   #추천수 - 다대다 관계

    def __str__(self):
        return self.subject

# 답변 모델
class Answer(models.Model):
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.content

# 댓글 모델
class Comment(models.Model):
    content = models.TextField()    #댓글 내용
    create_date = models.DateTimeField()  #댓글 작성일
    modify_date = models.DateTimeField(null=True, blank=True)  #댓글 수정일
    author = models.ForeignKey(User, on_delete=models.CASCADE)  #외래키 - 댓글 글쓴이
    question = models.ForeignKey(Question, null=True, blank=True,
                                 on_delete=models.CASCADE) # 댓글이 달린 질문
    answer = models.ForeignKey(Answer, null=True, blank=True,
                               on_delete=models.CASCADE) # 댓글이 달린 답변

    def __str__(self):
        return self.content
