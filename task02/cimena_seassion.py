from seat import Seat
from ticket import Ticket


class CinemaSession:
    def __init__(self, movie_title: str, total_seats: int):
        if not movie_title.strip():
            raise ValueError("moviie_title bosh bolisji mumkin emas")
        if total_seats <= 0:
            raise ValueError("total_seats - dan katta bolishi kerak")
        self.seats = [Seat(i) for i in range(1, total_seats + 1)]
        self.bookings = []

    def available_seats(self) -> list[int]:
        result = []
        for seat in self.seats:
            if not seat.is_taken:
                result.append(seat.number)
        return result

    def book_seat(self, seat_number: int, user: str) -> Ticket:
        seat = None
        for s in self.seats:
            if s.number == seat_number:
                seat = s
                break

        if seat is None:
            raise ValueError("Bunday o'rin mavjud emas")

        if seat.is_taken:
            raise RuntimeError("Bu o'rin allaqachon band")

        seat.is_taken = True

        ticket = Ticket(seat, user)
        self.bookings.append(ticket)

        return ticket
