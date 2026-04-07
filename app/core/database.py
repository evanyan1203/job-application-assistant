# 用来创建数据库连接（SQLite / PostgreSQL 等）
from sqlalchemy import create_engine

# ORM 相关工具：Base（模型基类）、session（操作数据库）
from sqlalchemy.orm import declarative_base, sessionmaker


# 这是数据库地址（SQLite 文件）
# sqlite:/// 表示使用 SQLite
# ./job_assistant.db 表示数据库文件在当前目录
DATABASE_URL = "sqlite:///./job_assistant.db"


# 创建数据库引擎（engine = 数据库连接核心）
engine = create_engine(
    DATABASE_URL,
    
    # SQLite 特有设置（允许多线程访问）
    connect_args={"check_same_thread": False}
)


# 创建一个“数据库会话工厂”
# 以后每次操作数据库，都要用它创建 session
SessionLocal = sessionmaker(
    autocommit=False,   # 不自动提交（我们自己控制）
    autoflush=False,    # 不自动刷新
    bind=engine         # 绑定到我们刚刚创建的 engine
)


# Base = 所有数据库模型的父类
# 你后面写的 User、Profile 都要继承它
Base = declarative_base()


# 这个函数是 FastAPI 专用（依赖注入）
# 每个请求都会拿到一个数据库 session
def get_db():
    db = SessionLocal()   # 创建一个数据库连接（session）
    try:
        yield db          # 把 db 提供给接口使用
    finally:
        db.close()        # 请求结束后关闭连接