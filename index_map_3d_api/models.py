from index_map_3d_api.extensions import db
import json


# Association tables
spatial_unit_ba_unit_association = db.Table('spatial_unit_ba_unit_association',
    db.Column('spatial_unit_id', db.Integer, db.ForeignKey('spatial_unit.id'), primary_key="True"),
    db.Column('ba_unit_id', db.Integer, db.ForeignKey('ba_unit.id'), primary_key="True")
)

mortgage_right_association = db.Table('mortgage_right_association',
    db.Column('mortgage_id', db.Integer, db.ForeignKey('mortgage.id'), primary_key="True"),
    db.Column('right_id', db.Integer, db.ForeignKey('right.id'), primary_key="True")
)

# Models
class SpatialUnit(db.Model):
    __tablename__ = 'spatial_unit'

    # Fields
    id = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.String)

    # Relationships
    ba_units = db.relationship("BAUnit", secondary="spatial_unit_ba_unit_association", lazy="subquery",
                                    backref=db.backref('spatial_unit_ba_unit_association', lazy=True))

    def __init__(self, id, address):
        self.id = id
        self.address = address

    def __repr__(self):
        return json.dumps(self.as_dict(), sort_keys=True, seperators=(',', ':'))

    def as_dict(self, embed=[]):
        result =  {
            "id": self.id,
            "address": self.address,
        }

        embeddable_objects = ['ba_units']
        for object_name in embeddable_objects:
            if object_name in embed:
                result[object_name] = [item.as_dict(embed=embed) for item in getattr(self, object_name)]

        return result


class BAUnit(db.Model):
    __tablename__ = 'ba_unit'

    # Fields
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)

    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __repr__(self):
        return json.dumps(self.as_dict())

    def as_dict(self, embed=[]):
        result = {
            "id": self.id,
            "name": self.name, 
            "rights": [right.as_dict() for right in self.rights],
            "restrictions": [restriction.as_dict() for restriction in self.restrictions],
            "responsibilities": [responsibility.as_dict() for responsibility in self.responsibilities]
        }

        embeddable_objects = ['spatial_unit']
        embeddable_lists = ['rights', 'restrictions', 'responsibilities']

        for object_name in embeddable_objects:
            if object_name in embed:
                result[object_name] = getattr(self, object_name).as_dict()

        for list_name in embeddable_lists:
            if list_name in embed:
                result[list_name] = [item.as_dict() for item in getattr(self, list_name)]

        return result


class Responsibility(db.Model):
    __tablename__ = 'responsibility'

    # Fields
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    description = db.Column(db.String)
    ba_unit_id = db.Column(db.Integer, db.ForeignKey('ba_unit.id'), nullable=False)
    type = db.Column(db.String)
    party_id = db.Column(db.Integer, db.ForeignKey('party.id'), nullable=True)

    # Relationships
    ba_unit = db.relationship("BAUnit", backref=db.backref('responsibilities', lazy='dynamic'), uselist=False)
    party = db.relationship("Party", back_populates="responsibilities")


    def __init__(self, id, ba_unit, description, interest, type, party=None):
        self.id = id
        self.ba_unit = ba_unit
        self.description = description
        self.type = type
        self.party = party

    def __repr__(self):
        return json.dumps(self.as_dict(), sort_keys=True, seperators=(',', ':'))

    def as_dict(self, embed=[]):
        result = {
            "responsibility_id": self.id,
            "description": self.description,
            "type": self.type,
            "party": self.party.as_dict() if self.party else None
        }

        embeddable_objects = ['ba_unit']

        for object_name in embeddable_objects:
            if object_name in embed:
                result[object_name] = getattr(self, object_name).as_dict()
        
        return result


class Right(db.Model):
    __tablename__ = 'right'

    # Fields
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    description = db.Column(db.String)
    type = db.Column(db.String)
    ba_unit_id = db.Column(db.Integer, db.ForeignKey('ba_unit.id'), nullable=False)
    party_id = db.Column(db.Integer, db.ForeignKey('party.id'), nullable=True)


    # Relationships
    ba_unit = db.relationship("BAUnit", backref=db.backref('rights', lazy='dynamic'), uselist=False)
    mortgages = db.relationship("Mortgage", secondary=mortgage_right_association, lazy='subquery',
        backref=db.backref('rights', lazy=True))
    party = db.relationship("Party", back_populates="rights")

    def __init__(self, id, ba_unit, description, type, mortgages, party=None):
        self.id = id
        self.ba_unit = ba_unit
        self.description = description
        self.type = type
        self.mortgages = mortgages
        self.party = party
    
    def __repr__(self):
        return json.dumps(self.as_dict(), sort_keys=True, seperators=(',', ':'))

    def as_dict(self, embed=[]):
        result = {
            "right_id": self.id,
            "description": self.description,
            "type": self.type,
            "party": self.party.as_dict() if self.party else None
        }

        embeddable_objects = ['ba_unit']
        embeddable_lists = ['mortgages']
        
        for object_name in embeddable_objects:
            if object_name in embed:
                result[object_name] = getattr(self, object_name).as_dict()
        for list_name in embeddable_lists:
            if list_name in embed:
                result[list_name] = [item.as_dict() for item in getattr(self, list_name)]

        return result


class Restriction(db.Model):
    __tablename__ = 'restriction'

    # Fields
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    description = db.Column(db.String)
    type = db.Column(db.String)
    ba_unit_id = db.Column(db.Integer, db.ForeignKey('ba_unit.id'), nullable=False)
    party_id = db.Column(db.Integer, db.ForeignKey('party.id'), nullable=True)
    # party_required = db.Column(db.Boolean) # REMOVE

    # Relationships 
    ba_unit = db.relationship("BAUnit", backref=db.backref('restrictions', lazy='dynamic'), uselist=False)
    party = db.relationship("Party", back_populates="restrictions")

    def __init__(self, id, ba_unit, description, type, party=None):
        self.id = id
        self.ba_unit = ba_unit
        self.description = description
        self.type = type
        self.party = party

    def __repr__(self):
        return json.dumps(self.as_dict(), sort_keys=True, seperators=(',', ':'))

    def as_dict(self):
        return {
            "restriction_id": self.id,
            "description": self.description,
            "type": self.type,
            "party": self.party.as_dict() if self.party else None
        }

# TODO - Remove?
class Mortgage(db.Model):
    __tablename__ = 'mortgage'

    # Fields
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    restriction_id = db.Column(db.Integer, db.ForeignKey('restriction.id'))
    type = db.Column(db.String)
    amount = db.Column(db.Integer)
    interest_rate = db.Column(db.Float)

    # Relationships
    restriction = db.relationship("Restriction", backref=db.backref('mortgages', lazy='dynamic'), uselist=False)

    def __init__(self, id, restriction, type, amount, interest_rate):
        self.id = id
        self.restriction = restriction
        self.type = type
        self.amount = amount
        self.interest_rate = interest_rate
    
    def __repr__(self):
        return json.dumps(self.as_dict(), sort_keys=True, seperators=(',', ':'))

    def as_dict(self, embed=[]):
        result = {
            "mortgage_id": self.id,
            "type": self.type,
            "amount": self.amount,
            "interest_rate": self.interest_rate
        }

        embeddable_objects = ['']
        for object_name in embeddable_objects:
            if object_name in embed:
                result[object_name] = getattr(self, object_name).as_dict()


class Party(db.Model):
    __tablename__ = 'party'

    # Fields
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    type = db.Column(db.String)

    # Relationships
    rights = db.relationship("Right", back_populates="party")
    restrictions = db.relationship("Restriction", back_populates="party")
    responsibilities = db.relationship("Responsibility", back_populates="party")

    def __init__(self, id, name, type):
        self.id = id
        self.name = name
        self.type = type
    
    def __repr__(self):
        return json.dumps(self.as_dict(), sort_keys=True, seperators=(',', ':'))

    def as_dict(self):
        return {
            "party_id": self.id,
            "name": self.name,
            "type": self.type
        }
