from django import forms

from .models import Feedback


class FeedbackForm(forms.ModelForm):
    SATISFACTION = (
        ('EXCELLENT', 'EXCELLENT'),
        ('GOOD', 'GOOD'),
        ('BAD', 'BAD'),
        ('WORST', 'WORST')
    )
    AUDIBILTY = (
        ('EXCELLENT', 'EXCELLENT'),
        ('GOOD', 'GOOD'),
        ('BAD', 'BAD'),
        ('WORST', 'WORST')
    )
    SUBJECT_CLARITY = (
        ('EXCELLENT', 'EXCELLENT'),
        ('GOOD', 'GOOD'),
        ('BAD', 'BAD'),
        ('WORST', 'WORST')
    )
    ANY_PARTIALITY = (
        ('NO PARTIALITY', 'NO PARTIALITY'),
        ('SOMETIMES', 'SOMETIMES'),
        ('ALL THE TIME', 'ALL THE TIME')
    )
    HOMEWORK = (
        ('NO HOMEWORKS', 'NO HOMEWORKS'),
        ('SOMETIMES', 'SOMETIMES'),
        ('REGULARLY', 'REGULARLY')
    )
    PUNCTUALITY = (
        ('NEVER LATE', 'NEVER LATE'),
        ('OCCASIONALLY LATE', 'OCCASIONALLY LATE'),
        ('ALWAYS LATE', 'ALWAYS LATE')
    )
    ANOTHER_CLASS = (
        ('YES', 'YES'),
        ('NO', 'NO')
    )
    satisfied = forms.ChoiceField(
        choices=SATISFACTION, widget=forms.RadioSelect())
    audibility = forms.ChoiceField(
        choices=AUDIBILTY, widget=forms.RadioSelect())
    clarity = forms.ChoiceField(
        choices=SUBJECT_CLARITY, widget=forms.RadioSelect())
    partiality = forms.ChoiceField(
        choices=ANY_PARTIALITY, widget=forms.RadioSelect())
    homework = forms.ChoiceField(
        choices=HOMEWORK, widget=forms.RadioSelect())
    punctuality = forms.ChoiceField(
        choices=PUNCTUALITY, widget=forms.RadioSelect())
    another_class = forms.ChoiceField(
        choices=ANOTHER_CLASS, widget=forms.RadioSelect())

    class Meta:
        model = Feedback
        fields = (
            'satisfied',
            'audibility',
            'clarity',
            'partiality',
            'homework',
            'punctuality',
            'another_class',

        )
