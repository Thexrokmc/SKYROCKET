class SkyrocketEngine:

    def __init__(
        self,
        market_provider,
        facts_engine,
        score_engine,
        decision_engine,
        market_cycle_engine,
        risk_engine,
        capital_manager,
        dca_scheduler,
        report_generator
    ):

        self.market_provider = market_provider
        self.facts_engine = facts_engine
        self.score_engine = score_engine
        self.decision_engine = decision_engine
        self.market_cycle_engine = market_cycle_engine
        self.risk_engine = risk_engine
        self.capital_manager = capital_manager
        self.dca_scheduler = dca_scheduler
        self.report_generator = report_generator

    def analyze(

        self,

        symbol,

        portfolio_value,

        asset_value,

        available_cash,

        fear_greed,

        days_since_last_buy

    ):

        market = self.market_provider.get(symbol)

        facts = self.facts_engine.build(market)

        score = self.score_engine.calculate(facts)

        cycle = self.market_cycle_engine.detect(market)

        decision = self.decision_engine.make(score)

        risk = self.risk_engine.recommend(
            portfolio_value,
            asset_value,
            score,
            cycle
        )

        capital = self.capital_manager.recommend(
            available_cash,
            score,
            cycle
        )

        dca = self.dca_scheduler.recommend(
            score,
            cycle,
            fear_greed,
            days_since_last_buy
        )

        return self.report_generator.generate(
            symbol=symbol,
            market=market,
            facts=facts,
            score=score,
            cycle=cycle,
            decision=decision,
            risk=risk,
            capital=capital,
            dca=dca
        )
