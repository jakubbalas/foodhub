from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


class Ingredient(Base):
    pass


class Recipe(Base):
    pass


class MeasurementUnit(Base):
    pass
