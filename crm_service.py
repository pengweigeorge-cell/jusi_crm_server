'''
JUSI CRM (Customer Relationship Management) 服务接口
'''
import re
import logging
from fastapi import APIRouter
from models import (
    CustomerInfo,
    ResponseModel,
)

from mysql_client import create_customer

logger = logging.getLogger(__name__)

crm_router = APIRouter()

PHONE_REGEX = re.compile(r'^1[3-9]\d{9}$')
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')


@crm_router.post("/customer_info", response_model=ResponseModel)
async def save_customer_info(customer_info: CustomerInfo):
    """保存客户留资信息"""
    # 校验手机号格式
    if not PHONE_REGEX.match(customer_info.phone):
        return ResponseModel(code=400, message="手机号格式不正确")

    # 校验邮箱格式（如果提供了邮箱）
    if customer_info.email and not EMAIL_REGEX.match(customer_info.email):
        return ResponseModel(code=400, message="邮箱格式不正确")

    result = await create_customer(customer_info)
    if not result:
        return ResponseModel(code=500, message="保存客户信息失败")

    return ResponseModel(code=200, message="ok")
