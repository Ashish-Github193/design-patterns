from uuid import uuid4


class DatabaseManager(object):
    def __new__(cls):
        if not hasattr(cls, "instance"):
            cls.instance_id = uuid4()
            cls.instance = super(DatabaseManager, cls).__new__(cls)
        return cls.instance

    def get_instance_id(self):
        return self.instance_id


if __name__ == "__main__":
    db1 = DatabaseManager()
    db1_repr = f"DatabaseManager instance id: {db1.get_instance_id()}"
    print(db1_repr, end="\n\n")

    db2 = DatabaseManager()
    db2_repr = f"DatabaseManager instance id: {db2.get_instance_id()}"
    print(db2_repr, end="\n\n")
