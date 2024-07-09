from django.shortcuts import render, redirect, get_object_or_404
from .models import TestPerson, NameSprav, Group, Test, Answer
from .consts import QUESTIONS_IN_TEST
import random


def homepage(request):
    return render(request, 'testing/homepage.html')


def login(request):
    if request.method == 'POST':
        log_test = request.POST['log_test']
        passw_test = request.POST['passw_test']
        fio = request.POST.get('FIO')
        phone = request.POST.get('phone')
        try:
            user = TestPerson.objects.get(
                log_test=log_test, passw_test=passw_test
            )
            request.session['user_id'] = user.test_person_id

            if fio:
                user.fio = fio
            if phone:
                user.phone = phone
            user.save()

            return redirect('testing:test_list')
        except TestPerson.DoesNotExist:
            return render(
                request, 'testing/login.html', {'error': 'Invalid credentials'}
            )

    return render(request, 'testing/login.html')


def test_list(request):
    if 'user_id' not in request.session:
        return redirect('testing:login')

    tests = NameSprav.objects.filter(is_active=True)
    return render(request, 'testing/test_list.html', {'tests': tests})


def start_test(request):
    if 'user_id' not in request.session:
        return redirect('testing:login')

    user_id = request.session['user_id']
    user = get_object_or_404(TestPerson, test_person_id=user_id)

    Test.objects.filter(test_person_id=user).delete()

    questions = list(Group.objects.filter(is_active=True))
    random_questions = []

    while len(random_questions) < QUESTIONS_IN_TEST and questions:
        question = random.choice(questions)
        answers = Answer.objects.filter(quest_id=question)
        if answers.exists():
            random_questions.append(question)
            questions.remove(question)

    for idx, question in enumerate(random_questions):
        answers = Answer.objects.filter(quest_id=question)
        for answer in answers:
            Test.objects.create(
                test_person_id=user,
                answer_id=answer,
                section_id=answer.section_id_id,
                quest_id=question.group_id,
                f_check=answer.f_check,
                f_answer=False,
                n_try=1,
                n_q=idx + 1,
            )

    return redirect('testing:question', pk=user.test_person_id)


def question_view(request, pk):
    user = get_object_or_404(TestPerson, test_person_id=pk)

    if request.method == 'POST':
        for key, value in request.POST.items():
            if key.startswith('answer_'):
                question_id = int(key.split('_')[1])
                selected_answer_id = int(value)

                test_instances = Test.objects.filter(
                    test_person_id=user, quest_id=question_id
                )
                for test_instance in test_instances:
                    test_instance.f_answer = (
                        test_instance.answer_id.answer_id == selected_answer_id
                    )
                    test_instance.save()
        total_questions = (
            Test.objects.filter(test_person_id=user)
            .values('quest_id')
            .distinct()
            .count()
        )
        correct_answers = (
            Test.objects.filter(
                test_person_id=user, f_check=True, f_answer=True
            )
            .values('quest_id')
            .distinct()
            .count()
        )
        user.result_person = correct_answers / total_questions * 100
        user.save()
        return redirect('testing:result', pk=user.test_person_id)

    unanswered_question_ids = (
        Test.objects.filter(test_person_id=user, f_answer=False)
        .values('quest_id')
        .distinct()
    )
    if not unanswered_question_ids.exists():
        return redirect('testing:result', pk=user.test_person_id)

    question_data = []
    for unanswered_question_id in unanswered_question_ids:
        question = Test.objects.filter(
            test_person_id=user, quest_id=unanswered_question_id['quest_id']
        ).first()
        answers = Answer.objects.filter(quest_id=question.quest_id)
        question_data.append({'question': question, 'answers': answers})

    return render(
        request,
        'testing/questions.html',
        {'question_data': question_data, 'test_person': user},
    )


def result(request, pk):
    user = get_object_or_404(TestPerson, test_person_id=pk)
    return render(request, 'testing/result.html', {'user': user})


def exit(request):
    return render(request, 'testing/exit.html')
