import datetime
from typing import List

import pydantic

from models.commons import random_keys
from models.products.loan import model as loan_model
from models.products import model as products_model


class LoanBuilder(pydantic.BaseModel):
    def create(self, principal: float, monthly_interest_rate: float, start_date: datetime.date,
               payment_periodicity: int,
               term_in_days: int) -> loan_model.Loan:
        loan = loan_model.Loan(
            product_id=random_keys.generate_unique_id(),
            product_type=products_model.AVAILABLE_PRODUCT_TYPES[products_model.ProductTypes.LOAN],
            principal=principal,
            monthly_interest_rate=monthly_interest_rate,
            start_date=start_date,
            payment_periodicity=payment_periodicity,
            term_in_days=term_in_days,
            state=loan_model.LoanStates.ACTIVE
        )
        expected_payments = self._generate_expected_payments(loan=loan)
        loan.payment_summary = loan_model.LoanPaymentSummary(
            expected_payments=expected_payments
        )
        return loan

    @staticmethod
    def _generate_expected_payments(loan: loan_model.Loan) -> List[loan_model.LoanPayment]:
        """Generate a list of expected payments."""
        expected_payments = []
        payment_date = loan.start_date
        for i in range(1, loan.number_of_payments + 1):
            expected_payments.append(
                loan_model.LoanPayment(
                    id=i,
                    date=payment_date,
                    amount=loan.single_payment
                )
            )
            payment_date += datetime.timedelta(days=loan.payment_periodicity)
        return expected_payments
