# Request: DCF valuation

**From:** Senior Portfolio Manager
**To:** Equity Research Analyst

We are considering a position in **Apple Inc.** (ticker AAPL). The company's latest annual
report (Form 10-K) is attached in `anchor/`, together with my notes in `companions/manager_notes.md`.

Please build an Excel DCF model (`.xlsx`) that values the equity and gives me an intrinsic value per share.

Requirements:
1. Pull historical revenue, operating income, D&A, capex, and change in working capital for the last
   3 fiscal years from the 10-K.
2. Project unlevered free cash flow for 5 years. State and justify your revenue growth and margin assumptions.
3. Estimate WACC (show cost of equity via CAPM, pre-tax cost of debt, tax rate, capital weights). Use the
   risk-free rate, equity risk premium, beta, cost of debt and reference share price given in my notes.
4. Compute terminal value (Gordon growth) and enterprise value; bridge to equity value using net debt
   and diluted shares from the 10-K.
5. Include a **sensitivity table** of value per share across WACC (+/-1.0 pt, 0.5 pt steps) and terminal
   growth (1.5% to 3.5%).
6. Add a short "Assumptions and risks" sheet (max 150 words).

Keep inputs in clearly labelled cells and use formulas, not hard-coded results.
