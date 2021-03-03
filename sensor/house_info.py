from datetime import date, datetime

class HouseInfo:
    def __init__(self, data):
        # data is a list of dicts
        self._data = data

    def get_data_by_area(self, field, rec_area=0):
        field_data = []
        # Add record to field_data if the value of rec_area is either 0 or equal to the record's area
        for record in self._data:
            if rec_area == 0:
                field_data.append(record[field])
            elif rec_area == int(record['area']):
                field_data.append(record[field])
        return field_data

    def get_data_by_date(self, field, rec_date=date.today()):
        field_data = []
        for record in self._data:
            if date.strftime(rec_date, "%m/%d/%y") == record['date']:
                field_data.append(record[field])
        return field_data
