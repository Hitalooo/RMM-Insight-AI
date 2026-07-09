from app.extensions import db


class Alerta(db.Model):
    __tablename__ = "alertas"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    descricao = db.Column(
        db.String(255),
        nullable=False
    )