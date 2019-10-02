from index_map_3d_api.extensions import db
import json


class BAUnit(db.Model):
    __tablename__ = 'ba_unit'
    id = db.Column(db.Integer, primary_key=True)
    spatial_unit_id = db.Column(db.String)
    interests = db.relationship("Interest", back_populates="ba_unit")

    def __init__(self, id, spatial_unit_id, interests=None):
        self.id = id
        self.spatial_unit_id = spatial_unit_id
        self.interests = interests

    def __repr__(self):
        return json.dumps(self.as_dict())

    def as_dict(self):
        return {
            "id": self.id,
            "spatial_unit_id": self.spatial_unit_id

        }


class Interest(db.Model):
    __tablename__ = 'interest'
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String)
    ba_unit_id = db.Column(db.Integer, db.ForeignKey('ba_unit.id'))
    ba_unit = db.relationship("BAUnit", back_populates="interests")
    party = db.relationship("Party", back_populates="interests")

    def __init__(self, id, description, ba_unit_id, ba_unit, party):
        self.id = id
        self.description = description
        self.ba_unit_id = ba_unit_id
        self.ba_unit = ba_unit
        self.party = party

    def __repr__(self):
        return json.dumps(self.as_dict())

    def as_dict(self):
        return {
            "id": self.id,
            "description": self.description,
            "ba_unit_id": self.ba_unit_id,
            "ba_unit": self.ba_unit_id,
            "party": self.party
        }


class Responsibility(db.Model):
    __tablename__ = 'responsibility'
    id = db.Column(db.Integer, db.ForeignKey('interest.id'), primary_key=True)
    type = db.Column(db.String)

    def __init__(self, id, type):
        self.id = id,
        self.type = type

    def __repr__(self):
        return json.dumps(self.as_dict())

    def as_dict(self):
        return {
            "id": self.id,
            "type": self.type
        }


class Right(db.Model):
    __tablename__ = 'right'
    id = db.Column(db.Integer, db.ForeignKey('interest.id'), primary_key=True)
    type = db.Column(db.String)
    mortgages = db.relationship("Mortgage", back_populates="rights")

    def __init__(self, id, type, mortgages):
        self.id = id
        self.type = type
        self.mortgages = mortgages
    
    def __repr__(self):
        return json.dumps(self.as_dict())

    def as_dict(self):
        return {
            "id": self.id,
            "type": self.type,
            "mortgages": self.mortgages
        }


class Restriction(db.Model):
    __tablename__ = 'restriction'
    id = db.Column(db.Integer, db.ForeignKey('interest.id'), primary_key=True)
    type = db.Column(db.String)
    party_required = db.Column(db.Boolean)

    def __init__(self, id, type, party_required):
        self.id = id
        self.type = type
        self.party_required = party_required

    def __repr__(self):
        return json.dumps(self.as_dict())

    def as_dict(self):
        return {
            "id": self.id,
            "type": self.type,
            "party_required": self.party_required
        }

class Mortgage(db.Model):
    __tablename__ = 'mortgage'
    id = db.Column(db.Integer, db.ForeignKey('restriction.id'), primary_key=True)
    type = db.Column(db.String)
    amount = db.Column(db.Integer)
    interest_rate = db.Column(db.Float)
    rights = db.relationship("Right", back_populates="mortgages")

    def __init__(self, id, type, amount, interest_rate, rights):
        self.id = id
        self.type = type
        self.amount = amount
        self.interest_rate = interest_rate
        self.rights = rights
    
    def __repr__(self):
        return json.dumps(self.as_dict())

    def as_dict(self):
        return {
            "id": self.id,
            "type": self.type,
            "amount": self.amount,
            "interest_rate": self.interest_rate,
            "rights": self.rights
        }


class Party(db.Model):
    __tablename__ = 'party'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    type = db.Column(db.String)
    interests = db.relationship("Interest", back_populates="party")

    def __init__(self, id, name, type, interests):
        self.id = id
        self.name = name
        self.type = type
        self.interests = interets
    
    def __repr__(self):
        return json.dumps(self.as_dict())

    def as_dict(self):
        return {
            "id": self.id,
            "type": self.type,
            "interests": self.interests
        }
