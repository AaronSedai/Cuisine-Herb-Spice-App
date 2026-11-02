from herb_data import herb_spice_details
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

def import_herbs():
    with Session(engine) as session:
        for name, details in herb_spice_details.items():
            herb = HerbSpice(
                name=name,
                flavor_profile=details['flavor-profile'],
                cuisine=", ".join(details['cuisine']),
                pairings=", ".join(details['pairings'])
            )
            session.add(herb)
        session.commit()
        print(f"Imported {len(herb_spice_details)} herbs and spices.")

def show_database_count():
    with Session(engine) as session:
        statement = select(HerbSpice)
        herbs = session.exec(statement).all()

        print(f"Herbs and spices in database: {len(herbs)}")

create_db_and_tables()
# show_schema()
# import_herbs()
show_database_count()