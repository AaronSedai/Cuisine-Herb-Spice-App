from sqlmodel import SQLModel, Field, create_engine, Session, select

DATABASE_URL = "sqlite:///herb_spice.db"

engine = create_engine(DATABASE_URL)

class HerbSpice(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    flavor_profile: str
    cuisine: str
    pairings: str

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def add_test_herb():
    with Session(engine) as session:
        herb = HerbSpice(
            name='AllSpice',
            flavor_profile="combination of sweet, warm, woody, mild pepper notes with hints of cinnamon, clove, and nutmeg")
        session.add(herb)
        session.commit()

def show_herbs():
    with Session(engine) as session:
        statement = select(HerbSpice)
        herbs = session.exec(statement).all()

        for herb in herbs:
            print(herb)
def show_schema():
    print(HerbSpice.model_fields.keys())

create_db_and_tables()
show_schema()
# add_test_herb()
# show_herbs()