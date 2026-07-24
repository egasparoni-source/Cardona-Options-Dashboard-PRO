from pprint import pprint

from src.risk.risk_manager import RiskManager

resultado = RiskManager.analyze(

    capital=5000,

    risk_percent=1,

    entry=748.28,

    stop=716.58,

    target=811.68

)

print("\n========== RISK MANAGER ==========\n")

pprint(resultado)

print("\n=================================\n")