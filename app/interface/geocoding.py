"""
Geocoding Interface
@author Irfan Andriansyah <irfan@99.co>
"""
from abc import ABC
from typing import List, Any


class GeocodingItemsInterface(ABC):
    """
    Geocoding Items Interface
    """
    id: int
    title: str
    address: str
    additionalRegion: str
    province: str
    country: str

    def get_keyword(self):
        """
        Get keyword based on property in interface
        """
        keyword = [
            self.address, self.additionalRegion, self.province, self.country
        ]

        return ', '.join(
            GeocodingItemsInterface.remove_duplicate(keyword)
        ).replace('b\'', '').replace('\'', '')

    @staticmethod
    def remove_duplicate(keyword: List[str]) -> List[str]:
        """
        Remove duplicate array
        :param keyword: List[str]
        """
        response = []
        for item in keyword:
            if item not in response and item != '':
                response.append(item)

        return response


class GeocodingItemsParsedInterface(ABC):
    """
    Geocoding Items Parsed Interface
    """
    id: str
    administrative_area_level_1: str
    administrative_area_level_2: str
    administrative_area_level_3: str
    administrative_area_level_4: str
    lat: float
    lng: float

    def setter(
        self, id: int, administrative_area_level_1: str,
        administrative_area_level_2: str, administrative_area_level_3: str,
        administrative_area_level_4: str, lat: float, lng: float
    ):
        """
        Setter Interface
        """
        self.id = id
        self.administrative_area_level_1 = administrative_area_level_1
        self.administrative_area_level_2 = administrative_area_level_2
        self.administrative_area_level_3 = administrative_area_level_3
        self.administrative_area_level_4 = administrative_area_level_4
        self.lat = lat
        self.lng = lng

    def getter_csv(self):
        """
        Getter for format csv
        """
        field: List[Any] = [
            str(self.id), self.administrative_area_level_1,
            self.administrative_area_level_2, self.administrative_area_level_3,
            self.administrative_area_level_4,
            str(self.lat),
            str(self.lng)
        ]

        return '|'.join(field)

    @staticmethod
    def get_field():
        """
        Get Field Name
        """
        field: List[str] = [
            'id', 'administrative_area_level_1',
            'administrative_area_level_2', 'administrative_area_level_3',
            'administrative_area_level_4', 'lat', 'lng'
        ]

        return '|'.join(field)
