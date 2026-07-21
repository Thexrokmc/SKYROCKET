from config.symbols import Symbols

from engine.skyrocket_engine import SkyrocketEngine


def main():

    engine = SkyrocketEngine()

    print()

    print("=" * 70)
    print("🚀 SKYROCKET v1.0")
    print("=" * 70)
    print()

    for symbol in Symbols.all():

        try:

            report = engine.analyze(symbol)

            print(report)

            print()

        except Exception as e:

            print(f"{symbol} -> ERROR")

            print(e)

            print()

    print("=" * 70)
    print("Analysis Complete")
    print("=" * 70)


if __name__ == "__main__":

    main()
