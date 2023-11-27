## Установка (debain/ubuntu)
Установить интерпретатор prolog можно следующим образом:
  ```bash
sudo apt update
sudo apt install swi-prolog
```
## Запуск 
Для работы с нашей базой знаний из любой директории запустить интерпретатор в командной строке, далее загрузить нашу базу знаний
```bash
swipl

Welcome to SWI-Prolog (threaded, 64 bits, version 9.0.4)
SWI-Prolog comes with ABSOLUTELY NO WARRANTY. This is free software.
Please run ?- license. for legal details.

For online help and background, visit https://www.swi-prolog.org
For built-in help, use ?- help(Topic). or ?- apropos(Word).

?- consult('/home/valeriy-stepanenko/PycharmProjects/ITMO/CII/lab1/rules.pl').

```
