Для додавання тесту потрібно перейти за посиланням `/test/` та ввести щось на кшталп цього:
```
{
 "author": 1,     // id користувача
 "name": "zxcv"   // ім'я тесту
}
```
Щоб додати питання є посилання `/test/question/` та ввести:
```
{
 "test": 1,        // id тесту створиного вище
 "text": "test"    // текст питання
}
```
Додавання питань відбувається за писиланням `/test/answer/`:
```
[{                    // квадратні дужки тут потрібні для того, щоб надсилати одразу багато відповідей
 "question": 1,       // id тесту
 "text": "калясік",   // текст питання
 "is_true": true      // це поле вказує на те що ця відповідь правильна(не обов'язкове поле, якщо воно не введене буде false)
},
{
 "question": 1,
 "text": "дурень",
 "is_true": false
}]
```
Абсолютно всі відомості, що до тестів відображаються в `/test/`

First, install the necessary modules `pip install -r requirements.txt`

Start `cmd` and write `python manage.py runserver`

This is not a full-fledged site, it is just a backend for a React site.
