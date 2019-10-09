from index_map_3d_api.extensions import db
import json


# Mapping tables
spatial_unit_ba_unit_mapping = db.Table('spatial_unit_ba_unit_mapping',
    db.Column('spatial_unit_id', db.Integer, db.ForeignKey('spatial_unit.id'), primary_key="True"),
    db.Column('ba_unit_id', db.Integer, db.ForeignKey('ba_unit.id'), primary_key="True")
)

mortgage_right_mapping = db.Table('mortgage_right_mapping',
    db.Column('mortgage_id', db.Integer, db.ForeignKey('mortgage.id'), primary_key="True"),
    db.Column('right_id', db.Integer, db.ForeignKey('right.id'), primary_key="True")
)

# Models
class BAUnit(db.Model):
    __tablename__ = 'ba_unit'

    # Fields
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)

    # Relationships
    interests = db.relationship("Interest", back_populates="ba_unit")

    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __repr__(self):
        return json.dumps(self.as_dict())

    def as_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "interests": [interest.as_dict() for interest in self.interests]
            # TODO - return interests
        }


class SpatialUnit(db.Model):
    __tablename__ = 'spatial_unit'

    # Fields
    id = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.String)

    # Relationships
    ba_units = db.relationship("BAUnit", secondary="spatial_unit_ba_unit_mapping", lazy="subquery",
                                    backref=db.backref('spatial_unit_ba_unit_mapping', lazy=True))

    def __init__(self, id, address):
        self.id = id
        self.address = address

    def __repr__(self):
        return json.dumps(self.as_dict(), sort_keys=True, seperators=(',', ':'))

    def as_dict(self):
        return {
            "id": self.id,
            "address": self.address,
            "interests": [ba_unit.as_dict() for ba_unit in self.ba_units]
        }

class Interest(db.Model):
    __tablename__ = 'interest'

    # Fields
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    description = db.Column(db.String)
    ba_unit_id = db.Column(db.Integer, db.ForeignKey('ba_unit.id'), nullable=False)

    # Relationships
    # ba_unit = db.relationship("BAUnit", backref=db.backref('interests', lazy='dynamic'), uselist=False)
    ba_unit = db.relationship("BAUnit", uselist=False)
    # party = db.relationship("Party", back_populates="interests", uselist=False)

    def __init__(self, id, description, ba_unit, party):
        self.id = id
        self.description = description
        self.ba_unit = ba_unit
        # self.party = party

    def __repr__(self):
        return json.dumps(self.as_dict(), sort_keys=True, seperators=(',', ':'))

    def as_dict(self):
        return {
            "id": self.id,
            "description": self.description,
            # "ba_unit": self.ba_unit.as_dict()
            # "party": self.party
        }


class Responsibility(db.Model):
    __tablename__ = 'responsibility'

    # Fields
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    interest_id = db.Column(db.Integer, db.ForeignKey('interest.id'))
    type = db.Column(db.String)

    # Relationships
    interest = db.relationship("Interest", backref=db.backref('responsibilities', lazy='dynamic'), uselist=False)

    def __init__(self, id, interest, type):
        self.id = id,
        self.interest = interest,
        self.type = type

    def __repr__(self):
        return json.dumps(self.as_dict(), sort_keys=True, seperators=(',', ':'))

    def as_dict(self):
        return {
            "id": self.id,
            "interest": self.interest.as_dict(),
            "type": self.type
        }


class Right(db.Model):
    __tablename__ = 'right'

    # Fields
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    interest_id = db.Column(db.Integer, db.ForeignKey('interest.id'))
    type = db.Column(db.String)

    # Relationships
    interest = db.relationship("Interest", backref=db.backref('rights', lazy='dynamic'), uselist=False)
    mortgages = db.relationship("Mortgage", secondary=mortgage_right_mapping, lazy='subquery',
        backref=db.backref('rights', lazy=True))

    def __init__(self, id, interest, type, mortgages):
        self.id = id
        self.interest = interest
        self.type = type
        self.mortgages = mortgages
    
    def __repr__(self):
        return json.dumps(self.as_dict(), sort_keys=True, seperators=(',', ':'))

    def as_dict(self):
        return {
            "id": self.id,
            "interest": self.interest.as_dict(),
            "type": self.type,
            "mortgages": self.mortgages
        }


class Restriction(db.Model):
    __tablename__ = 'restriction'

    # Fields
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    interest_id = db.Column(db.Integer, db.ForeignKey('interest.id'))
    type = db.Column(db.String)
    party_required = db.Column(db.Boolean)

    interest = db.relationship("Interest", backref=db.backref('restrictions', lazy='dynamic'), uselist=False)

    def __init__(self, id, interest, type, party_required):
        self.id = id
        self.interest = interest
        self.type = type
        self.party_required = party_required

    def __repr__(self):
        return json.dumps(self.as_dict(), sort_keys=True, seperators=(',', ':'))

    def as_dict(self):
        return {
            "id": self.id,
            "interest": self.interest.as_dict(),
            "type": self.type,
            "party_required": self.party_required
        }

class Mortgage(db.Model):
    __tablename__ = 'mortgage'

    # Fields
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    restriction_id = db.Column(db.Integer, db.ForeignKey('restriction.id'))
    type = db.Column(db.String)
    amount = db.Column(db.Integer)
    interest_rate = db.Column(db.Float)

    # Relationships
    # rights = db.relationship("Right", back_populates="mortgages")

    def __init__(self, id, restriction_id, type, amount, interest_rate):
        self.id = id
        self.restriction_id = restriction_id
        self.type = type
        self.amount = amount
        self.interest_rate = interest_rate
        # self.rights = rights
    
    def __repr__(self):
        return json.dumps(self.as_dict(), sort_keys=True, seperators=(',', ':'))

    def as_dict(self):
        return {
            "id": self.id,
            "restriction_id": self.restriction_id,
            "type": self.type,
            "amount": self.amount,
            "interest_rate": self.interest_rate
            # "rights": self.rights
        }


class Party(db.Model):
    __tablename__ = 'party'

    # Fields
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    type = db.Column(db.String)

    # Relationships
    # interests = db.relationship("Interest", back_populates="party")

    def __init__(self, id, name, type):
        self.id = id
        self.name = name
        self.type = type
        # self.interests = interests
    
    def __repr__(self):
        return json.dumps(self.as_dict(), sort_keys=True, seperators=(',', ':'))

    def as_dict(self):
        return {
            "id": self.id,
            "type": self.type
            # "interests": self.interests
        }
