def compute_confidence(eval_result):

    try:
        df = eval_result["results"]

        score = (
            df["faithfulness"][0]
            + df["answer_relevancy"][0]
            + df["context_precision"][0]
        ) / 3

        return round(score, 3)

    except:
        return 0.0
