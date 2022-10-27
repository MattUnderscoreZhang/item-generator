from item_generator.db_session import get_engine, get_session
from item_generator.models import Base, Item


def recreate_all_tables() -> str:
    engine = get_engine()
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    return ""


def add_random_item() -> dict[str, str]:
    item = Item.random()
    session = get_session()
    session.add(item)
    session.commit()
    return item.as_dict()


def delete_items() -> str:
    n_items_deleted = get_session().query(Item).delete()
    return f"Deleted {n_items_deleted} items."


def get_items() -> list[dict[str, str]]:
    items = get_session().query(Item).all()
    return [item.as_dict() for item in items]


if __name__ == "__main__":
    recreate_all_tables()
    while True:
        add_random_item()
        items = get_session().query(Item).all()
        for item in items:
            print(item)
        # wait for user input
        input("Press enter to continue...")
