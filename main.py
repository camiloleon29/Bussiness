import datetime

import pydantic

from models.products.loan import builder as loan_builder


class Settings(pydantic.BaseModel):
    sundays_off: bool = True
    saturdays_off: bool = True
    holidays_off: bool = True


if __name__ == "__main__":
    builder = loan_builder.LoanBuilder()
    loan = builder.create(
        principal=1100000,
        monthly_interest_rate=10.0,
        term_in_days=30,
        start_date=datetime.date(2024, 8, 5),
        payment_periodicity=1,
    )

    for payment in loan.payment_summary.expected_payments:
        print(f"Payment ID: {payment.id}, Date: {payment.date}, Amount: ${payment.amount:.2f}")

    print(f"Total Amount Due: ${loan.total_to_due:.2f}")

