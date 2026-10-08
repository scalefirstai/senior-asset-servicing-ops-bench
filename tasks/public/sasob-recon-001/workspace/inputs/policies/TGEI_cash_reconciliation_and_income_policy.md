# Tidewell Funds Trust — Fund Accounting Procedures (extract)
Administrator: Pellmore Fund Services. Approved by the Fund Treasurer 2025-11-03. Version 4.2.

## 3. Daily cash reconciliation
3.1 Each custody cash account is reconciled daily to the accounting system before NAV release.
3.2 Every difference must be identified to a transaction and a root cause. Differences are corrected on
    the side that is wrong. Timing differences are carried as reconciling items with an expected clear date.
3.3 **No plugs.** Unexplained differences may not be written off, plugged to expense or to suspense
    without written approval of the Fund Controller, and never above USD 1,000 in aggregate per fund per day.
3.4 Cash received that does not belong to the Fund (misdirected wires, other-fund activity) must not be
    recorded as Fund income or capital share activity. Notify the custodian and the relevant transfer
    agent/fund accounting team the same day and track as a custodian-side reconciling item until reversed.
3.5 Accrued expenses paid by custodian auto-debit are recorded as a payment against the accrual.
    Any difference between the invoice and the accrual is trued up through the expense line.

## 4. Foreign exchange
4.1 FX trades are booked at the executed contract rate per the counterparty confirmation. WMR benchmark
    rates are used only for valuation of FX balances, never for booking executed trades.

## 5. Investment income
5.1 Dividend income is recorded gross on ex-date; foreign withholding tax is recorded at the rate expected
    to be withheld at source given the Fund's documentation status on the record date.
5.2 Where tax is withheld above the applicable treaty rate and the Fund is eligible to reclaim the excess,
    the excess is recorded as a tax reclaim receivable (GL 1450) — not as an expense — provided the reclaim
    is considered collectible. Reclaims in FR, DE, NL and JP are considered collectible. Tax Services
    (custodian) is instructed to file the reclaim.
5.3 Depositary (ADR/ADS) fees deducted from distributions are recorded as a reduction of dividend income.

## 6. Security master
6.1 Settlement cycle defaults: US equities and US corporate bonds settle T+1 (SEC Rule 15c6-1, as amended
    effective 2024-05-28). Security master exceptions are reported to Reference Data (security_master)
    for correction at source.
