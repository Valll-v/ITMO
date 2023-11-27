/* Классы */
INSERT INTO class VALUES (DEFAULT, 'Доктор', 'Производят работу');
INSERT INTO class VALUES (DEFAULT, 'Преподаватель', 'Производят работу');
INSERT INTO class VALUES (DEFAULT, 'Студентота', 'Болванят');

/* Люди */
INSERT INTO person VALUES (DEFAULT, 'имя', 'Чандрасекарампилай');
INSERT INTO person VALUES (DEFAULT, 'имя', 'Терновский');
INSERT INTO person VALUES (DEFAULT, 'Николаев', 'Владимир');
INSERT INTO person VALUES (DEFAULT, 'Валерий', 'Степаненко');

/* Предметы */
INSERT INTO item VALUES (DEFAULT, 'Компьютер', '', TRUE);
INSERT INTO item VALUES (DEFAULT, 'Блок', 'Хранят данные', TRUE);
INSERT INTO item VALUES (DEFAULT, 'Ноутбук', 'Валерин', TRUE);
INSERT INTO item VALUES (DEFAULT, 'Мышка', 'Компьютерная', TRUE);
INSERT INTO item VALUES (DEFAULT, 'Сервера Valve', 'Почините их кто-нибудь', FALSE);

/* Отчеты */
INSERT INTO report VALUES (DEFAULT, 'Предварительное обследование ЭАЛа');
INSERT INTO report VALUES (DEFAULT, 'Отчет по лабораторной работе N%1');

/* Действия */
INSERT INTO action VALUES (DEFAULT, 1, 'Провел Обследование', 'Было закончено предварительно обследование ЭАЛа', 1);
INSERT INTO action VALUES (DEFAULT, 1, 'Восстановил', 'В рамках обследования восстановил все блоки', 1);
INSERT INTO action VALUES (DEFAULT, 4, 'Программирует', 'Валера жестко программирует SQL скрипты', 2);
INSERT INTO action VALUES (DEFAULT, 4, 'Подключается', 'Валера после лаб хочет плотно отдохнуть, но сервера валв заглохли');
INSERT INTO action VALUES (DEFAULT, 3, 'Проверяет', 'В рамках предмета ИСБД идет проверка лаб студентов', 2);

/* Добавим людям классы */
INSERT INTO person_class VALUES (1, 1); /* Чандрасекарампилай - доктор */
INSERT INTO person_class VALUES (2, 1); /* Терновский - доктор */
INSERT INTO person_class VALUES (3, 1); /* Владимир Вячеславович - доктор */
INSERT INTO person_class VALUES (3, 2); /* Владимир Вячеславович - преподаватель */
INSERT INTO person_class VALUES (4, 3); /* Степаненко Валерий - Студент */

/* Добавим людям классы */
INSERT INTO action_item VALUES (2, 1); /* Восстановление блоков затронуло блоки */
INSERT INTO action_item VALUES (2, 2); /* Восстановление блоков затронуло компьютер */
INSERT INTO action_item VALUES (3, 3); /* Программирование затрагивает ноутбук */
INSERT INTO action_item VALUES (3, 4); /* Программирование затрагивает мышь */
INSERT INTO action_item VALUES (4, 5); /* Подключение затрагивает сервера */
INSERT INTO action_item VALUES (5, 3); /* Проверка лабы затрагивает ноутбук */

/* Свяжем отчеты с авторами */
INSERT INTO person_report VALUES (1, 1); /* Восстановление блоков затронуло блоки */
INSERT INTO person_report VALUES (2, 1); /* Восстановление блоков затронуло компьютер */
INSERT INTO person_report VALUES (4, 2); /* Программирование затрагивает ноутбук */
