from app import User, Movie
from app import db

user = User(name='gao')

m1 = Movie(title='1', year='1994')
m2 = Movie(title='2', year='1994') # 就是因为之前的错误引用导致的读取错误！

db.session.add(user)
db.session.add(m1)
db.session.add(m2) # 注意这里只是加入了会话
db.session.commit()

