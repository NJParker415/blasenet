import logging
import numpy as np

from data.data_reader import BlaseReader


class Data:

    def __init__(self, data_type, params, specific_season=False):
        self.specific_season = specific_season
        self.data_type = data_type
        self.data_params = params

        if self.data_type == "blasenet":
            self.data_reader = BlaseReader(**params)
        else:
            logging.error('unsupported data type')
            raise ValueError('unsupported data type')

    def get_train_validate_test(self):
        """Return training, validation, and test sets"""
        return self.data_reader.get_train_validate_test()

    def get_train_test(self):
        """Return training and test sets"""
        x_train, x_validate, x_test, y_train, y_validate, y_test, columns = self.data_reader.get_train_validate_test()

        x_train = np.concatenate((x_train, x_validate))
        y_train = np.concatenate((y_train, y_validate))

        return x_train, x_test, y_train, y_test, columns

    def get_data(self):
        """Return the un-split dataset"""
        x = self.data_reader.x
        y = self.data_reader.y
        columns = self.data_reader.columns

        return x, y, columns

    def get_relevant_features(self):
        """Returns relevant data features if there are any"""
        if hasattr(self.data_reader, 'relevant_features'):
            return self.data_reader.get_relevant_features()
        else:
            return None
