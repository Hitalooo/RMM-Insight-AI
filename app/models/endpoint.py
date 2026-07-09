from app.extensions import db


class Endpoint(db.Model):

    __tablename__ = "endpoints"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    nome = db.Column(
        db.String(150),
        nullable=False
    )

    sistema_operacional = db.Column(
        db.String(100)
    )