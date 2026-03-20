from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # MySQL数据库配置
    db_host: str = "localhost"
    db_port: int = 3306
    db_user: str = "jusi"
    db_password: str
    db_name: str = "jusi_db"

    # 其他配置项
    api_vstr: str = "/api/v1"
    app_name: str = "JUSI CMS"
    app_version: str = "1.0.0"
    bind_addr: str = "0.0.0.0"
    bind_port: int = 13102
    debug: bool = True
    
    # 指定配置文件和相关参数
    class Config:
        env_file = ".env"
        env_file_encoding = 'utf-8'
        case_sensitive = False

# 创建配置实例
settings = Settings()
