# Book Library API

A RESTful API for managing books, authors, and categories — built with Django REST Framework.

---

## Learning Roadmap

- [x] **Step 1 — Project Setup** — Django + DRF installed, `books` app created, `INSTALLED_APPS` configured
- [x] **Step 2 — Models** — `Category`, `Author`, `Book` models with proper fields and relationships
- [x] **Step 3 — Migrations** — Initial migration + `price` field added in second migration
- [x] **Step 4 — Serializers** — `ModelSerializer` for all 3 models; nested read + write-only PK fields on `BookSerializer`
- [x] **Step 5 — ViewSets** — `ModelViewSet` for `Category`, `Author`, `Book`
- [x] **Step 6 — Router & URLs** — `DefaultRouter` registers all 3 viewsets under `/api/`
- [x] **Step 7 — Permissions** — `IsAuthenticatedOrReadOnly` on all viewsets (read = public, write = login required)
- [x] **Step 8 — JWT Authentication** — `djangorestframework-simplejwt` installed; `/api/token/` and `/api/token/refresh/` endpoints
- [x] **Step 9 — Filtering** — `DjangoFilterBackend` + `filterset_fields` on `BookViewSet` (`category`, `author`)
- [x] **Step 10 — Search** — `SearchFilter` on `BookViewSet` (`title`, `description`)
- [x] **Step 11 — Ordering** — `OrderingFilter` on `BookViewSet` (`price`)
- [x] **Step 12 — Pagination** — `LimitOffsetPagination` globally in `settings.py`, `PAGE_SIZE = 10`
- [x] **Step 13 — Serializer Validation** — `validate_bio` (min 20 chars) on `AuthorSerializer`; `validate_published_date` (no future dates) on `BookSerializer`
- [x] **Step 14 — Image Upload** — `Pillow` installed; `ImageField` on `Author.photo` and `Book.cover_image`
- [x] **Step 15 — Testing** — `AuthorAPITest` (list, auth-required create, invalid bio validation) and `BookAPITest` (list, search, filter by author, ordering by price) in `books/tests.py`

---

## API Endpoints

| Method | URL | Description | Auth required |
|--------|-----|-------------|---------------|
| GET | `/api/books/` | List all books | No |
| POST | `/api/books/` | Create a book | Yes |
| GET | `/api/books/{id}/` | Get a book | No |
| PUT/PATCH | `/api/books/{id}/` | Update a book | Yes |
| DELETE | `/api/books/{id}/` | Delete a book | Yes |
| GET | `/api/authors/` | List all authors | No |
| POST | `/api/authors/` | Create an author | Yes |
| GET | `/api/categories/` | List all categories | No |
| POST | `/api/categories/` | Create a category | Yes |
| POST | `/api/token/` | Obtain JWT token | No |
| POST | `/api/token/refresh/` | Refresh JWT token | No |

### Query Parameters (Books)

| Parameter | Example | Description |
|-----------|---------|-------------|
| `search` | `?search=django` | Search by title or description |
| `ordering` | `?ordering=price` or `?ordering=-price` | Sort by price |
| `category` | `?category=1` | Filter by category ID |
| `author` | `?author=2` | Filter by author ID |
| `limit` | `?limit=5&offset=10` | Pagination |

---

## Tech Stack

- Python 3.14
- Django 6.0
- Django REST Framework 3.17
- djangorestframework-simplejwt 5.5
- django-filter
- Pillow 12.2
