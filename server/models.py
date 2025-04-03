from sqlalchemy_serializer import SerializerMixin

class Zookeeper(db.Model, SerializerMixin):
    __tablename__ = 'zookeepers'
    serialize_rules = ('-animals.zookeeper',)

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)
    birthday = db.Column(db.Date)

    animals = db.relationship('Animal', back_populates='zookeeper')


class Enclosure(db.Model, SerializerMixin):
    __tablename__ = 'enclosures'
    serialize_rules = ('-animals.enclosure',)

    id = db.Column(db.Integer, primary_key=True)
    environment = db.Column(db.String)
    open_to_visitors = db.Column(db.Boolean)

    animals = db.relationship('Animal', back_populates='enclosure')


class Animal(db.Model, SerializerMixin):
    __tablename__ = 'animals'
    serialize_rules = ('-zookeeper.animals', '-enclosure.animals',)

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)
    species = db.Column(db.String)

    zookeeper_id = db.Column(db.Integer, db.ForeignKey('zookeepers.id'))
    enclosure_id = db.Column(db.Integer, db.ForeignKey('enclosures.id'))

    enclosure = db.relationship('Enclosure', back_populates='animals')
    zookeeper = db.relationship('Zookeeper', back_populates='animals')

    def __repr__(self):
        return f'<Animal {self.name}, a {self.species}>'
