from sqlalchemy import create_engine, text

engine = create_engine('sqlite:///SQLAlchemy/db.sqlite3', echo=True)

with engine.connect() as con:
    with engine.begin():
        sql = text('select id, nome, preco from nucleo_produto')
        result = con.execute(sql)
    with engine.begin():
        sql = text('select id, nome, preco from nucleo_produto')
        result = con.execute(sql)


