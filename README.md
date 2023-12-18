[![Release](https://img.shields.io/github/tag/andrei-karpov/1c_kkt_54fz.svg?label=Last%20release&a)](https://github.com/andrei-karpov/1c_kkt_54fz/releases)

# ККТ-ОНЛАЙН 54ФЗ: «Обработка для работы фискальных регистраторов» #

В разделе [issues](https://github.com/andrei-karpov/1c_kkt_54fz/issues), можно добавить свои пожелания или задать вопросы по работе программы.

## Что умеет ##

- Поддерживает [несколько систем налогообложения](docs/mechanism_distribution.md#распределение-по-системам-налогообложения) в одном документе 1С
- Можно использовать один фискальный регистратор с разных рабочих мест.
- Поддерживает последние изменения по 54 ФЗ, форматы обмена: ФФД **1.05**, **1.1** и **1.2**
- Можно использовать в составе отраслевых конфигураций: [**Рарус: Альфа-Авто, Далион**](docs/connecting.md#особенность-подключения-рарус)
- Можно использовать там, где нет функционала по работе [с торговым оборудованием.](docs/instruction.md#форма-отладки)
- Поддерживает собственный [шаблон чека](docs/template_document.md#шаблон-документа-печати) для вывода рекламной или иной информации
- Можно разбить один чек сразу на [несколько ККТ](docs/connecting.md#подключение-дополнительного-оборудования), например, алкоголь по одной кассе, а кухню по другой
- Можно изменить программу по-желанию, для этого есть дополнительно [подключаемая библиотека](docs/for_programmers.md#изменение-функционала-под-себя).
- Можно дополнительно [печатать «копию» чека](docs/instruction.md#печать-копии-чека) на обычном принтере.
- Перед фискальной печатью можно дополнительно сформировать предварительный чек, где будут выведены все нужные реквизиты для проверки
- Можно сформировать [чек коррекции](docs/form_check_and_check_correction.md#чек-коррекции) средствами обработки, либо на основании типового документа
- Использует собственную форму «Рабочего места кассира» ([Форма проверки печати](docs/form_check_and_check_correction.md))
- Поддержка печати чеков с детализацией номенклатуры по кассовым документам(Приходный кассовый ордер, Расходный кассовый ордер, Платежное поручение входящее и т.д)
- Отдельно можно использовать Эмулятор оборудования ККТ
- Позволяет [отправить электронный чек](docs/management_distribution.md) средствами 1С по почте или в виде SMS
- Работает на платформах 1С [8.1](docs/connecting.md#особенность-подключения-81), 8.2 и 8.3
- Работает на операционных системах **Windows** и [**Linux**](docs/connecting.md#особенность-подключения-linux)
- Поддерживает [**ФФД 1.2**](docs/marking.md#поддержка-ффд-12)

## Навигация ##

- [**Подключение обработки, и все с этим связанное**](docs/connecting.md)
  - [Компоненты оборудования](docs/connecting.md#компоненты-оборудования)
  - [Особенность подключения 8.1](docs/connecting.md#особенность-подключения-81)
  - [Особенность подключения LINUX](docs/connecting.md#особенность-подключения-linux)
  - [Особенность подключения Рарус](docs/connecting.md#особенность-подключения-рарус)
  - [Особенность подключения Далион](docs/connecting.md#особенность-подключения-далион)
  - [Особенность подключения УТ 10.2](docs/connecting.md#особенность-подключения-ут-102)
  - [Структура архива с обработкой](docs/connecting.md#структура-архива-с-обработкой)
  - [Как обновить ранее приобретенную программу?](docs/connecting.md#как-обновить-ранее-приобретенную-программу)
  - [Подключение эквайринговых терминалов](docs/connecting.md#подключение-эквайринговых-терминалов)
  - [Подключение дополнительного оборудования](docs/connecting.md#подключение-дополнительного-оборудования)
- [**Описание параметров программы**](docs/parameters_description.md)
  - [Основные параметры](docs/parameters_description.md#основные-параметры)
  - [Дополнительные параметры](docs/parameters_description.md#дополнительные-параметры)
  - [ЕНВД, УСН, Нефискальные чеки](docs/parameters_description.md#енвд-усн-нефискальные-чеки)
  - [Параметры драйвера](docs/parameters_description.md#параметры-драйвера)
  - [Параметры документов](docs/parameters_description.md#параметры-документов)
  - [Параметры для ФФД](docs/parameters_description.md#параметры-для-ффд)
  - [Маркировка](docs/parameters_description.md#маркировка)
  - [Служебное](docs/parameters_description.md#служебное)
  - [Ручное управление](docs/parameters_description.md#ручное-управление)
- [**Лицензирование. Особенности покупки**](docs/licensing.md)
  - [Форма лицензирования](docs/licensing.md#форма-лицензирования)
  - [Особенность получения обновлений и технической поддержки](docs/licensing.md#особенность-получения-обновлений-и-технической-поддержки)
  - [Написать разработчику](docs/licensing.md#написать-разработчику)
  - [Как записать лог для технической поддержки?](docs/licensing.md#как-записать-лог-для-технической-поддержки)
  - [Особенность активации Инфостарт](docs/licensing.md#особенность-активации-инфостарт)
- [**Маркировка. Продажа лекарств, шин, обуви и т.д.**](docs/marking.md)
  - [Настройка типов маркировки](docs/marking.md#настройка-типов-маркировки)
  - [Продажа лекарств](docs/marking.md#продажа-лекарств)
  - [Отражение продаж индивидуальных средства защиты](docs/marking.md#отражение-продаж-индивидуальных-средства-защиты)
  - [Как продавать маркированный товар через обработку](docs/marking.md#как-продавать-маркированный-товар-через-обработку)
- [**Дополнительная функциональность**](docs/instruction.md)
  - [Особенность пробития авансовых чеков и установки признаков способа расчета](docs/instruction.md#особенность-пробития-авансовых-чеков-и-установки-признаков-способа-расчета)
  - [Печать копии чека](docs/instruction.md#печать-копии-чека)
  - [Подключение через прокси](docs/instruction.md#подключение-через-прокси)
  - [Редактор произвольного кода](docs/instruction.md#редактор-произвольного-кода)
  - [Форма отладки](docs/instruction.md#форма-отладки)
  - [Отключение печати бумажных чеков](docs/instruction.md#отключение-печати-бумажного-чека)
- [**Рассылка чеков средствами обработки**](docs/management_distribution.md)
  - [Рассылка чеков по SMS](docs/management_distribution.md#рассылка-чеков-по-sms)
  - [Рассылка чеков средствами 1С по Email](docs/management_distribution.md#рассылка-чеков-средствами-1с-по-email)
  - [Форма ввода Email и Номера телефона](docs/management_distribution.md#форма-ввода-email-и-номера-телефона)
- [**Шаблон чека**](docs/template_document.md)
- [**Форма проверки печати и чек коррекции**](docs/form_check_and_check_correction.md)
  - [Настройка открытия формы проверки печати](docs/form_check_and_check_correction.md#настройка-открытия-формы-проверки-печати)
  - [Настройка формы проверки печати](docs/form_check_and_check_correction.md#настройка-формы-проверки-печати)
  - [Чек коррекции](docs/form_check_and_check_correction.md#чек-коррекции)
- [**Механизм распределения. Как задать условия применения параметров программы.**](docs/mechanism_distribution.md)
  - [Условия распределения](docs/mechanism_distribution.md#условия-распределения)
  - [Распределение по системам налогообложения](docs/mechanism_distribution.md#распределение-по-системам-налогообложения)
  - [Распределение по номерам секций](docs/mechanism_distribution.md#распределение-по-номерам-секций)
  - [Распределение по договорам Агента](docs/mechanism_distribution.md#распределение-по-договорам-агента)
  - [Настройка признаков предмета расчета](docs/mechanism_distribution.md#настройка-признаков-предмета-расчета)
  - [Настройка признаков способа расчета](docs/mechanism_distribution.md#настройка-признаков-способа-расчета)
  - [Настройка поставщика агента](docs/mechanism_distribution.md#настройка-поставщика-агента)
  - [Настройка печати реквизитов ГТД и Страна](docs/mechanism_distribution.md#настройка-печати-реквизитов-гтд-и-страна)
  - [Настройка печати получателя и его ИНН](docs/mechanism_distribution.md#настройка-печати-получателя-и-его-инн)
  - [Настройка ограничения времени продажи](docs/mechanism_distribution.md#настройка-ограничения-времени-продажи)
  - [Настройка ставки НДС по умолчанию](docs/mechanism_distribution.md#настройка-ставки-ндс-по-умолчанию)
  - [Подмена номенклатуры](docs/mechanism_distribution.md#подмена-номенклатуры)
- [**Для программистов**](docs/for_programmers.md)
  - [Доработка конфигурации](docs/for_programmers.md#доработка-конфигурации)
  - [Дополнительные параметры](docs/for_programmers.md#дополнительные-параметры)
  - [Изменение функционала "под себя"](docs/for_programmers.md#изменение-функционала-под-себя)
- [**Подключение Рарус**](docs/rarus_connecting.md)
  - [Изменение конфигурации](docs/rarus_connecting.md#изменение-конфигурации)
  - [Подключение оборудования](docs/rarus_connecting.md#подключение-оборудования)
- [**Список используемых компонент**](docs/components.md)
  - [Компоненты Windows](docs/components.md#компоненты-ккт-для-windows)
  - [Компоненты Linux](docs/components.md#компоненты-ккт-для-linux)
- [**Полезные ссылки**](docs/useful_links.md)
- [**Возможные ошибки**](docs/errors.md)
