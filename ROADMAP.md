# Book Library API — Roadmap

Полный план обучения Django REST Framework на примере проекта Book Library API.

---

## Пройденные шаги

- [x] **Step 1 — Project Setup** — установлены Django + DRF, создано приложение `books`, настроен `INSTALLED_APPS`
- [x] **Step 2 — Models** — модели `Category`, `Author`, `Book` с полями и связями
- [x] **Step 3 — Migrations** — начальная миграция + добавление поля `price`
- [x] **Step 4 — Serializers** — `ModelSerializer` для всех 3 моделей; вложенное чтение + write-only PK поля в `BookSerializer`
- [x] **Step 5 — ViewSets** — `ModelViewSet` для `Category`, `Author`, `Book`
- [x] **Step 6 — Router & URLs** — `DefaultRouter` регистрирует все 3 viewset'а под `/api/`
- [x] **Step 7 — Permissions** — `IsAuthenticatedOrReadOnly` на всех viewset'ах
- [x] **Step 8 — JWT Authentication** — `djangorestframework-simplejwt`, эндпоинты `/api/token/` и `/api/token/refresh/`
- [x] **Step 9 — Filtering** — `DjangoFilterBackend` + `filterset_fields` (`category`, `author`)
- [x] **Step 10 — Search** — `SearchFilter` (`title`, `description`)
- [x] **Step 11 — Ordering** — `OrderingFilter` (`price`)
- [x] **Step 12 — Pagination** — `LimitOffsetPagination`, `PAGE_SIZE = 10`
- [x] **Step 13 — Serializer Validation** — `validate_bio` (мин. 20 символов), `validate_published_date` (без будущих дат)
- [x] **Step 14 — Image Upload** — `Pillow`, `ImageField` на `Author.photo` и `Book.cover_image`
- [x] **Step 15 — Testing** — `AuthorAPITest` и `BookAPITest` в `books/tests.py` (CRUD, permissions, search, filter, ordering)

---

## Следующие шаги

- [x] **Step 16 — API Documentation** — подключён `drf-spectacular`; Swagger UI на `/api/docs/`, Redoc на `/api/redoc/`, схема на `/api/schema/`
- [x] **Step 17 — Custom Permissions** — `IsOwnerOrReadOnly` в `books/permissions.py`; поле `Book.created_by`, `perform_create()` проставляет владельца, проверено через Swagger (owner → 200, чужой → 403)
- [x] **Step 18 — Throttling** — `AnonRateThrottle` (5/min) и `UserRateThrottle` (20/min) в `settings.py`; превышение лимита → 429 Too Many Requests
- [x] **Step 19 — Caching** — `LocMemCache` в `settings.py`; `GET /api/books/` кэшируется на 60 сек через `@method_decorator(cache_page(60))` на методе `list` (повторные запросы ~8x быстрее)
- [x] **Step 20 — Signals** — `books/signals.py` подключён через `apps.py ready()`; `pre_save` авто-генерирует `slug` для `Category` (slugify), `post_save`/`post_delete` сбрасывают кэш книг (`cache.clear()`)
- [x] **Step 21 — Nested write** — `author` стал writable nested в `BookSerializer`; переопределён `create()` с `get_or_create` — книга создаётся вместе с новым автором за один запрос (без дублей)
- [x] **Step 22 — Soft delete** — поле `Book.is_deleted` (default=False); `perform_destroy()` ставит флаг вместо удаления, `queryset` фильтрует `is_deleted=False` (DELETE → 204, книга остаётся в базе)
- [x] **Step 23 — Celery** — `config/celery.py` + Redis-брокер; задача `send_book_notification` в `books/tasks.py`, вызывается через `.delay()` из сигнала `post_save` (created); worker выполняет её в фоне, не блокируя ответ API
- [ ] **Step 24 — CI/CD** — GitHub Actions: автоматический запуск `python manage.py test` на каждый push
- [ ] **Step 25 — Dockerize** — `Dockerfile` + `docker-compose.yml` для Django + Postgres
- [ ] **Step 26 — Deployment** — выложить проект на Render/Railway/Fly.io

---

## Как пользоваться этим файлом

Отмечай `[ ]` → `[x]` по мере прохождения каждого шага.
