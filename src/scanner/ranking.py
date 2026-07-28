class Ranking:

    @staticmethod
    def sort(results):

        valid_results = []

        for result in results:

            try:
                if (
                    result is not None
                    and result.get("trade") is not None
                    and "score" in result["trade"]
                ):
                    valid_results.append(result)

            except Exception:
                pass

        return sorted(
            valid_results,
            key=lambda x: x["trade"]["score"],
            reverse=True
        )