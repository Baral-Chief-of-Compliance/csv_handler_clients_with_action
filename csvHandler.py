import pandas as pd


#класс для работы с данными
class csvHandler(object):

    data : pd.DataFrame

    #загрузка дата фрейма из файла по пути
    def load_data(self, file_path: str) -> None:
        try:
            self.data = pd.read_csv(file_path)
        except:
            print("не удалась загрузить данные")

    
    def __init__(self, file_path: str):
        self.load_data(file_path)

    
    #Агрегации данных по клиентам, подсчета числа действий каждого клиента.
    def count_client_action(self, client_id:int) -> pd.DataFrame:
        data_client : pd.DataFrame  = self.data.loc[self.data['client_id'] == client_id]
        return data_client.groupby(['action']).agg({'action': ['count']})
    

    #Фильтрации данных по определенным критериям (например, только действия оформления заказа).
    def filter_crireria(self, criteria_name: str, value) -> pd.DataFrame:
        column_table = [column for column in self.data]
        
        for column in column_table:
            if criteria_name == column:
                return self.data.loc[self.data[f'{criteria_name}'] == value]


    # - Определите среднее число действий клиентов.
    # - Найдите топ-5 клиентов с наибольшим числом действий.
    def analyze_client_behavior(self) -> pd.DataFrame:
        clients_action_counts = self.data.groupby(['client_id']).agg(count_action=('action', 'count'))
        top_5_clients = clients_action_counts.sort_values(['client_id', 'count_action']).groupby('client_id').head(5)
        mean_counts = clients_action_counts.agg(mean_action=('count_action', 'mean'))
        return pd.concat([mean_counts, top_5_clients])
    

    #сохранение обработанных данных
    def save_processed_data(self,dataPd: pd.DataFrame, out_file_path: str) -> None:
        dataPd.to_csv(out_file_path)


    #возвращение данных
    def show_data(self) -> pd.DataFrame:
        return self.data