import pandas as pd

class NJCleaner:
    
    def __init__(self, csv_path : str) -> None:
        self.data = pd.read_csv(csv_path)

    def order_by_scheduled_time(self):
        order = self.data.sort_values(by=['scheduled_time'])
        return order
    
    def prep_df(self, save_csv_path : str):
        self.data = self.order_by_scheduled_time()

        #...
        #...
        #...

        self.data.to_csv(save_csv_path)