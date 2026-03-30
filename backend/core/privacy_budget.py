class PrivacyBudget:
    def __init__(self, total_budget=5.0):
        self.total_budget = total_budget
        self.remaining_budget = total_budget

    def consume(self, epsilon):
        if epsilon > self.remaining_budget:
            raise Exception("Privacy budget exhausted")
        self.remaining_budget -= epsilon

    def remaining(self):
        return self.remaining_budget