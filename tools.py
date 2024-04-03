import pandas as pd

# Function for cleaning urls from text data
def remove_urls(strings: pd.Series) -> pd.Series:
    parts = strings.str.split('https://', n=1)
    result = parts.str[0].fillna('')
    return result

# Combine pipeline results with news titles
def combine_result(result: list, titles: list) -> list:
    for i in range(len(titles)):
        result[i]['title'] = titles[i]
    return result

# Calculate percentage of each label
def get_percentages(series: pd.Series) -> None:
    n = len(series)
    n_negative = sum(series == 0)
    n_positive = sum(series == 1)
    n_neutral = sum(series == 2)
    negative_pct = round(100 * (n_negative / n), 2)
    positive_pct = round(100 * (n_positive / n), 2)
    neutral_pct = round(100 * (n_neutral / n), 2)

    print(f'Positive : {n_positive} ({positive_pct}%)\nNeutral : {n_neutral} ({neutral_pct}%)\nNegative : {n_negative} ({negative_pct}%)\nOf total {n} articles')

if __name__ == '__main__':
    pass