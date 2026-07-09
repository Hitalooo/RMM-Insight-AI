from app.extensions import db


class Endpoint(db.Model):
    __tablename__ = "endpoints"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    cliente_id = db.Column(
        db.Integer,
        db.ForeignKey("clientes.id"),
        nullable=False,
        index=True
    )

    nome = db.Column(
        db.String(150),
        nullable=False
    )

    tipo_dispositivo = db.Column(
        db.String(50)
    )

    fabricante = db.Column(
        db.String(100)
    )

    modelo = db.Column(
        db.String(150)
    )

    numero_serie = db.Column(
        db.String(150)
    )

    sistema_operacional = db.Column(
        db.String(100)
    )

    usuario_logado = db.Column(
        db.String(150)
    )

    endereco_ip = db.Column(
        db.String(50)
    )

    status = db.Column(
        db.String(30),
        default="Online",
        index=True
    )

    ultima_comunicacao = db.Column(
        db.DateTime
    )

    uptime = db.Column(
        db.Integer
    )

    politica = db.Column(
        db.String(150)
    )

    memoria_ram = db.Column(
        db.Integer
    )

    disco_total = db.Column(
        db.Float
    )

    disco_livre = db.Column(
        db.Float
    )

    criado_em = db.Column(
        db.DateTime,
        server_default=db.func.now()
    )

    cliente = db.relationship(
        "Cliente",
        back_populates="endpoints"
    )

    alertas = db.relationship(
        "Alerta",
        back_populates="endpoint",
        cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"<Endpoint {self.nome}>"