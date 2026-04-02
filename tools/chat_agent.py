def answer_question(df, question):
    question = question.lower()

    if "rows" in question:
        return f"The dataset has {df.shape[0]} rows."

    if "columns" in question:
        return f"The dataset has {df.shape[1]} columns."

    if "missing" in question:
        return f"Missing values: {df.isnull().sum().sum()}"

    return "Try asking about rows, columns, or missing values."