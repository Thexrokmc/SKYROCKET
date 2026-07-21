class DCAManager:

    def recommend(

        self,

        score,

        allocation

    ):

        if allocation >= 20:

            return "NO BUY"

        if score >= 90:

            return "STRONG DCA"

        elif score >= 80:

            return "BUY"

        elif score >= 65:

            return "SMALL BUY"

        elif score >= 50:

            return "WAIT"

        else:

            return "SKIP"
