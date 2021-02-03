# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_tea_util import models as util_models
from alibabacloud_yanhjtest20200202 import models as yanhj_test_20200202_models
from alibabacloud_openapi_util.client import Client as OpenApiUtilClient


class Client(OpenApiClient):
    """
    *\
    """
    def __init__(
        self, 
        config: open_api_models.Config,
    ):
        super().__init__(config)
        self._endpoint_rule = ''
        self.check_config(config)
        self._endpoint = self.get_endpoint('yanhjtest', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(
        self,
        product_id: str,
        region_id: str,
        endpoint_rule: str,
        network: str,
        suffix: str,
        endpoint_map: Dict[str, str],
        endpoint: str,
    ) -> str:
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def send_commond_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> yanhj_test_20200202_models.SendCommondResponse:
        req = open_api_models.OpenApiRequest()
        return yanhj_test_20200202_models.SendCommondResponse().from_map(
            self.do_rpcrequest('SendCommond', '2020-02-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def send_commond_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> yanhj_test_20200202_models.SendCommondResponse:
        req = open_api_models.OpenApiRequest()
        return yanhj_test_20200202_models.SendCommondResponse().from_map(
            await self.do_rpcrequest_async('SendCommond', '2020-02-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def send_commond(self) -> yanhj_test_20200202_models.SendCommondResponse:
        runtime = util_models.RuntimeOptions()
        return self.send_commond_with_options(runtime)

    async def send_commond_async(self) -> yanhj_test_20200202_models.SendCommondResponse:
        runtime = util_models.RuntimeOptions()
        return await self.send_commond_with_options_async(runtime)

    def get_all_product_with_options(
        self,
        request: yanhj_test_20200202_models.GetAllProductRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yanhj_test_20200202_models.GetAllProductResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return yanhj_test_20200202_models.GetAllProductResponse().from_map(
            self.do_rpcrequest('GetAllProduct', '2020-02-02', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def get_all_product_with_options_async(
        self,
        request: yanhj_test_20200202_models.GetAllProductRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yanhj_test_20200202_models.GetAllProductResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return yanhj_test_20200202_models.GetAllProductResponse().from_map(
            await self.do_rpcrequest_async('GetAllProduct', '2020-02-02', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def get_all_product(
        self,
        request: yanhj_test_20200202_models.GetAllProductRequest,
    ) -> yanhj_test_20200202_models.GetAllProductResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_all_product_with_options(request, runtime)

    async def get_all_product_async(
        self,
        request: yanhj_test_20200202_models.GetAllProductRequest,
    ) -> yanhj_test_20200202_models.GetAllProductResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_all_product_with_options_async(request, runtime)
