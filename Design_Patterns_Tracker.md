# Design Patterns Tracker

**Project:** Python Stock Analysis & Recommendation Engine (C++ core via pybind11)
**Format:** 1 hour/day — 15 min concept, 35 min implementation, 10 min log
**Start date:** Sept 12, 2026
**Target finish:** Dec 25, 2026 (buffer before Jan 1 DSA start)
**Languages:** Python (AI/ML, orchestration) + C++ (engine-level patterns). Java excluded — work-only.

---

## Session Structure (repeat daily)

1. **Concept (15 min):** What problem does this solve? What breaks without it?
2. **Implement (35 min):** Apply it directly inside the stock-engine project — no toy examples in isolation.
3. **Log (10 min):** Fill in the row below — Problem / Where Used / Gotcha.

---

## Phase 0 — SOLID Foundations (Sept 12–18)

| Day | Date       | Principle             | Refactor Target                                                       | Status |
| --- | ---------- | --------------------- | --------------------------------------------------------------------- | ------ |
| 1   | Sept 12    | Single Responsibility | Split `DataFetcher` into Fetch/Parse/Cache                            | ☑      |
| 2   | Sept 13    | Open/Closed           | `Indicator` base class — new indicators without editing existing code | ☑      |
| 3   | Sept 14    | Liskov Substitution   | Ensure `PredictionStrategy` subclasses are swappable                  | ☑      |
| 4   | Sept 15    | Interface Segregation | Split bloated `Engine` into `Trainable`/`Predictable`/`Backtestable`  | ☑      |
| 5   | Sept 16    | Dependency Inversion  | C++ engine adapter depends on abstract interface, not concrete class  | ☐      |
| 6-7 | Sept 17–18 | Review/buffer         | Re-read week's code, tighten any rushed refactor                      | ☐      |

---

## Phase 1 — Creational Patterns (Sept 19 – Oct 9)

| Pattern          | Est. Days | Project Mapping                                | Status |
| ---------------- | --------- | ---------------------------------------------- | ------ |
| Singleton        | 1         | Config/logger manager, DB connection pool      | ☐      |
| Factory Method   | 3         | `DataSource` objects (NSE API, CSV, yfinance)  | ☐      |
| Abstract Factory | 3         | Indicator calculator families (Trend/Momentum) | ☐      |
| Builder          | 3         | `BacktestConfig` step-by-step construction     | ☐      |
| Prototype        | 1         | Clone `Portfolio` state for what-if simulation | ☐      |

---

## Phase 2 — Structural Patterns (Oct 10 – Oct 30)

| Pattern   | Est. Days | Project Mapping                                                | Status |
| --------- | --------- | -------------------------------------------------------------- | ------ |
| Adapter   | 3         | Wrap C++ backtesting engine behind Python interface (pybind11) | ☐      |
| Bridge    | 3         | Decouple prediction strategy from execution engine             | ☐      |
| Composite | 3         | `Portfolio` → `Position` → `Trade` hierarchy                   | ☐      |
| Decorator | 2         | Logging/caching/rate-limiting on data-fetch calls              | ☐      |
| Facade    | 2         | `AnalysisEngine.run(ticker)` hiding RAG+indicators+engine      | ☐      |
| Proxy     | 2         | Lazy-load heavy historical data                                | ☐      |
| Flyweight | 2         | Shared indicator-parameter objects across backtests            | ☐      |

---

## Phase 3 — Behavioral Core (Oct 31 – Nov 20)

| Pattern                 | Est. Days | Project Mapping                                               | Status |
| ----------------------- | --------- | ------------------------------------------------------------- | ------ |
| Strategy                | 3         | Swappable prediction algorithms (LSTM/MA-crossover/sentiment) | ☐      |
| Observer                | 3         | Notify dashboard/logger/alerts on new signal                  | ☐      |
| Command                 | 3         | Buy/sell/hold as queueable, loggable, undoable objects        | ☐      |
| Template Method         | 2         | Fixed `run_backtest()` skeleton, override `generate_signal()` | ☐      |
| Chain of Responsibility | 3         | Validation pipeline: risk → capital → compliance checks       | ☐      |
| State                   | 3         | `Trade` lifecycle: pending → executed → closed                | ☐      |

---

## Phase 4 — Remaining Behavioral (Nov 21 – Dec 4)

| Pattern     | Est. Days | Project Mapping                                                      | Status |
| ----------- | --------- | -------------------------------------------------------------------- | ------ |
| Mediator    | 3         | Coordinate RAG + MCP orchestration + prediction engine               | ☐      |
| Memento     | 2         | Save/restore portfolio snapshots (undo/rollback)                     | ☐      |
| Visitor     | 3         | Run tax/risk/performance calcs over `Portfolio` without modifying it | ☐      |
| Iterator    | 2         | Custom iteration over time-series with lookback windows              | ☐      |
| Interpreter | 2         | Small DSL for user-defined trading rules (lowest priority)           | ☐      |

---

## Phase 5 — Advanced / Enterprise Patterns (Dec 5 – Dec 25)

| Pattern            | Est. Days | Project Mapping                                            | Status |
| ------------------ | --------- | ---------------------------------------------------------- | ------ |
| Repository         | 2         | Abstract data access (DB/API/CSV) behind uniform interface | ☐      |
| Unit of Work       | 2         | Batch portfolio changes into one atomic commit             | ☐      |
| CQRS               | 2         | Separate read path (dashboard) from write path (execution) | ☐      |
| Producer-Consumer  | 2         | Feed live market data into engine via queue                | ☐      |
| Thread/Object Pool | 2         | Reuse DB connections / backtest workers                    | ☐      |
| Active Object      | 2         | Decouple async prediction request from execution           | ☐      |
| Circuit Breaker    | 1         | Stop hammering a failing data API                          | ☐      |
| Retry with Backoff | 1         | Pair with Circuit Breaker                                  | ☐      |
| Saga               | 2         | Multi-step fetch→predict→execute→log with rollback         | ☐      |
| Null Object        | 1         | `NoOpStrategy` instead of scattered null checks            | ☐      |
| Specification      | 2         | Composable filter rules (e.g., RSI < 30 AND volume > X)    | ☐      |

---

## Daily Log

_Fill in after each session. Keep entries short — 2-3 lines max._

| Date    | Pattern/Principle | Problem It Solved                                                                                                                | Where Used in Project                                                                                                                               | Gotcha / Note                                                                                                                                                     |
| ------- | ----------------- | -------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Sept 12 | SRP               | DataFetcher mixed IO+parsing+caching — any change to one risked breaking the others                                              | python/ingestion/ split into fetcher.py, parser.py, cache.py                                                                                        | orchestrator (main.py) is allowed to know about all three — SRP applies per-class, not per-file-that-uses-them                                                    |
| Sept 13 | OCP               | Adding indicators would've meant editing a growing if/elif block                                                                 | python/indicators/ — base.py + sma.py, ema.py, rsi.py                                                                                               | Abstract base class in Python needs ABC + @abstractmethod, or nothing forces subclasses to implement calculate()                                                  |
| Sept 14 | LSP               | A strategy subclass with a different return type/signature would silently break any caller looping over strategies               | python/strategies/ — base.py + ma_crossover.py, threshold.py                                                                                        | Insufficient data should return "hold", never raise — raising on valid-but-sparse input is itself an LSP violation (caller can't blindly call .predict() anymore) |
| Sept 15 | ISP               | A single fat Engine interface would've forced rule-based strategies to implement dummy train()/backtest() methods they never use | python/strategies/interfaces.py — split into Predictable, Trainable, Backtestable                                                                   | Python allows multiple inheritance cleanly here (LSTMStrategy(Predictable, Trainable)) — this is exactly the scenario ISP is designed for                         |
| Sept 16 | DIP               | AnalysisEngine calling a concrete engine class directly would mean rewriting it when the real C++ engine replaces the stub       | python/engine_bridge/interface.py (abstraction) + stub_engine.py (concrete) + analysis_engine.py (depends on abstraction, injected via constructor) | Constructor injection is the simplest DIP mechanism in Python — no DI framework needed for a project this size                                                    |

## Notes

- Java is excluded from this tracker — it's covered separately for work (Windchill/Creo context), one pattern/week per manager's guidance.
- This tracker feeds directly into the 18-week capstone build plan — patterns implemented here become part of the actual capstone codebase, not throwaway examples.
- If a week gets missed, don't compress two patterns into one day — push the schedule forward instead. Depth over pace.
