from django import forms
from board.models import Question, Answer

# 질문 등록 폼
class QuestionForm(forms.ModelForm):
    class Meta:   #내부 클래스
      model = Question
      fields = ['subject', 'content']
      labels = {
          'subject':'제목',
          'content':'내용'
      }

# 질문 등록 폼
class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['content']
        labels = {'content':'내용'}