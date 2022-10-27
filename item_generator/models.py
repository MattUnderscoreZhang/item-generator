import random
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

from item_generator import items


Base = declarative_base()


class SerializableBase(Base):
    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class Item(SerializableBase):
    __tablename__ = "item"

    id = Column(Integer, primary_key=True)
    name = Column(String(200))
    price = Column(Integer)
    description = Column(String)

    def __repr__(self) -> str:
        return f"{self.name}: {self.price} gold\n\t{self.description}"

    @staticmethod
    def random() -> 'Item':
        rarity = random.random()
        rarity = "common" if rarity < 0.8 else "uncommon" if rarity < 0.95 else "rare"
        name = f"{random.choice(items.creatures[rarity])} {random.choice(items.body_part)}"
        price = random.randint(1, 100) if rarity == "common" else random.randint(100, 1000) if rarity == "uncommon" else random.randint(1000, 10000)
        return Item(
            name=name,
            price=price,
            description=f"{rarity[0].upper() + rarity[1:]} ingredient item."
        )
