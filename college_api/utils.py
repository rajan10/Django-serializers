class College:
    def __init__(self, id, name, location, phone):
        self.id=id
        self.name=name
        self.location=location
        self.phone=phone

    def __str__(self):
        return f"College:{self.name}"