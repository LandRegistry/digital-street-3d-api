from flask import Blueprint, Response, current_app, request
from sqlalchemy import exc
from digital_street_3d_api.exceptions import ApplicationError
from digital_street_3d_api.models import SpatialUnit, BAUnit, Party, Restriction, Responsibility, Right
from flask_negotiate import consumes, produces
import json

register_v1 = Blueprint('register_v1', __name__)


@register_v1.route("/spatial_units", methods=["GET"])
@produces("application/json")
def get_spatial_units():
    """Get a list of all SpatialUnits."""

    results = []

    query_result = SpatialUnit.query.all()

    # Format/Process
    embed_str = request.args.get('embed')
    objects_to_embed = embed_str.split(',') if embed_str else {}

    for item in query_result:
        results.append(item.as_dict(embed=objects_to_embed))

    return Response(response=json.dumps(results, sort_keys=True, separators=(',', ':')),
                    mimetype='application/json',
                    status=200)


@register_v1.route("/ba_units", methods=["GET"])
@produces("application/json")
def get_ba_units():
    """Get a list of all BAUnits."""

    results = []

    query_result = BAUnit.query.all()

    for item in query_result:
        results.append(item.as_dict())

    return Response(response=json.dumps(results, sort_keys=True, separators=(',', ':')),
                    mimetype='application/json',
                    status=200)


@register_v1.route("/rights", methods=["GET"])
@produces("application/json")
def get_rights():
    """Get a list of all Rights."""

    results = []

    query_result = Right.query.all()

    for item in query_result:
        results.append(item.as_dict(embed=['mortgages']))

    return Response(response=json.dumps(results, sort_keys=True, separators=(',', ':')),
                    mimetype='application/json',
                    status=200)


@register_v1.route("/restrictions", methods=["GET"])
@produces("application/json")
def get_restrictions():
    """Get a list of all Restrictions."""

    results = []

    query_result = Restriction.query.all()

    for item in query_result:
        results.append(item.as_dict())

    return Response(response=json.dumps(results, sort_keys=True, separators=(',', ':')),
                    mimetype='application/json',
                    status=200)


@register_v1.route("/responsibilities", methods=["GET"])
@produces("application/json")
def get_responsibilities():
    """Get a list of all Responsibilities."""

    results = []

    query_result = Responsibility.query.all()

    for item in query_result:
        results.append(item.as_dict())

    return Response(response=json.dumps(results, sort_keys=True, separators=(',', ':')),
                    mimetype='application/json',
                    status=200)


@register_v1.route("/parties", methods=["GET"])
@produces("application/json")
def get_parties():
    """Get a list of all Parties."""

    results = []

    query_result = Party.query.all()

    for item in query_result:
        results.append(item.as_dict())

    return Response(response=json.dumps(results, sort_keys=True, separators=(',', ':')),
                    mimetype='application/json',
                    status=200)
