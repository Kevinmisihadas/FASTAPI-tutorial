import mongoengine
def initialize_db() ->None:
    """initialize the database"""
    mongoengine.connect(
        host="mongodb://localhost:27017",
        db="netflix",
        

    )