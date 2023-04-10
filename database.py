from sqlalchemy import create_engine, text

engine = create_engine(  "mysql+pymysql://9sd7fxi27uqit0x4rdno:pscale_pw_9bp8okXLxGatTvKEP49iYZXPkBWzFVrYvIhi3enmgMw@aws.connect.psdb.cloud/flask-test-site?charset=utf8mb4",
  connect_args={
    "ssl": {
      "ssl_ca": "/etc/ssl/cert.pem"
    }
  })

# with engine.connect() as conn:
#   result = conn.execute(text("select * from projects"))
#   # print(result.all())

#   # HOW to get dict from SQLAlchemy row
#   # row = result.all()[0]
#   # print(row._mapping)


#   result_dicts = []

#   for row in result.all():
#     result_dicts.append(row._mapping)


#   print(result_dicts)







