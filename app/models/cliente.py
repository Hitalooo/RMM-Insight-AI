from app.extensions import db


class Cliente(db.Model):
    __tablename__ = "clientes"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    nome = db.Column(
        db.String(150),
        nullable=False,
        unique=True,
        index=True
    )

    ativo = db.Column(
        db.Boolean,
        nullable=False,
        default=True
    )

    observacoes = db.Column(
        db.Text,
        nullable=True
    )

    criado_em = db.Column(
        db.DateTime,
        server_default=db.func.now()
    )

    atualizado_em = db.Column(
        db.DateTime,
        server_default=db.func.now(),
        onupdate=db.func.now()
    )

    endpoints = db.relationship(
        "Endpoint",
        back_populates="cliente",
        cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"<Cliente {self.nome}>"