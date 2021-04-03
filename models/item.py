from db import db

class ItemModel(db.Model):
    __tablename__ = "items"

    id = db.Column(db.Integer, primary_key=True)
    file_name = db.Column(db.String(32))
    media_type = db.Column(db.String(32))
    created_at = db.Column(db.DateTime(), nullable=False)
    updated_at = db.Column(db.DateTime(), nullable=False)
    name_type = db.UniqueConstraint(file_name, media_type)

    def __init__(self, file_name, media_type, created_at, updated_at):
        self.file_name = file_name
        self.media_type = media_type
        self.created_at = created_at
        self.updated_at = updated_at

    def json(self):
        return {
            "id": self.id,
            "name": self.file_name,
            "media_type": self.media_type,
            "created_at": self.created_at.strftime("%Y-%m-%d %H:%M:%S:%f"),
            "updated_at": self.updated_at.strftime("%Y-%m-%d %H:%M:%S:%f")
        }

    @classmethod
    def find_by_name_type(cls, name, type):
        return cls.query.filter_by(file_name=name, media_type=type).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()