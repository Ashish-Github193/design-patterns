from tabulate import tabulate


class TableData:
    def extract_data(self):
        """Returns data in a table format
        Returns:
            dict: A dictionary containing the data in a table format
        """
        return {
            "names": ["John", "Jane", "Bob"],
            "ages": [25, 30, 35],
            "genders": ["male", "female", "male"],
        }


class BarChartPlugin:
    def set_data(self, data: list[list[str]]):
        """Sets the data for the bar chart
        Parameters:
            data (list[list[str]]): A list of lists containing the data for the bar chart
        """
        formatted_data = tabulate(data[1:], headers=data[0], tablefmt="pipe")
        print(formatted_data)


class Adapter:
    def table_data_to_bar_chart(
        self, table_data: TableData
    ) -> list[list[str]]:
        """Converts a TableData object to a format compatible with BarChartPlugin
        Parameters:
            table_data (TableData): A table data object
        Returns:
            list[list[str]]: A formatted list of lists
        """
        extracted_data = table_data.extract_data()
        if not extracted_data:
            raise ValueError("TableData returned empty data.")

        headers = list(extracted_data.keys())
        rows = zip(*extracted_data.values())
        return [headers, *rows]


if __name__ == "__main__":
    table_data = TableData()
    adapter = Adapter()
    formatted_data = adapter.table_data_to_bar_chart(table_data)

    bar_chart = BarChartPlugin()
    bar_chart.set_data(formatted_data)
