class DataExplorer:
    def __init__(self, data):
        """
        Initialize the DataExplorer class with the data.

        Args:
            data (DataFrame): The dataset for exploration.
        """
        self.data = data

    def display_top_rows(self, n=5):
        """
        Display the top rows of the data.

        Args:
            n (int): Number of rows to display (default is 5).
        """
        print(f"Top {n} rows of training data:")
        print(self.data.head(n))
        print("--------------------------------------------------------------------------------------------------------------")

    def display_bottom_rows(self, n=5):
        """
        Display the bottom rows of the data.

        Args:
            n (int): Number of rows to display (default is 5).
        """
        print(f"Bottom {n} rows of training data:")
        print(self.data.tail(n))
        print("--------------------------------------------------------------------------------------------------------------")

    def display_random_rows(self, n=5):
        """
        Display random rows from both training and testing data.

        Args:
            n (int): Number of rows to display (default is 5).
        """
        print(f"Random {n} rows of training data:")
        print(self.data.sample(n))
        print("--------------------------------------------------------------------------------------------------------------")

    def display_shape(self):
        """
        Display the shape (number of rows and columns) of the datasets.
        """
        print("Shape of the dataset:")
        print(f"Rows: {self.data.shape[0]}, Columns: {self.data.shape[1]}")
        print("--------------------------------------------------------------------------------------------------------------")

    def display_columns(self):
        """
        Display the column names of the datasets.
        """
        print("Columns of the dataset:")
        print(self.data.columns)
        print("--------------------------------------------------------------------------------------------------------------")

    def display_info(self):
        """
        Display information about the data types and non-null counts of the datasets.
        """
        print("Info about the dataset:")
        print(self.data.info())
        print("--------------------------------------------------------------------------------------------------------------")

    def display_descriptive_stats(self):
        """
        Display descriptive statistics (count, mean, std, min, 25%, 50%, 75%, max) of the datasets.
        """
        print("Descriptive statistics of dataset:")
        print(self.data.describe())
        print("--------------------------------------------------------------------------------------------------------------")