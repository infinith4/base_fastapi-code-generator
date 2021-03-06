# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class RequestSignupConfirmModel(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, signup_token=None):  # noqa: E501
        """RequestSignupConfirmModel - a model defined in OpenAPI

        :param signup_token: The signup_token of this RequestSignupConfirmModel.  # noqa: E501
        :type signup_token: str
        """
        self.openapi_types = {
            'signup_token': str
        }

        self.attribute_map = {
            'signup_token': 'signup_token'
        }

        self._signup_token = signup_token

    @classmethod
    def from_dict(cls, dikt) -> 'RequestSignupConfirmModel':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The RequestSignupConfirmModel of this RequestSignupConfirmModel.  # noqa: E501
        :rtype: RequestSignupConfirmModel
        """
        return util.deserialize_model(dikt, cls)

    @property
    def signup_token(self):
        """Gets the signup_token of this RequestSignupConfirmModel.


        :return: The signup_token of this RequestSignupConfirmModel.
        :rtype: str
        """
        return self._signup_token

    @signup_token.setter
    def signup_token(self, signup_token):
        """Sets the signup_token of this RequestSignupConfirmModel.


        :param signup_token: The signup_token of this RequestSignupConfirmModel.
        :type signup_token: str
        """

        self._signup_token = signup_token
