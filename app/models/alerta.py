from app.extensions import db


class Alerta(db.Model):
    __tablename__ = "alertas"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    endpoint_id = db.Column(
        db.Integer,
        db.ForeignKey("endpoints.id"),
        nullable=False,
        index=True
    )

    tipo = db.Column(
        db.String(100),
        nullable=False
    )

    severidade = db.Column(
        db.String(30),
        nullable=False,
        index=True
    )

    descricao = db.Column(
        db.Text,
        nullable=False
    )

    status = db.Column(
        db.String(30),
        nullable=False,
        default="Aberto",
        index=True
    )

    data_alerta = db.Column(
        db.DateTime,
        server_default=db.func.now()
    )

    endpoint = db.relationship(
        "Endpoint",
        back_populates="alertas"
    )

    def __repr__(self):
        return f"<Alerta {self.tipo}>"