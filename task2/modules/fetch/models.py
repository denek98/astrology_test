from dataclasses import dataclass, asdict


@dataclass
class CurrencyRateParams:
    """
    A data class to hold the parameters for the currency rate API request.
    """

    date: str
    base_currency: str
    currencies: str

    def dict(self) -> dict[str, str]:
        """
        Converts the dataclass instance to a dictionary.

        :return: A dictionary representation of the dataclass.
        """
        return asdict(self)
