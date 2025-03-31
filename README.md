# Идентификация личности по отпечаткам пальцев рук при помощи фрактальной геометрии

## Описание проекта
Данный проект разрабатывается в рамках обучения в Санкт-Петербургском политехническом университете Петра Великого. Основная цель проекта — исследование и применение методов фрактальной геометрии для идентификации личности по отпечаткам пальцев. На первом этапе мы разрабатываем программный инструмент для сбора и обработки отпечатков пальцев с использованием сканера.

## Цели проекта
- Разработка системы сбора и хранения отпечатков пальцев.
- Анализ изображений отпечатков с использованием методов фрактальной геометрии.
- Создание алгоритма идентификации личности на основе полученных данных.

## Установка и настройка
### 1. Установка зависимостей
Для работы программы необходим Python 3. Убедитесь, что у вас установлены следующие зависимости:

```sh
pip install -r requirements.txt
```

Дополнительно необходимо подключить и настроить драйвера сканера отпечатков пальцев.

### 2. Запуск программы
Система сбора отпечатков запускается следующим образом:

```sh
python scan_fingerprints.py
```

После запуска программа начнет работу с подключенным сканером, отображая полученные отпечатки и сохраняя их в указанной директории.

## Структура проекта
```
├── assets/                             # Каталог для хранения изображений отпечатков
├── 1_fingerprint.ipynb                 # Пример снятия отпечатка
├── 2_fingerprints_processing.ipynb     # Скрипт по обработке сканов отпечатков
├── 3_fingerprint_identification.ipynb  # Подсчет погрешностей измерения и среднего значения
├── 4_fractal_dem.ipynb                 # Фрактальная размерность и метод квадратов
├── scan_fingerprints.py                # Основной скрипт сбора отпечатков пальцев
├── README.md                           # Описание проекта
```

## Дальнейшая работа
В ходе дальнейшей работы над проектом README будет дополняться примерами кода, алгоритмами обработки данных и выводами исследований.

