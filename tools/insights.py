def generate_insights(df):
    insights = []

    insights.append(f"Rows: {df.shape[0]}")
    insights.append(f"Columns: {df.shape[1]}")
    insights.append(f"Missing values: {df.isnull().sum().sum()}")

    return insights