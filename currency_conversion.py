
class Money:

    def __init__(self, value, symbol):
        self.value = value
        self.symbol = symbol

    def convert(self):
        usd = 1
        euro_usd = 1.13
        yen_usd = .01
        btc_usd = 607.65
        if self.symbol == "USD":
            self.conversion = usd
            self.total = self.value * self.conversion
        elif self.symbol == "EUR":
            self.conversion = euro_usd
            self.total = self.value * self.conversion
        elif self.symbol == "JPY":
            self.conversion = yen_usd
            self.total = self.value * self.conversion
        elif self.symbol == "BTC":
            self.conversion = btc_usd
            self.total = self.value * self.conversion
        return self.total

    def __add__(self, other):
        return Money((self.convert() + other.convert()) / self.conversion, self.symbol)

    def __sub__(self, other):
        return Money((self.convert() - other.convert()) / self.conversion, self.symbol)

    def __mul__(self, other):
        return Money((self.convert() * other.convert()) / self.conversion, self.symbol)

    def __eq__(self, other):
        return Money(self.convert) == Money(other.convert)

    def __gt__(self, other):
        return Money(self.convert()) > Money(other.convert())

    def __ge__(self, other):
        return Money(self.convert()) >= Money(other.convert())

    def __lt__(self, other):
        return Money(self.convert()) < Money(other.convert())

    def __le__(self, other):
        return Money(self.convert()) <= Money(other.convert())

    def __ne__(self, other):
        return Money(self.convert()) != Money(other.convert())

    def __str__(self):
        return "{} {}".format(self.value, self.symbol)


# dollars = Money(1, "USD")
# yen = Money(100.303, "JPY")
# euro = Money(.89, "EUR")
# bitcoin = Money(.0016, "BTC")

btc = Money(500, "BTC")
print(btc.convert())

print ((Money(500, "EUR")) * (Money(20, "BTC")))
