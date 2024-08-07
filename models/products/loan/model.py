import datetime
import enum
import math
from typing import List

import pydantic

from models.products import model as product_model


class LoanStates(enum.Enum):
    ACTIVE = enum.auto()
    PAID = enum.auto()
    CANCELED = enum.auto()


class LoanPayment(pydantic.BaseModel):
    id: int = pydantic.Field(..., description="Unique identifier for the payment.")
    date: datetime.date = pydantic.Field(..., description="Date when the payment was made.")
    amount: float = pydantic.Field(..., gt=0, description="Amount of the payment.")


class LoanPaymentSummary(pydantic.BaseModel):
    expected_payments: List[LoanPayment] = pydantic.Field(default_factory=list,
                                                          description="List of expected payments.")
    actual_payments: List[LoanPayment] = pydantic.Field(default_factory=list,
                                                        description="List of payments that have been made.")

    @property
    def total_paid_amount(self) -> float:
        """Calculate the total amount paid from actual payments."""
        return sum(payment.amount for payment in self.actual_payments)


class Loan(product_model.Product):
    principal: float = pydantic.Field(..., gt=0, description="Initial amount of money borrowed.")
    monthly_interest_rate: float = pydantic.Field(..., ge=0, description="Monthly interest rate as a percentage.")
    start_date: datetime.date = pydantic.Field(..., description="Start date of the loan.")
    term_in_days: int = pydantic.Field(..., gt=0, description="Term in days.")
    payment_periodicity: int = pydantic.Field(..., gt=0, description="Payment periodicity in days.")
    payment_summary: LoanPaymentSummary = pydantic.Field(default=None,
                                                         description="Summary of payments related to the loan.")
    state: LoanStates = pydantic.Field(..., description="State of the loan.")

    @property
    def end_date(self) -> datetime.date:
        """Calculate the duration of the loan in days."""
        return self.start_date + datetime.timedelta(days=self.term_in_days)

    @property
    def total_to_due(self) -> float:
        """Calculate the single payment using the formula for an amortizing loan."""
        p = self.principal
        r = self.monthly_interest_rate / 100
        t = self.term_in_days / 30
        return p * (1 + r * t)

    @property
    def single_payment(self) -> float:
        """Calculate the total payment over the life of the loan."""
        return self.total_to_due / self.number_of_payments

    @property
    def number_of_payments(self) -> int:
        """Calculate the number of payments required."""
        return math.ceil(self.term_in_days / self.payment_periodicity)

    @property
    def outstanding_balance(self) -> float:
        """Calculate the remaining balance after payments."""
        return self.total_to_due - self.payment_summary.total_paid_amount
