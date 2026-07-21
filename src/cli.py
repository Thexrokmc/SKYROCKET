import argparse

from main import main
from core.version import VersionManager


def create_parser():

    parser = argparse.ArgumentParser(
        prog="skyrocket",
        description="SKYROCKET Crypto Portfolio Intelligence"
    )

    parser.add_argument(
        "--version",
        action="store_true",
        help="Show application version."
    )

    parser.add_argument(
        "--health",
        action="store_true",
        help="Run system health check."
    )

    parser.add_argument(
        "--analyze",
        action="store_true",
        help="Run portfolio analysis."
    )

    return parser


def run():

    parser = create_parser()

    args = parser.parse_args()

    if args.version:

        print(
            VersionManager.full_version()
        )

        return

    if args.health:

        print(
            "Health check not implemented yet."
        )

        return

    if args.analyze:

        main()

        return

    parser.print_help()


if __name__ == "__main__":

    run()
