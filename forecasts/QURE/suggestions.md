# QURE rev3: gaps for the forecaster skill / repo

1. Validator: no structure for scenario sensitivities (Q4-approval, alternative refill); kept in diag.json and forecast.md only.
2. No field for royalty-financing liabilities (HemB SPV $473.2M) that Finagle should treat as debt; noted in text only.
3. No field to mark an input as coming from a CEO-simulation bot (pointer, not a document); rev3's year-1 ~190 path is tagged [S] with the user's P item, which is the closest fit.
4. Finagle request: SBC/capex lists tied to the forecast revenue path must be rebuilt by hand whenever the forecast changes; a %-of-sales option for forecast.sbc and forecast.capex would remove that coupling.
