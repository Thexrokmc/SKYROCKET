from datetime import datetime
import platform
import sys


class SystemReport:

    def __init__(

        self,

        health_check,

        integration_tests

    ):

        self.health_check = health_check
        self.integration_tests = integration_tests

    def generate(self):

        health = self.health_check.run()

        tests = self.integration_tests.run()

        return {

            "generated_at": datetime.utcnow().isoformat(),

            "python_version": sys.version,

            "platform": platform.platform(),

            "health": health,

            "tests": tests,

            "summary": {

                "health_ok": all(

                    value == "OK"

                    or value == "Not configured"

                    for value in health.values()

                ),

                "tests_passed": tests["passed"],

                "tests_failed": tests["failed"]

            }

        }
