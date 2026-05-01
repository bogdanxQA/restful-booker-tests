# API тестирование Restful-Booker

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![pytest](https://img.shields.io/badge/pytest-8.2.0-blue?logo=pytest)
![Allure Report](https://img.shields.io/badge/Allure_Report-2.29.0-blue?logo=allure)
![Requests](https://img.shields.io/badge/requests-2.31.0-blue?logo=python)
![Pydantic](https://img.shields.io/badge/pydantic-2.5.0-blue?logo=pydantic)

Проект по автоматизации тестирования API сервиса [Restful-Booker](https://restful-booker.herokuapp.com/).  
Набор позитивных и негативных тестов, написанных на Python с использованием **pytest**, **requests**, **Pydantic** и **Allure**.

---

## 📋 О проекте

Этот проект — мой **промежуточный этап** в изучении автоматизации тестирования API. Здесь я применяю полученные знания на практике, поэтому код и архитектура могут быть далеко не идеальными.  

**Общее количество тестов:** 35

**Allure‑отчёт** автоматически генерируется через **GitHub Actions** и доступен на **GitHub Pages**:  
[**Посмотреть свежий отчёт Allure**](https://bogdanxqa.github.io/restful-booker-tests/)

**Что реализовано:**

- Полный CRUD-цикл: создание, чтение, обновление, удаление бронирований.
- Позитивные и негативные тестовые сценарии.
- Валидация JSON-схем ответов через Pydantic.
- Минимальное логирование HTTP-запросов и ответов (в консоль и файл).
- Генерация отчётов Allure.

> **ℹ️ Некоторые тесты могут падать**: это связано с неполной / противоречивой документацией API (например, в документации указан статус 200, а по факту возвращается 201). Подобные расхождения намеренно мною оставлены для наглядности.

## Примечания

- Тесты используют реальный API `https://restful-booker.herokuapp.com/`, который сбрасывается каждые 10 минут.
- Для защищённых запросов (создание, обновление, удаление) требуется аутентификация. Токен генерируется автоматически перед выполнением тестов.
- Логи запросов и ответов сохраняются в папку `logs/` и дублируются в консоль при запуске с флагом `-s`.

## ⚙️ CI/CD (GitHub Actions)

- **Триггер:** только ручной запуск (workflow_dispatch).
- **Что делает:** прогоняет все тесты, генерирует Allure-отчёт и автоматически публикует его на GitHub Pages.

---

## Используемые технологии

| Инструмент | Назначение |
|------------|------------|
| Python 3.11 | Язык программирования |
| pytest | Фреймворк для запуска тестов |
| requests | HTTP-клиент для отправки запросов к API |
| Pydantic | Валидация и парсинг JSON-ответов |
| Allure | Формирование наглядных отчётов о тестировании |
| logging | Логирование действий в консоль и файл |

---

## 📁 Структура проекта

```text
restful-booker-tests/
├── common/
│   └── api/                # HTTP-клиент и методы API
│       ├── client.py
│       ├── auth_api.py
│       └── booking_api.py
├── models/                 # Pydantic-модели для валидации
│   ├── main.py
│   └── types.py
├── data/                   # Тестовые данные (JSON)
│   └── booking_payloads.json
├── tests/                  # Тесты и фикстуры
│   ├── conftest.py
│   ├── test_booking.py
│   └── test_negative.py
├── utils/                  # Утилиты
│   ├── checks.py
│   └── logger.py
├── logs/                   # Логи (создаются при запуске)
├── .github/workflows/      # CI/CD конфигурация
├── requirements.txt
└── README.md
```

## Запуск тестов

### 1. Клонируйте репозиторий

```bash
git clone https://github.com/bogdanxQA/restful-booker-tests.git
cd restful-booker-tests
```

---

### 2. Создайте и активируйте виртуальное окружение

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**macOS / Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 3. Установите зависимости

```bash
pip install -r requirements.txt
```

---

### 4. Запустите тесты

```bash
pytest -v
```

---

### 5. Сформируйте Allure-отчёт

Установите Allure (требуется Java):

```bash
# Windows (через Scoop)
scoop install allure

# macOS
brew install allure
```

Запустите тесты с сохранением результатов:

```bash
pytest --alluredir=allure-results
```

Сформируйте и откройте отчёт:

```bash
allure serve allure-results
```

---

