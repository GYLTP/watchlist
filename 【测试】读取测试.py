from app import Movie  # 导入模型类  其实读取的是数据库中的movie表
from app import db


movie = Movie.query.first() #

print(movie.title)

print(Movie.query.all())

print(Movie.query.count())


print(Movie.query.get(1)) # 获取键值为1记录

print(Movie.query.filter_by(title='Mahjong').first())



# 更新

movie = Movie.query.get(2) # 获得主键为2的记录

movie.title = "wall e"

movie.year = '2008'

db.session.commit()


# 删除
movie = Movie.query.get(1) # 构建实例
db.session.delete(movie)
db.session.commit()

#


