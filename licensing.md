# Лицензирование #

[в начало](README.md#навигация)

Обработка использует 3 режима: «**Демо**», «**Лицензия**» и «**Лицензия на ферму RDP-серверов**»

«**Демо**» - позволяет использовать полный функционал обработки, отличается от «Лицензия» и «Лицензия на ферму RDP-серверов» тем, что при печати присутствует задержка с информационным окном о том, что используется демоверсия, а также есть ограничение на количество операций для одного пользователя.

«**Лицензия**» - полноценная работа с обработкой без искусственных задержек и ограничений. Лицензия бессрочная, продлевать ее не нужно.

«**Лицензия на ферму RDP-серверов**» - полноценная лицензия, для частных случаев, когда работа происходит по RDP, однако при этом используется несколько компьютеров-серверов, и при переподключении пользователь может подключиться уже к другому компьютеру, например, такой функционал обычно используется для сервисов, что предоставляют 1с в аренду (1C fresh).

Для режимов «**Лицензия**» и «**Лицензия на ферму RDP-серверов**», необходимо приобрести лицензию на программу, и активировать ее по инструкции. Обратите внимание, 1 ключ может работать только на 1-м рабочем месте, если лицензию нужно переактивировать, то нужно вначале «Деактивировать» первую лицензию через меню обработки, а затем заново получить лицензию на другом рабочем месте.

**Возможные спорные ситуации:**

1. 1С находится на сервере, и пользователи подключаются к ней через установленную на своем компьютере 1С, необходимо приобрести столько лицензий сколько компьютеров использует обработку.

2. 1С находится на сервере, и пользователи подключаются к ней через RemoteAPP, тогда необходимо приобрести только 1 лицензию на сервер

3. 1С находится на сервере, и пользователи подключаются к ней через RDP, тогда необходимо приобрести только 1 лицензию на сервер

Видеоинструкция по активации лицензии: [Активация лицензии](https://www.youtube.com/watch?v=7v10ljuM3ag)

## Особенность получения обновлений и технической поддержки ##

Все обновления привязаны к технической поддержки пользователя. Обработка сверяет дату ее окончания, и, если версия не соответствует - переключает работу в демо-режим. Не стоит беспокоиться, что вы не сможете получить версию, которая вам доступна. Через форму обработки теперь можно получить все необходимые файлы для работы, при этом можно получить и доступные предыдущие версии.

Важно, все купленные лицензии закрепляются за тем email, что был указан при покупке, и потому техническая поддержка оказывается не на купленную лицензию, а на указанный email, поэтому при первоначальной покупки лицензии, техническая поддержка автоматически устанавливается на 2 месяца, однако если в последствии на этот email будут приобретать дополнительные лицензии, то техническая поддержка уже не будет продлена, и нужно приобретать позицию именно с технической поддержкой.

Дату окончания технической поддержки можно проверить через параметры обработки. Без технической поддержки консультации по программе не оказываются.

## Форма лицензирования ##

Доступ к форме лицензирования осуществляется через параметры обработки, раздел ["Ручное управление"](Описание%20параметров.md#ручное-управление) - **"Лицензирование"**, либо через форму первоначальной настройки, если ранее обработка не приобретелась.

![Форма лицензирования](media/0bb4b50404cdbd53ddc0d9654b11d042.png)

> Если лицензия была оплачена через сайт **"Инфостарт"**, то первоначально заказ нужно прикрепить к своей учетной записи, укажите в поле **Email** свою почту и нажмите **"Привязать к почте заказ Инфостарт"**, в открывшемся окне заполните **номер заказа**. Пароль для учетной записи запрашивается уже после привязки лицензии.

Для использования формы лицензирования необходимо вначале получить пароль для указанного email, для этого нажмите "Получить пароль", в течение 5-ти минут должен прийти пароль на указанную почту, если письма нет, то проверьте папку "СПАМ", скорее всего письмо попало туда. Пароль для указанной почты один и не меняется, даже если приобретено несколько лицензий.

Форма лицензирования позволяет:

- по кнопке **"Количество доступных лицензий"** - узнать, когда истекает техническая поддержка, сколько приобретено лицензий, и на каких компьютерах они активированы
  
  ![Количество доступных лицензий](media/08d6897e1cdcd4b40175d547142e01d8.png)

- по кнопке **"Деактивировать списком"**, можно выбрать нужные лицензии для деактивации, обратите внимание, что есть ограничение на количество деактиваций в день - оно равно количеству приобретенных лицензий.

   ![Деактивация](media/4f5a13860e9cacf6792c6227e165c324.png)

   Деактивация лицензии происходит, если нажать на имя соответствующего компьютера.

- по кнопке **"Сформировать файл технической поддержки"**, можно получить файл тех поддержки, который необходимо указать в [параметрах обработки](Описание%20параметров.md#основные-параметры) поле **"путь к файлу технической поддержки"**. Он необходим на случае, если не доступен интерент или есть периодические обрывы связи, для проверки, что данная версия обработки доступна для использования. Для формирования файла нужен доступ к интернету, он одинаков для всех лицензий активированных на одну учетную запись. После получения файла, его необходимо перенести на тот компьютер, где активирована лицензия.
- кнопки **"Сформировать файл активации"** и **"Получить ключ через файл активации"** используются, если на компьютере, где будет использована лицензия нет интернета. На том комьютере необходимо запустить обработки и в данном меню выбрать "Сформировать файл активации", обработка пропишет в файл информацию необходимую для активации через интернет, после необходимо взять этот файл и на компьютере, где есть интернет запустить также обработку и нажать "Получить ключ через файл активации" и указать сформированный файл - будет получен ключ для рабочего места без интернета. После останется только перенсти этот ключ на указанное рабочее место.
- кнопка "**Получить ключ**" - активирует лицензию для текущего рабочего места, и сохраняет ее в указанный каталог.
    >**Важно**: для использования, файл лицензии должен быть доступен, иначе программа будет считать, что ключ не активирован. На доступность может влиять права пользователя Windows на этот каталог, а также если файл лицензии заблокирован другим приложением
- кнопка "**Получить ключ для фермы RDP-серверов**" - формирует общий ключ для фермы RDP-серверов.
    >**Важно**: если используется ферма RDP-серверов, то доступ к интернету должен быть обязательно, если на сервере используется [прокси](Инструкция.md#подключение-через-прокси), то его нужно будет настроить в параметрах обработки, чтобы связь не обрывалась.

## Написать разработчику ##

Данная команда позволяет задать разработчику вопрос или отправить пожелание по разработке. Укажите вопрос, заполните email, и ранее полученный пароль после нажмите "Отправить", ответ придет на указанную почту.

![Письмо разработчику](media/письморазработчику.png)