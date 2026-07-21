class Decision:

    def __init__(self):

        self.action = ""

        self.score = 0

        self.reasons = []

    def add_reason(self, reason):

        self.reasons.append(reason)
