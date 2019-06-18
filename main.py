"""
Main App
@author Moch Nurhalimi ZD <moch.nurhalimi@gmail.com>
"""

import pandas as pd
from app.modules.cleansing import Cleansing
from app.common import config
import csv
import datetime
import pytz
import sys
from typing import List

from app.utils.config import ConfigHelper
from app.utils.logger import Logger
from app.factory.database import DatabaseFactory
from app.factory.http import HttpFactory
from app.models.property import PropertiesModel
from app.models.localities import LocalitiesModel
from app.interface.geocoding import GeocodingItemsInterface, \
    GeocodingItemsParsedInterface
from app.abstract.logger import LOGGER_TYPE


class MatchNewLocalities:
    """
    Match localities to get new localityID.
    """

    def __init__(self):
        CONFIG = ConfigHelper('config.conf')
        self.config: ConfigHelper = ConfigHelper('config.conf')
        self.logger: Logger = Logger(CONFIG, datetime, 'app-loging')
        self.db = DatabaseFactory('MySQL', self.config, self.logger)
        self.list_keyword_provinces = config.LIST_KEYWORD_PROVINCES
        self.list_keyword_cities = config.LIST_KEYWORD_CITIES
        self.list_keyword_districts = config.LIST_KEYWORD_DISTRICTS

        self.cleansing = Cleansing()

    def check_duplicate_district(self):
        """
        Check is there district that other city in each province .
        """
        print(
            self.localities_mv[(self.localities_mv.level == 3)
                               & (self.localities_mv.provinsi == 'Jakarta')]
            ['kecamatan'].value_counts()
        )

    def get_dataset(self, path, sep=','):
        """
        Get CSV dataset new localities.
        """
        return pd.read_csv(path, sep=sep)

    def clean_locality_mv(self):
        """
        Clean Localities MV.
        """
        self.localities_mv['provinces'] = self.localities_mv['provinsi'].apply(
            lambda x: self.cleansing.lower_locality(x)
        )

        self.localities_mv['cities'] = self.localities_mv['kabko'].apply(
            lambda x: self.cleansing.
            replace_locality(x, self.list_keyword_cities)
        )

        self.localities_mv['districts'] = self.localities_mv[
            'kecamatan'].apply(lambda x: self.cleansing.lower_locality(x))

        self.localities_mv['villages'] = self.localities_mv['desa'].apply(
            lambda x: self.cleansing.lower_locality(x)
        )

        return self.localities_mv

    def clean_localities_geo(self):
        """
        Clean localities from geocoding.
        """
        self.listing_location_from_geo[
            'provinces'] = self.listing_location_from_geo[
                'administrative_area_level_1'].apply(
                    lambda x: self.cleansing.
                    replace_locality(x, self.list_keyword_provinces)
                )

        self.listing_location_from_geo[
            'cities'] = self.listing_location_from_geo[
                'administrative_area_level_2'].apply(
                    lambda x: self.cleansing.
                    replace_locality(x, self.list_keyword_cities)
                )

        self.listing_location_from_geo[
            'districts'] = self.listing_location_from_geo[
                'administrative_area_level_3'].apply(
                    lambda x: self.cleansing.
                    replace_locality(x, self.list_keyword_districts)
                )

        self.listing_location_from_geo[
            'villages'] = self.listing_location_from_geo[
                'administrative_area_level_4'].apply(
                    lambda x: self.cleansing.
                    replace_locality(x, self.list_keyword_districts)
                )

        return self.listing_location_from_geo

    def select_localities_geo(self):
        """
        Select localities geo have cleaned.
        """
        return self.clean_geo_locality[[
            'id', 'provinces', 'cities', 'districts', 'villages', 'lat', 'lng'
        ]]

    def match_new_listing_locality(self):
        """
        Match and join data between listing locality from Google API and localities MV.
        """
        self.localities_mv = self.localities_mv[self.localities_mv.level == 3]
        return self.clean_geo_locality[[
            'id', 'provinces', 'cities', 'districts', 'villages', 'lat', 'lng'
        ]].merge(
            self.localities_mv[[
                'localityId', 'level', 'parentId', 'name', 'provinces',
                'cities', 'districts', 'villages'
            ]],
            on=['cities', 'districts'],
            how='inner'
        )

    def read_result_csv(self, filename="result.csv"):
        """
        Get result csv.
        """
        str_now = datetime.datetime.now(pytz.utc
                                        ).strftime("%Y-%m-%d'T'%H:%M:%S.%f")
        datas = list()
        line_count = 0
        try:
            with open("dataset/{}".format(filename)) as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=',')
                for row in csv_reader:
                    data = {
                        'propertyID': str(row[1]),
                        'localityMVID': str(row[8])
                    }
                    datas.append(data)
                    line_count += 1
                print('Processed {} lines.'.format(line_count))
        except Exception as e:
            print(e)

        return datas

    def update_listing(self, propertyID, newLocalityID):

        QUERY = self.db.query \
            .update(PropertiesModel) \
            .where(
                PropertiesModel.id == propertyID).values(localityMVId= newLocalityID)

    def run(self):

        # self.localities_mv = self.get_dataset(
        #     'dataset/localities/localitiesMV.csv'
        # )

        # self.listing_location_from_geo = self.get_dataset(
        #     'dataset/listing/output-2019-06-17.csv', '|'
        # )
        # self.listing_location_from_geo.fillna('')
        # self.clean_geo_locality = self.clean_localities_geo();
        # self.clean_geo_locality = self.select_localities_geo();
        # self.localities_mv.fillna('')
        # self.localities_mv = self.clean_locality_mv()
        # self.listing_new_locality = self.match_new_listing_locality()
        # self.listing_new_locality.to_csv('dataset/result.csv')

        # self.listing_new_localities = self.read_result_csv()
        # print(self.listing_new_localities)

        self.update_listing(100000503, 100)


if __name__ == "__main__":
    MatchNewLocalities().run()
