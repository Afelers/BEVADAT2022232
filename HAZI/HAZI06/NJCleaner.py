import pandas as pd

class NJCleaner:
    
    def __init__(self, csv_path : str) -> None:
        self.data = pd.read_csv(csv_path)

    def order_by_scheduled_time(self):
        order = self.data.sort_values(by=['scheduled_time'])
        return order
    
    def drop_columns_and_nan(self):
        filtered = self.data.drop(columns=['from', 'to'])
        filtered = filtered.dropna()
        return filtered
    
    def convert_date_to_day(self):
        days = list(map(lambda x: pd.Timestamp(x).day_name(), self.data['date']))
        filtered = self.data.drop(columns=['date'])
        filtered['day'] = days
        return filtered

    def convert_scheduled_time_to_part_of_the_day(self):
        self.data['scheduled_time'] = pd.to_datetime(self.data['scheduled_time'])
        parts_of_the_day = list(map(lambda x: "late_night" if x.hour < 4 else ("early_morning" if x.hour < 8 else ("morning" if x.hour < 12 else ("afternoon" if x.hour < 16 else ("evening" if x.hour < 20 else "night")))), self.data['scheduled_time']))
        filtered = self.data.drop(columns=['scheduled_time'])
        filtered["part_of_the_day"] = parts_of_the_day
        return filtered
    
    def convert_delay(self):
        delays = list(map(lambda x: 0 if x < 5.0 else 1, self.data['delay_minutes']))
        output = self.data
        output['delay'] = delays
        return output
    
    def drop_unnecessary_columns(self):
        output = self.data.drop(columns=['train_id', 'actual_time', 'delay_minutes'])
        return output

    def save_first_60k(self, path : str):
        self.data.head(60000).to_csv(path, index=False)

    def prep_df(self, path='data/NJ.csv'):
        self.data = self.order_by_scheduled_time()
        self.data = self.drop_columns_and_nan()
        self.data = self.convert_date_to_day()
        self.data = self.convert_scheduled_time_to_part_of_the_day()
        self.data = self.convert_delay()
        self.data = self.drop_unnecessary_columns()
        self.save_first_60k(path)