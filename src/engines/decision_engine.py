class SkyScoreEngine:

    def calculate(self, results):

        total_weight = 0
        achieved_weight = 0

        for result in results:

            total_weight += result.weight

            if result.passed:
                achieved_weight += result.weight

        if total_weight == 0:
            return 0

        return round(
            achieved_weight / total_weight * 100,
            1
        )
