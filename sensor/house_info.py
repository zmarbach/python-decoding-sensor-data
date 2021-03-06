from datetime import date

from util.my_constants import AREA, DATE, MDY_FORMAT


class HouseInfo:
    def __init__(self, data):
        # data is a list of dicts
        self.data = data

    def get_data_by_area(self, field, rec_area=0):
        field_data = []
        # Add record to field_data if the value of rec_area is either 0 or equal to the record's area
        for record in self.data:
            if rec_area == 0:
                field_data.append(record[field])
            elif rec_area == int(record[AREA]):
                field_data.append(record[field])
        return field_data

    def get_data_by_date(self, field, rec_date=date.today()):
        field_data = []
        for record in self.data:
            if rec_date.strftime(MDY_FORMAT) == record[DATE]:
                field_data.append(record[field])
        return field_data
