from pydantic import BaseModel
from typing import Optional
from utils import current_timestamp


# 客户信息
class CustomerInfo(BaseModel):
    name: str  # 姓名 / 称呼
    phone: str  # 手机号
    company: Optional[str] = "" # 公司 / 机构名称
    email: Optional[str] = ""   # 电子邮箱
    requirements: Optional[str] = ""  # 客户需求
    created_at: int = current_timestamp()


# 通用响应模型
class ResponseModel(BaseModel):
    code: int = 200
    message: str = "ok"
