# coding: utf-8

"""
    API Doc

    Onedoc is an innovative API solution for developers, offering a simple and secure way to create and manage PDF documents using familiar technologies like React.

    The version of the OpenAPI document: 1.0
    Generated by: https://konfigthis.com
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING
from pydantic import BaseModel, Field, RootModel


class DocumentGeneratePdfFromBucketRequest(BaseModel):
    # The title of the PDF, defaults to \"document\".
    title: typing.Optional[str] = Field(None, alias='title')

    # The identifier of the bucket.
    bucket: typing.Optional[str] = Field(None, alias='bucket')

    # The password of the bucket.
    password: typing.Optional[str] = Field(None, alias='password')

    # The username of the bucket.
    username: typing.Optional[str] = Field(None, alias='username')

    # Whether or not to generate a test PDF, defaults to true.
    test: typing.Optional[bool] = Field(None, alias='test')

    # Whether or not to save the PDF to the bucket, defaults to false.
    save: typing.Optional[bool] = Field(None, alias='save')

    # The expiration time of the PDF in days, default is 1 day.
    expires_in: typing.Optional[int] = Field(None, alias='expiresIn')
    class Config:
        arbitrary_types_allowed = True
