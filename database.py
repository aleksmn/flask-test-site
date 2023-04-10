from sqlalchemy import create_engine, text
import os 

engine = create_engine(os.environ['DB_CONNECTION_STRING'],
  connect_args={
    "ssl": {
      "ssl_ca": "/etc/ssl/cert.pem"
    }
  })


def load_projects_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from projects"))
  
    result_dicts = []
  
    for row in result.all():
      result_dicts.append(row._mapping)
  
  
    return result_dicts




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







