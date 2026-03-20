'''
数据库操作模块
'''
import logging
import aiomysql
from contextlib import asynccontextmanager
from models import CustomerInfo
from config import settings

logger = logging.getLogger(__name__)


class Database:
    """数据库连接池管理类"""

    def __init__(self):
        self.pool = None

    async def connect(self):
        """创建数据库连接池"""
        try:
            self.pool = await aiomysql.create_pool(
                host=settings.db_host,
                port=settings.db_port,
                user=settings.db_user,
                password=settings.db_password,
                db=settings.db_name,
                charset='utf8mb4',
                autocommit=True,
                minsize=1,
                maxsize=10
            )
            logger.info("Database connection pool created successfully")
        except Exception as e:
            logger.error(f"Failed to create database connection pool: {str(e)}")
            raise

    async def close(self):
        """关闭数据库连接池"""
        if self.pool:
            self.pool.close()
            await self.pool.wait_closed()
            logger.info("Database connection pool closed")

    @asynccontextmanager
    async def get_connection(self):
        """获取数据库连接的上下文管理器"""
        async with self.pool.acquire() as conn:
            yield conn


# 全局数据库实例
db = Database()


async def init_db():
    """初始化数据库连接"""
    await db.connect()


async def close_db():
    """关闭数据库连接"""
    await db.close()


# 客户信息数据库操作函数
async def create_customer(customer_info: CustomerInfo) -> bool:
    """保存客户信息到数据库"""
    sql = """
        INSERT INTO tb_customer_info (name, phone, company, email, requirements, created_at)
        VALUES (%s, %s, %s, %s, %s, %s)
    """
    try:
        async with db.get_connection() as conn:
            async with conn.cursor() as cursor:
                await cursor.execute(sql, (
                    customer_info.name,
                    customer_info.phone,
                    customer_info.company,
                    customer_info.email,
                    customer_info.requirements,
                    customer_info.created_at,
                ))
                return True
    except Exception as e:
        logger.error(f"Failed to create customer: {str(e)}")
        return False
