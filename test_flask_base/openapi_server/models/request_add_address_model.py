# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class RequestAddAddressModel(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, address=None):  # noqa: E501
        """RequestAddAddressModel - a model defined in OpenAPI

        :param address: The address of this RequestAddAddressModel.  # noqa: E501
        :type address: str
        """
        self.openapi_types = {
            'address': str
        }

        self.attribute_map = {
            'address': 'address'
        }

        self._address = address

    @classmethod
    def from_dict(cls, dikt) -> 'RequestAddAddressModel':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The RequestAddAddressModel of this RequestAddAddressModel.  # noqa: E501
        :rtype: RequestAddAddressModel
        """
        return util.deserialize_model(dikt, cls)

    @property
    def address(self):
        """Gets the address of this RequestAddAddressModel.


        :return: The address of this RequestAddAddressModel.
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this RequestAddAddressModel.


        :param address: The address of this RequestAddAddressModel.
        :type address: str
        """

        self._address = address
