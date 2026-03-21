#!/bin/bash
# 初始化数据库：自动执行 deploy/ 目录下所有 SQL 脚本
# 用法: bash deploy/init_db.sh [env_file]
#   env_file: 环境变量文件路径，默认 .env

set -e

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
PROJECT_DIR="$(dirname "$SCRIPT_DIR")"
ENV_FILE="${1:-$PROJECT_DIR/.env}"

# 读取 .env 文件
if [ ! -f "$ENV_FILE" ]; then
    echo "错误: 找不到环境变量文件 $ENV_FILE"
    exit 1
fi

# 解析 .env 中的数据库配置
DB_HOST=$(grep -E '^DB_HOST=' "$ENV_FILE" | cut -d'=' -f2-)
DB_PORT=$(grep -E '^DB_PORT=' "$ENV_FILE" | cut -d'=' -f2-)
DB_USER=$(grep -E '^DB_USER=' "$ENV_FILE" | cut -d'=' -f2-)
DB_PASSWORD=$(grep -E '^DB_PASSWORD=' "$ENV_FILE" | cut -d'=' -f2-)

echo "数据库连接: ${DB_USER}@${DB_HOST}:${DB_PORT}"
echo "==============================="

# 执行 deploy 目录下所有 .sql 文件
for sql_file in "$SCRIPT_DIR"/*.sql; do
    [ -f "$sql_file" ] || continue
    filename=$(basename "$sql_file")
    echo "执行: $filename ..."
    mysql -h "$DB_HOST" -P "$DB_PORT" -u "$DB_USER" -p"$DB_PASSWORD" < "$sql_file"
    echo "完成: $filename"
done

echo "==============================="
echo "所有 SQL 脚本执行完毕"
