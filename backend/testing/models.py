from django.db import models


class TestPerson(models.Model):
    test_person_id = models.AutoField(primary_key=True)
    person_id = models.IntegerField(null=True)
    org_id = models.IntegerField()
    test_config_id = models.IntegerField()
    dt_test = models.DateTimeField('Дата прохождения теста', auto_now_add=True)
    person_org_id = models.IntegerField()
    result_person = models.FloatField(
        'Результат тестирования попытка 1', null=True
    )
    amount_time = models.FloatField('Среднее время', null=True)
    fio = models.CharField('ФИО тестируемого', max_length=255)
    is_delete = models.BooleanField(default=False, null=True)
    list_id = models.IntegerField()
    log_test = models.CharField('Логин для теста', max_length=15, null=True)
    passw_test = models.CharField(max_length=15, null=True)
    is_passed = models.PositiveSmallIntegerField(
        'Кол-во удачных прохождений теста', null=True, default=0
    )
    n_try = models.PositiveSmallIntegerField('Кол-во попыток', null=True)
    use_try = models.PositiveSmallIntegerField(
        'Кол-во использованых попыток', null=True
    )
    phone = models.CharField(
        'Номер телефона', max_length=63, null=True, default='0'
    )
    time_str = models.CharField(
        'Время тестирования попытка 1', max_length=31, null=True
    )
    time_str2 = models.CharField(
        'Время тестирования попытка 2', max_length=31, null=True
    )
    result_person2 = models.FloatField(
        'Результат тестирования попытка 2', null=True
    )
    n_break_quest = models.IntegerField(null=True)


class Test(models.Model):
    test_id = models.AutoField(primary_key=True)
    test_person_id = models.ForeignKey(TestPerson, on_delete=models.CASCADE)
    answer_id = models.ForeignKey('Answer', on_delete=models.CASCADE)
    section_id = models.IntegerField('Группа вопросов')
    quest_id = models.IntegerField('Вопрос')
    f_check = models.BooleanField('Правильный ли ответ', null=True)
    f_answer = models.BooleanField('Ответ тестируемого', default=False)
    n_try = models.PositiveSmallIntegerField('Номер попытки')
    n_q = models.IntegerField('Номер вопроса в тесте', null=True)


class Answer(models.Model):
    answer_id = models.AutoField(primary_key=True)
    section_id = models.ForeignKey(
        'Group',
        on_delete=models.CASCADE,
        verbose_name='Группа вопросов',
        related_name='answer_groups',
    )
    quest_id = models.ForeignKey(
        'Group',
        on_delete=models.CASCADE,
        verbose_name='Вопрос',
        related_name='answers',
    )
    answer_name = models.CharField('Текст варианта ответа', max_length=255)
    answer_cod = models.CharField(
        'Номер варианта ответа', max_length=50, null=True
    )
    f_check = models.BooleanField('Правильный ли ответ', null=True)


class Group(models.Model):
    group_id = models.AutoField(primary_key=True)
    group_name = models.CharField(
        'Название группы или текст вопроса', max_length=1024
    )
    parent_id = models.IntegerField('Группа вопросов', null=True)
    app = models.CharField(max_length=255, null=True)
    sort_code = models.IntegerField(null=True)
    is_active = models.BooleanField(default=False)
    type_id = models.IntegerField(null=True)
    amount = models.IntegerField(null=True)
    img = models.ImageField('Изображение', upload_to='images/', null=True)
    theme_id = models.ForeignKey('Theme', on_delete=models.SET_NULL, null=True)


class Theme(models.Model):
    theme_id = models.AutoField(primary_key=True)
    group_id = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True)
    theme_name = models.CharField('Название темы', max_length=255)


class NameSprav(models.Model):
    item_id = models.AutoField(primary_key=True)
    sprav_id = models.SmallIntegerField(default=4)
    item_cod = models.PositiveSmallIntegerField('Номер теста в списке тестов')
    item_name = models.CharField('Название теста', max_length=255)
    item_name_cod = models.CharField(
        'Кол-во вопросов в тесте', max_length=255, null=True
    )
    is_change = models.BooleanField(default=False, null=True)
    is_active = models.BooleanField(default=False, null=True)
