from datetime import datetime
from zoneinfo import ZoneInfo


class MarketSession:

    @staticmethod
    def get_status():

        ny_time = datetime.now(ZoneInfo("America/New_York"))

        hour = ny_time.hour
        minute = ny_time.minute

        current = hour * 60 + minute

        market_open = 9 * 60 + 30
        market_close = 16 * 60

        weekday = ny_time.weekday()

        if weekday >= 5:
            return {
                "status": "CLOSED",
                "icon": "🔴",
                "time": ny_time.strftime("%H:%M"),
                "message": "Weekend"
            }

        if current < market_open:
            return {
                "status": "PRE-MARKET",
                "icon": "🟡",
                "time": ny_time.strftime("%H:%M"),
                "message": "Waiting for open"
            }

        if current <= market_close:
            return {
                "status": "OPEN",
                "icon": "🟢",
                "time": ny_time.strftime("%H:%M"),
                "message": "Market Open"
            }

        return {
            "status": "AFTER HOURS",
            "icon": "🟠",
            "time": ny_time.strftime("%H:%M"),
            "message": "After Hours"
        }