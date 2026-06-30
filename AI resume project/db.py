from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

DATABASE_URL =" mysql+mysqldb://2itGhoZU3UrRScR.root:i7nACzm1tgc4hvbw@gateway01.ap-southeast-1.prod.alicloud.tidbcloud.com:4000/sys?ssl_mode=VERIFY_IDENTITY&ssl_ca=<CA_PATH>"
engine =create_engine(
    DATABASE_URL,
    pool_pre_ping=True,
    connect_args={
        "ssl": {
            "ssl": True
            }
}
    ) 

sessionlocal = sessionmaker(bind=engine)
base = declarative_base()