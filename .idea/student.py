class Student:
    def __init__(self, name, fees_rate):
        self.name = name
        self.dates_attended = []
        self.fees_rate = fees_rate
        self.fees_paid = 0
        self.fees_status = "Unpaid"
        self.credit_classes = 0  # extra classes paid for

    def add_attendance(self, date):
        self.dates_attended.append(date)

    def pay_fees(self, amount, expected_classes):
        self.fees_paid += amount

        expected_fees = expected_classes * self.fees_rate
        if self.fees_paid > expected_fees:
            # Calculate extra amount
            extra_amount = self.fees_paid - expected_fees
            extra_classes = extra_amount // self.fees_rate
            self.credit_classes += int(extra_classes)
            # Keep partial leftover money if it doesn't complete a full class
            self.fees_paid = expected_fees + (extra_amount % self.fees_rate)

        self.update_status()

    def calculate_due(self):
        attended_classes = len(self.dates_attended)
        total_classes_charged = attended_classes

        if self.credit_classes > 0:
            if attended_classes <= self.credit_classes:
                self.credit_classes -= attended_classes
                total_classes_charged = 0
            else:
                total_classes_charged = attended_classes - self.credit_classes
                self.credit_classes = 0

        total_fees = total_classes_charged * self.fees_rate
        due = total_fees - self.fees_paid

        return due

    def update_status(self):
        self.fees_status = "Paid" if self.fees_paid >= 0 else "Unpaid"
