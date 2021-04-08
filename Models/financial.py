class Financial:
    _name = None
    _year_one = 0
    _year_two = 0
    _year_three = 0

    def __init__(self, name, year_one, year_two, year_three):
        self._name = name
        self._year_one = year_one
        self._year_two = year_two
        self._year_three = year_three

    def get_name(self):
        return self._name

    def get_year_one(self):
        return self._year_one

    def get_year_two(self):
        return self._year_two

    def get_year_three(self):
        return self._year_three

    def __str__(self):
        return f"{self._name}, Y1:{self._year_one}, Y2:{self._year_two}, Y3:{self._year_three}"

