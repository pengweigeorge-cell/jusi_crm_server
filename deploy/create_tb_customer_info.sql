-- 创建 jusi_db 数据库（如果不存在）
CREATE DATABASE IF NOT EXISTS jusi_db DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

USE jusi_db;

-- 创建客户信息表 tb_customer_info
CREATE TABLE IF NOT EXISTS tb_customer_info (
    id INT AUTO_INCREMENT PRIMARY KEY COMMENT '自增主键',
    name VARCHAR(64) NOT NULL COMMENT '姓名/称呼',
    phone VARCHAR(20) NOT NULL COMMENT '手机号',
    company VARCHAR(128) DEFAULT '' COMMENT '公司/机构名称',
    email VARCHAR(128) DEFAULT '' COMMENT '电子邮箱',
    requirements TEXT DEFAULT NULL COMMENT '客户需求',
    created_at BIGINT NOT NULL COMMENT '创建时间戳（秒）',
    INDEX idx_phone (phone),
    INDEX idx_created_at (created_at)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci COMMENT='客户信息表';
