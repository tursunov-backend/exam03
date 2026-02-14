# Task 2: Cinema Booking

## Loyiha Haqida

### Nima Qilamiz?
Siz kinoteattr uchun chipta bron qilish tizimini yozasiz. 

**Real hayotiy misol:**
- Kinoteatrda bitta film ko'rsatiladi (masalan: "Avatar 2")
- Zalda 5 ta o'rin bor (1, 2, 3, 4, 5 raqamli)
- Odamlar kelib o'rinlarni bron qilishadi
- Har bir o'rin faqat **bir marta** band qilinishi mumkin

### Tizim Qanday Ishlaydi?

```
1. Kinoteattr admin "Avatar 2" filmiga seans yaratadi (5 o'rinli)
2. Ali kelib 3-raqamli o'ringa chipta bron qiladi
3. Vali kelib 1-raqamli o'ringa chipta bron qiladi
4. Sardor 3-raqamga bron qilmoqchi → MUMKIN EMAS (Ali olgan)
5. Tizim bo'sh joylarni ko'rsatadi: [2, 4, 5]
```

### Klasslar Strukturasi va Bog'lanish

```
Seat (O'rin)
  ↓ ishlatiladi
Ticket (Chipta) - Seat obyektiga murojaat qiladi
  ↓ saqlaydi
CinemaSession (Seans) - Seat va Ticket obyektlarini boshqaradi
```

**Composition (Tarkib) Nima?**
- `Seat` - alohida class (o'rinni ifodalaydi)
- `Ticket` - alohida class, ichida `Seat` obyekti bor
- `CinemaSession` - asosiy class, `Seat` va `Ticket` obyektlarini yaratadi va boshqaradi

**Muhim:** Har bir class **alohida** yoziladi, lekin ular bir-biri bilan bog'langan.

---

## 1. Seat Class

O'rinni ifodalaydi.

### Constructor

```python
Seat(number: int)
```

### Attributelar

| Nomi | Turi | Boshlang'ich | Tavsif |
|------|------|--------------|--------|
| `number` | int | constructordan | O'rin raqami |
| `is_taken` | bool | `False` | Bandmi? |

### Misol

```python
seat = Seat(3)
print(seat.number)    # 3
print(seat.is_taken)  # False

seat.is_taken = True
print(seat.is_taken)  # True
```

---

## 2. Ticket Class

Chipta - qaysi o'rin va kim olgani.

### Constructor

```python
Ticket(seat: Seat, owner: str)
```

**Muhim:** `seat` parametri `Seat` class obyekti bo'lishi kerak!

### Attributelar

| Nomi | Turi | Tavsif |
|------|------|--------|
| `seat` | Seat | Qaysi o'rin obyekti |
| `owner` | str | Kim olgan |

### Misol

```python
seat = Seat(5)
ticket = Ticket(seat, "Ali")

print(ticket.owner)         # "Ali"
print(ticket.seat.number)   # 5
print(ticket.seat.is_taken) # False (hali band qilinmagan)
```

---

## 3. CinemaSession Class

Asosiy class - butun tizimni boshqaradi.

### Constructor

```python
CinemaSession(movie_title: str, total_seats: int)
```

### Validatsiya
- `movie_title` - bo'sh emas → `ValueError`
- `total_seats` - 0 dan katta → `ValueError`

### Attributelar

| Nomi | Turi | Tavsif |
|------|------|--------|
| `movie_title` | str | Film nomi |
| `total_seats` | int | Jami o'rinlar |
| `seats` | list[Seat] | Barcha Seat obyektlari |
| `bookings` | list[Ticket] | Barcha Ticket obyektlari |

**Constructor da bajariladigan ishlar:**
1. Attributelarni o'rnatish
2. `seats` listini yaratish
3. Har bir o'rin uchun `Seat` obyekti yaratish va listga qo'shish

```python
# Constructor ichida
self.seats = []
for i in range(1, total_seats + 1):
    self.seats.append(Seat(i))
```

---

## 4. CinemaSession Metodlari

### `available_seats() -> list[int]`

Bo'sh o'rinlar raqamlarini qaytaradi.

**Bajarilishi:**
```python
# Pseudocode
result = []
for seat in self.seats:
    if not seat.is_taken:
        result.append(seat.number)
return result
```

---

### `book_seat(seat_number: int, user: str) -> Ticket`

Chipta bron qiladi va `Ticket` obyektini qaytaradi.

**Bajarilishi:**
1. `seat_number` to'g'ri oraliqda borligini tekshirish (1 ≤ seat_number ≤ total_seats)
   - Agar yo'q bo'lsa → `ValueError`
2. `self.seats` dan tegishli `Seat` obyektini topish
3. Agar `seat.is_taken == True` → `RuntimeError` (allaqachon olingan)
4. `seat.is_taken = True` qilish
5. `Ticket(seat, user)` obyekti yaratish
6. `self.bookings` ga qo'shish
7. `Ticket` obyektini qaytarish

**Muhim:** Siz `Ticket` yaratayotganda, `seat` obyektini (butun obyekt) berasiz, faqat raqamni emas!

---

### `__str__() -> str`

```python
"CinemaSession: Avatar 2 (5 seats)"
```

Format: `CinemaSession: {movie_title} ({total_seats} seats)`

---

## 5. To'liq Foydalanish Misoli

```python
# 1. Classlarni import qilish yoki yaratish
# seat.py da Seat class
# ticket.py da Ticket class  
# cinema_session.py da CinemaSession class

# 2. Seans yaratish
session = CinemaSession("Avatar 2", 5)

# 3. Bo'sh joylarni ko'rish
print(session.available_seats())  # [1, 2, 3, 4, 5]

# 4. Bron qilish
ticket1 = session.book_seat(3, "Ali")
print(ticket1.owner)              # "Ali"
print(ticket1.seat.number)        # 3
print(ticket1.seat.is_taken)      # True

# 5. Bo'sh joylar
print(session.available_seats())  # [1, 2, 4, 5]

# 6. Yana bron
ticket2 = session.book_seat(1, "Vali")
print(session.available_seats())  # [2, 4, 5]

# 7. Olingan joyga yana bron (xato)
try:
    session.book_seat(3, "Sardor")
except RuntimeError as e:
    print("Xato: O'rin allaqachon olingan!")

# 8. String representation
print(session)  # CinemaSession: Avatar 2 (5 seats)

# 9. Bookings ro'yxatini ko'rish
print(f"Jami bron: {len(session.bookings)}")  # 2
for ticket in session.bookings:
    print(f"O'rin {ticket.seat.number}: {ticket.owner}")
```

---

## 6. Classlar Orasidagi Bog'lanish

```python
# Seat - mustaqil class
class Seat:
    def __init__(self, number: int):
        self.number = number
        self.is_taken = False

# Ticket - Seat obyektidan foydalanadi
class Ticket:
    def __init__(self, seat: Seat, owner: str):
        self.seat = seat      # Seat obyekti saqlanadi
        self.owner = owner

# CinemaSession - Seat va Ticket obyektlarini yaratadi va boshqaradi
class CinemaSession:
    def __init__(self, movie_title: str, total_seats: int):
        self.seats = [Seat(i) for i in range(1, total_seats + 1)]
        self.bookings = []
    
    def book_seat(self, seat_number: int, user: str) -> Ticket:
        # Seat obyektini topish
        # Ticket yaratish
        # Saqlash
        return ticket
```

---

## 7. Fayl Strukturasi

```
task02/
├── seat.py          # Seat class
├── ticket.py        # Ticket class
├── cinema_session.py # CinemaSession class
└── main.py          # Test/demo kod
```

**seat.py:**
```python
class Seat:
    def __init__(self, number: int):
        self.number = number
        self.is_taken = False
```

**ticket.py:**
```python
from seat import Seat

class Ticket:
    def __init__(self, seat: Seat, owner: str):
        self.seat = seat
        self.owner = owner
```

**cinema_session.py:**
```python
from seat import Seat
from ticket import Ticket

class CinemaSession:
    # ... kodingiz
```

---

## 8. Muhim Nuqtalar

✅ **Har bir class alohida** - Seat, Ticket, CinemaSession alohida fayllar

✅ **Composition** - Ticket ichida Seat obyekti bor

✅ **Constructor seats yaratadi** - CinemaSession boshida barcha Seat larni yaratadi

✅ **book_seat Ticket obyekti qaytaradi** - to'g'ri return type

✅ **Band o'ringa bron qilib bo'lmaydi** - RuntimeError

✅ **available_seats faqat bo'sh joylar** - is_taken == False
