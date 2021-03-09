from datetime import date
from house_info import HouseInfo
from util.my_constants import PARTICULATE


class ParticleData(HouseInfo):
    GOOD = "good"
    MODERATE = "moderate"
    BAD = "bad"

    def _convert_data(self, data):
        recs = []
        for rec in data:
            recs.append(float(rec))
        return recs

    def get_data_by_area(self, rec_area=0):
        recs = super().get_data_by_area(PARTICULATE, rec_area)
        return self._convert_data(recs)

    def get_data_by_date(self, rec_date=date.today()):
        recs = super().get_data_by_date(PARTICULATE, rec_date)
        return self._convert_data(recs)

    def get_data_concentrations(self, data):
        particulate = {
            self.GOOD: 0,
            self.MODERATE: 0,
            self.BAD: 0
        }

        # data being passed in will be a list of floats because already converted
        for rec in data:
            if rec <= 50.0:
                particulate[self.GOOD] = particulate.get(self.GOOD) + 1
            elif 50.0 < rec <= 100.0:
                particulate[self.MODERATE] = particulate.get(self.MODERATE) + 1
            else:
                particulate[self.BAD] = particulate.get(self.BAD) + 1

        return particulate
