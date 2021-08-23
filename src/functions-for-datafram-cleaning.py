def clear_whitspaces_columns(df):
    """
    Clears whitespaces from the columns in a dataframe 
    """
    col = df.columns

    col=[i.rstrip() for i in col]

    df.columns = col
    