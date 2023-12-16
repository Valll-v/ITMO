# coding: utf-8
import re


def serialize_answers(answers):
    result = set()
    for answer in answers:
        answer = tuple(sorted(answer.values()))
        if answer not in result and '_' not in answer:
            result.add(answer)
    return result


def my_hero_choise(info):
    if info[0]:
        print('У вас уже выбран герой.')
        return None
    elif len(info[1]) >= 3:
        print('Ваша команда полная. Вы не можете выбрать себе героя.')
        return None
    match len(info[1]):
        case 0:
            return 'perfect_team(X,Y,Z)'
        case 1:
            return f'perfect_team(X,Y,{info[1][0]})'
        case 2:
            return f'perfect_team(X,{info[1][1]},{info[1][0]})'


def my_team_hero_choise(info):
    if not info[0]:
        print('Сначала выберите героя.')
        return None
    elif len(info[1]) >= 3:
        print('Ваша команда полная.')
        return None
    match len(info[1]):
        case 0:
            return f'perfect_team({info[0][0]},Y,Z)'
        case 1:
            return f'perfect_team({info[0][0]},Y,{info[1][0]})'


def my_item_choice(info):
    if not info[0]:
        print('Сначала выберите героя.')
        return None
    elif len(info[2]) >= 6:
        print('Ваш инвентарь полон.')
        return None
    main = f'good_for_hero({info[0][-1]},Y)'
    for item in info[2]:
        main = main + f',not(Y = {item})'
    return main


examples = [
    r'Я играю на slark',
    r'У меня в команде есть cristal_maiden',
    r'Я купил bloodstone',
]


init_patterns = [
    r'Я играю на (.+)',
    r'У меня в команде есть (.+)',
    r'Я купил (.+)',
]


questions = {
    'Кого мне пикнуть?': my_hero_choise,
    'Что мне купить?': my_item_choice,
    'Кого пикнуть моей команде?': my_team_hero_choise,
}


def update_info(string: str, info: list[list]):
    for i, pattern in enumerate(init_patterns):
        match = re.match(pattern, string, re.IGNORECASE)
        if match is not None:
            info[i].append(match.groups()[0])
            return info
    print('Неизвестный тип информации. Попробуйте другой.')
    return info


def form_query(string, info):
    if string in questions:
        return questions[string](info)
    print('Неверный выбор вопроса')
    return None
