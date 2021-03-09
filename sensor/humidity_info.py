from datetime import date
from house_info import HouseInfo
from util.my_constants import HUMIDITY


class HumidityData(HouseInfo):

    def _convert_data(self, data):
        recs = []
        for rec in data:
            recs.append(float(rec) * 100)
        return recs

    def get_data_by_area(self, rec_area=0):
        recs = super().get_data_by_area(HUMIDITY, rec_area)
        return self._convert_data(recs)

    def get_data_by_date(self, rec_date=date.today()):
        recs = super().get_data_by_date(HUMIDITY, rec_date)
        return self._convert_data(recs)
