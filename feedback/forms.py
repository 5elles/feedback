from django import forms


class FeedbackForm(forms.Form):
    name = forms.CharField(
        label="Имя",
        max_length=12,
        min_length=3,
        error_messages={
            'max_length': 'Символов должно быть меньше',
            'min_length': 'Символов должно быть больше',
            'required': 'Поле не может быть пустым',
        }
    )
    surname = forms.CharField(
        label="Фамилия",
        max_length=12,
        min_length=3,
        error_messages={
            'max_length': 'Символов должно быть меньше',
            'min_length': 'Символов должно быть больше',
            'required': 'Поле не может быть пустым',
        }
    )
    feedback = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 4, 'columns': 5}),
        label="Отзыв",
        max_length=120,
        min_length=3,
        error_messages={
            'max_length': 'Символов должно быть меньше',
            'min_length': 'Символов должно быть больше',
            'required': 'Поле не может быть пустым',
        }
    )


    # rating = forms.IntegerField(
    #     label="Рейтинг",
    #     max_value=100,
    #     min_value=0,
    #     error_messages={
    #         'max_value': 'Рейтинг должен быть в пределах от 0 до 100',
    #         'min_value': 'Рейтинг должен быть в пределах от 0 до 100',
    #         'required': 'Поле не может быть пустым',
    #     }
    # )