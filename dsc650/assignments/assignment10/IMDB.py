from pathlib import Path
import os
from IPython.display import clear_output


class IMDB_Dataset():
    def __init__(self):
        current_path = Path(os.getcwd()).resolve().parents[2]
        data_path = current_path.joinpath('data/external/imdb/aclImdb')
        self.train_dir = data_path.joinpath('train')
        self.test_dir = data_path.joinpath('test')
        self.print_dict = {"pos_train": "-" * 100, "neg_train": "-" * 100, "pos_test": "-" * 100, "neg_test": "-" * 100}

    def _load_train_data(self):
        labels = []
        text = []
        label_dict = {'pos': 1, 'neg': 0}

        # For each of the labels
        for label in ['pos', 'neg']:
            i = 0
            # Create a new directory for each label
            label_dir = self.train_dir.joinpath(label)
            # And find all the files within that directory
            for file_name in os.listdir(label_dir):
                # Create another directory for each file
                file_path = label_dir.joinpath(file_name)
                # And open that file
                with open(file_path, 'r', encoding="utf8") as file:
                    # Append the contents to the text list
                    clear_output(wait=True)
                    text.append(file.read())
                    self.print_dict[f'{label}_train'.split('=')[0]] = "#" * (int(100 * i / 12499)) + "-" * (
                        int(100 * (12500 - i) / 12499))
                    for key, val in self.print_dict.items():
                        print(f"{key: <10}: [{val: <100}]")
                    # Add the label to the label list
                    labels.append(label_dict[label])
                    i += 1
        return text, labels

    def _load_test_data(self):
        labels = []
        text = []
        label_dict = {'pos': 1, 'neg': 0}

        # For each of the labels
        for label in ['pos', 'neg']:
            i = 0
            # Create a new directory for each label
            label_dir = self.test_dir.joinpath(label)
            # And find all the files within that directory
            for file_name in os.listdir(label_dir):
                # Create another directory for each file
                file_path = label_dir.joinpath(file_name)
                # And open that file
                with open(file_path, 'r', encoding="utf8") as file:
                    # Append the contents to the text list
                    clear_output(wait=True)
                    text.append(file.read())
                    self.print_dict[f'{label}_test'.split('=')[0]] = "#" * (int(100 * i / 12499)) + "-" * (
                        int(100 * (12500 - i) / 12499))
                    for key, val in self.print_dict.items():
                        print(f"{key: <10}: [{val: <100}]")
                    # Add the label to the label list
                    labels.append(label_dict[label])
                    i += 1
        return text, labels

    def load_data(self):
        X_train, y_train = self._load_train_data()
        X_test, y_test = self._load_test_data()
        return (X_train, y_train), (X_test, y_test)
