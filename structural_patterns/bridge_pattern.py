class PaymentMethod(object):
    def __init__(self) -> None:
        self.type: str = ""


class CreditCardPayment(PaymentMethod):
    def __init__(self) -> None:
        super().__init__()
        self.type = "Credit Card"


class PayPalPayment(PaymentMethod):
    def __init__(self) -> None:
        super().__init__()
        self.type = "PayPal"


class ProductOrder(object):
    def __init__(self, payment_method: PaymentMethod) -> None:
        self.product_order_type: str
        self.payment_method = payment_method

    def process_payment(self) -> None:
        print(
            f"Processing {self.product_order_type} order with {self.payment_method.type}"
        )


class PhysicalProductOrder(ProductOrder):
    def __init__(self, payment_method: PaymentMethod) -> None:
        super().__init__(payment_method)
        self.product_order_type = "Physical"


class DigitalProductOrder(ProductOrder):
    def __init__(self, payment_method: PaymentMethod) -> None:
        super().__init__(payment_method)
        self.product_order_type = "Digital"


if __name__ == "__main__":
    physical_order_with_credit_card = PhysicalProductOrder(CreditCardPayment())
    physical_order_paypal = PhysicalProductOrder(PayPalPayment())
    digital_order_with_credit_card = DigitalProductOrder(CreditCardPayment())
    digital_order_paypal = DigitalProductOrder(PayPalPayment())

    physical_order_with_credit_card.process_payment()
    physical_order_paypal.process_payment()
    digital_order_with_credit_card.process_payment()
    digital_order_paypal.process_payment()
