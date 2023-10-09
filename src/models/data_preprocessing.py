def calculate_missing_percentage(data, title):
    """
    Calculate and display the percentage of missing values in a DataFrame.

    Args:
        data (DataFrame): The DataFrame for which missing values are to be calculated.
        title (str): A title to identify the source of the data (e.g., "Train Data").

    Returns:
        None
    """
    # Import the tabulate library for tabular data formatting
    from tabulate import tabulate

    # Calculate the percentage of null values in each feature of the data
    missing_counts_pert = data.isna().mean().reset_index()
    missing_counts_pert.columns = ['Column', 'Missing Proportion']
    missing_counts_pert['Missing Percentage'] = missing_counts_pert['Missing Proportion'] * 100
    missing_counts_pert['Missing Percentage'] = missing_counts_pert['Missing Percentage'].round(2)

    # Print the results using tabulate for better readability
    print(f"Missing Percentage in {title}:\n")
    print(tabulate(missing_counts_pert[['Column', 'Missing Percentage']], headers='keys', tablefmt='pretty'))
