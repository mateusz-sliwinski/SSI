import pandas as pd


class Object:
    values: list[any]
    decision: any

    def __init__(self, values: list[any], decision: any):
        self.values = values
        self.decision = decision


class DecisionSystem:
    __objects: list[Object] = []
    __attributes: list[str] = []
    __decision: list[bool] = []

    def __init__(self, read_txt: str, read_attributes: str) -> None:
        try:
            data_frame_attributes = pd.read_csv(f'{read_attributes}', header=None, sep='\t')
            data_frame = pd.read_csv(f'{read_txt}', header=None, sep=' ', names=data_frame_attributes[0],
                                     skipinitialspace=True)

            self.__attributes = data_frame.columns

            for col, row in data_frame.iterrows():
                data = row[:-1].astype(str)
                decision = row[-1:]

                self.__objects.append(Object(data.tolist(), decision))

            for col, row in data_frame_attributes.iterrows():
                if row[1] == 's':
                    self.__decision.append(True)
                else:
                    self.__decision.append(False)

        except FileNotFoundError:
            print('File not found')

    def get_all_objects(self) -> list[Object]:
        return self.__objects

    def get_attr_type(self, attr_pos: int) -> str:
        return self.__attributes[attr_pos]

    def get_attr_name(self) -> list[str]:
        return self.__attributes

    def get_all_object_float(self, list_column: list[int], list_row: list[int]) -> list[list[float]]:
        data = self.get_all_objects()
        data_df_value = pd.DataFrame()
        data_df_decision = pd.DataFrame()

        for item in data:
            df_helping = pd.DataFrame(item.values)
            data_df_value = pd.concat([data_df_value, df_helping], axis=1, ignore_index=True)

        data_df_value = data_df_value.T

        for item in data:
            df_helping = pd.DataFrame(item.decision)
            data_df_decision = pd.concat([data_df_decision, df_helping], axis=1, ignore_index=True)

        data_df_decision = data_df_decision.T

        data_df = pd.concat([data_df_value, data_df_decision], axis=1, ignore_index=True)
        data_df = data_df.iloc[list_column, list_row]
        data_df = data_df.astype(float)

        return data_df
