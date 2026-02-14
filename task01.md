# Task 1: Book Class

## Umumiy Tavsif
Kutubxona tizimi uchun `Book` klassini yarating. Bu klass kitob haqida ma'lumotlarni saqlaydi va kitoblarni boshqarish operatsiyalarini amalga oshiradi.

---

## 1. Constructor

```python
Book(id: int, title: str, author: str, pages: int)
```

### Validatsiya
Quyidagi qoidalar buzilsa `ValueError` ko'tarilishi kerak:

- `id` - musbat butun son bo'lishi shart
- `title` - bo'sh string bo'lmasligi kerak
- `author` - bo'sh string bo'lmasligi kerak  
- `pages` - 0 dan katta bo'lishi shart

---

## 2. Attributelar

| Nomi | Turi | Boshlang'ich qiymat | Tavsif |
|------|------|---------------------|--------|
| `id` | int | constructordan | Kitobning unikal ID raqami |
| `title` | str | constructordan | Kitob nomi |
| `author` | str | constructordan | Muallif ismi |
| `pages` | int | constructordan | Sahifalar soni |
| `is_borrowed` | bool | `False` | Kitob olinganmi? |
| `borrower` | str \| None | `None` | Kim olgan (ism) |
| `borrow_history` | list[tuple[str, datetime]] | `[]` | Kimlar olgan va qachon |
| `archived` | bool | `False` | Arxivlanganmi? |

---

## 3. Metodlar

### `borrow(user: str) -> None`
Kitobni foydalanuvchiga beradi.

**Bajarilishi:**
1. Agar kitob `archived` bo'lsa → `RuntimeError` ko'tarish
2. Agar kitob allaqachon olingan bo'lsa (`is_borrowed == True`) → `RuntimeError` ko'tarish
3. `is_borrowed = True` qilish
4. `borrower = user` qilish
5. `borrow_history` ga `(user, datetime.now())` qo'shish

---

### `return_book() -> None`
Olingan kitobni qaytaradi.

**Qoidalar:**
- Agar kitob olinmagan bo'lsa (`is_borrowed == False`) → `RuntimeError` ko'tarish
- `borrower = None` qilish
- `is_borrowed = False` qilish

---

### `change_title(new_title: str) -> None`
Kitob nomini o'zgartiradi.

**Qoidalar:**
- `new_title` bo'sh bo'lmasligi kerak → `ValueError`
- Agar kitob `archived` bo'lsa → `RuntimeError` ko'tarish

---

### `archive() -> None`
Kitobni arxivlaydi (mantiqiy o'chirish).

**Qoidalar:**
- Agar kitob hozir kimgadir olingan bo'lsa → `RuntimeError` ko'tarish
- `archived = True` qilish

---

### `info() -> dict`
Kitob haqida to'liq ma'lumot qaytaradi.

**Qaytarish formati:**
```python
{
    "id": int,
    "title": str, 
    "author": str,
    "pages": int,
    "status": str,  # "available" | "borrowed" | "archived"
    "borrower": str | None,
    "times_borrowed": int  # borrow_history uzunligi
}
```

**Status qoidalari:**
- `archived == True` → `"archived"`
- `is_borrowed == True` → `"borrowed"`
- Aks holda → `"available"`

---

## 4. Dunder Metodlar

### `__str__()`
```python
"<Book Clean Code>"
```
Format: `<Book {title}>`

---

### `__repr__()`
```python
"Book(id=1, title='Clean Code', borrowed=True)"
```
Format: `Book(id={id}, title='{title}', borrowed={is_borrowed})`

---

### `__eq__(other)`
Ikki kitobni `id` bo'yicha solishtiradi.

```python
book1 == book2  # book1.id == book2.id
```

---

### `__len__()`
Kitobning sahifalar sonini qaytaradi.

```python
len(book)  # book.pages
```

---

### `__bool__()`
Kitob aktiv yoki yo'qligini ko'rsatadi.

```python
bool(book)  # False agar archived, True aks holda
```

---

## 5. Foydalanish Misoli

```python
from datetime import datetime

# Kitob yaratish
book = Book(1, "Clean Code", "Robert Martin", 464)

# Kitobni berish
book.borrow("Ali")
print(book.borrower)  # "Ali"
print(book.is_borrowed)  # True

# Kitobni qaytarish
book.return_book()
print(book.borrower)  # None

# Nomini o'zgartirish
book.change_title("Clean Code 2nd Edition")

# Info olish
info = book.info()
print(info["status"])  # "available"
print(info["times_borrowed"])  # 1

# Dunder metodlar
print(book)  # <Book Clean Code 2nd Edition>
print(len(book))  # 464
print(bool(book))  # True

# Arxivlash
book.archive()
print(bool(book))  # False
```

---

## 6. Muhim Nuqtalar (Test)

Quyidagi holatlar to'g'ri ishlashi kerak:

✅ **Borrow history yangilanishi** - har safar `borrow()` chaqirilganda tarixga qo'shiladi

✅ **Arxivlangan kitobni borrow qilib bo'lmaydi** - `RuntimeError` ko'tariladi

✅ **Olingan kitobni arxivlab bo'lmaydi** - `RuntimeError` ko'tariladi

✅ **`__eq__` faqat ID bo'yicha** - boshqa fieldlar farq qilsa ham ID bir xil bo'lsa `True`

✅ **`len(book)` sahifalar sonini** qaytaradi

✅ **`info()` to'g'ri status** - available/borrowed/archived
