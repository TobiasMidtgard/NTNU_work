def get_total_days(dataframe):
    return len(dataframe) // 24


def get_average_consumption(dataframe):
    return dataframe["KWH 60 Forbruk"].mean()


def get_largest_usage(dataframe):
    return dataframe["KWH 60 Forbruk"].idxmax()
