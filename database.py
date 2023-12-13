# database.py
from sqlalchemy import create_engine, Column, Integer, String, MetaData, Table, insert, select

class DataBase:
    def __init__(self, name_database='database'):
        self.name = name_database
        self.url = f"sqlite:///{name_database}.db"
        self.engine = create_engine(self.url)
        self.connection = self.engine.connect()
        self.metadata = MetaData()

    def create_table(self, name_table, **kwargs):
        columns = [Column(k, v, primary_key=True) if 'id_' in k else Column(k, v) for k, v in kwargs.items()]
        Table(name_table, self.metadata, *columns)
        self.metadata.create_all(self.engine)
        print(f"Table : '{name_table}' are created successfully")

    def read_table(self, name_table, return_keys=False):
        table = Table(name_table, self.metadata, autoload=True, autoload_with=self.engine)
        if return_keys:
            return table.columns.keys()
        else:
            return table

    def add_row(self, name_table, **kwargs):
        name_table = self.read_table(name_table)

        stmt = insert(name_table).values(kwargs)
        self.connection.execute(stmt)
        print('Row id added')

    def delete_row_by_id(self, name_table, id_):
        name_table = self.read_table(name_table)

        stmt = delete(name_table).where(name_table.c.id_ == id_)
        self.connection.execute(stmt)
        print(f'Row id {id_} deleted')

    def select_table(self, name_table):
        name_table = self.read_table(name_table)
        stm = select([name_table])
        return self.connection.execute(stm).fetchall()
