import csv


class FileHandler:
    def __init__(self) -> None:
        self.rows = []

    def read(self, input):
        with open(input, "r") as file:
            rows = csv.DictReader(file)
            for i in rows:
                self.rows.append(i)

    def create(self, filename, data):
        with open(filename, "w", newline="") as file:
            for key, value in data.items():
                if key == "Months":
                    for key, value in value.items():
                        file.write(f"Number of transactions in {key}, {value}\n")
                    continue
                file.write(f"{key}, {value}\n")
