from house_info import HouseInfo
from datetime import date, datetime
from util.my_constants import TEMPERATURE



class TemperatureData(HouseInfo):

    def _convert_data(self, data):
        recs = []
        for rec in data:
            recs.append(int(rec, base=10))
        return recs

    def get_data_by_area(self, rec_area=0):
        recs = super().get_data_by_area(TEMPERATURE, rec_area)
        return self._convert_data(recs)

    def get_data_by_date(self, rec_date=date.today()):
        recs = super().get_data_by_date(TEMPERATURE, rec_date)
        return self._convert_data(recs)
