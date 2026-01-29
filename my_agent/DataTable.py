import pandas as pd

data = {
    "Endpoint/Service": [
        "GET /adapter05/card/{digitizedCardId}", "POST /adapter05/card/digitizable",
        "POST /adapter06/card/digitizable", "POST /adapter06/card/notify",
        "GET /v1/investment-reporting/report/{reportType}/elements",
        "GET /v1/investment-reporting/tech-services/health/check",
        "POST /v1/internal/investments/open-sr"
    ],
    "Asset Name": [
        "ITA Wallet Credit Card API", "ITA Wallet Credit Card API",
        "ITA Wallet Debit Card API", "ITA Wallet Debit Card API",
        "ITA Investment Management", "ITA Investment Management",
        "ITA InvestmentReporting API"
    ],
    "Reference Squad": [
        "Credit Card Squad", "Credit Card Squad",
        "Debit Card Squad", "Debit Card Squad",
        "Investment Squad", "Investment Squad",
        "Investment Squad"
    ]
}

df = pd.DataFrame(data)
print(df)