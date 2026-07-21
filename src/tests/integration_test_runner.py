from datetime import datetime


class IntegrationTestRunner:

    def __init__(self):

        self.tests = []

    def add_test(

        self,

        name,

        test_function

    ):

        self.tests.append(

            (

                name,

                test_function

            )

        )

    def run(self):

        results = []

        passed = 0

        failed = 0

        started = datetime.utcnow()

        for name, test in self.tests:

            try:

                test()

                results.append({

                    "name": name,

                    "status": "PASS"

                })

                passed += 1

            except Exception as e:

                results.append({

                    "name": name,

                    "status": "FAIL",

                    "error": str(e)

                })

                failed += 1

        finished = datetime.utcnow()

        return {

            "started": started.isoformat(),

            "finished": finished.isoformat(),

            "passed": passed,

            "failed": failed,

            "results": results

        }
