# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List


class SendCommondResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SendCommondResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SendCommondResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = SendCommondResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAllProductRequest(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        product: str = None,
        env: str = None,
    ):
        # requestId
        self.request_id = request_id
        # pop产品
        self.product = product
        # 环境
        self.env = env

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.product is not None:
            result['Product'] = self.product
        if self.env is not None:
            result['Env'] = self.env
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Product') is not None:
            self.product = m.get('Product')
        if m.get('Env') is not None:
            self.env = m.get('Env')
        return self


class GetAllProductResponseBodyData(TeaModel):
    def __init__(
        self,
        description: str = None,
        domains: List[str] = None,
        name_space: str = None,
        product: str = None,
        type: str = None,
    ):
        # description
        self.description = description
        # 域名
        self.domains = domains
        # nameSpace
        self.name_space = name_space
        # product
        self.product = product
        # type
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.domains is not None:
            result['Domains'] = self.domains
        if self.name_space is not None:
            result['NameSpace'] = self.name_space
        if self.product is not None:
            result['Product'] = self.product
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Domains') is not None:
            self.domains = m.get('Domains')
        if m.get('NameSpace') is not None:
            self.name_space = m.get('NameSpace')
        if m.get('Product') is not None:
            self.product = m.get('Product')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class GetAllProductResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetAllProductResponseBodyData = None,
        request_id: str = None,
        success: bool = None,
    ):
        # code
        self.code = code
        # 产品信息
        self.data = data
        # Id of the request
        self.request_id = request_id
        # success
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = GetAllProductResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetAllProductResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetAllProductResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetAllProductResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


