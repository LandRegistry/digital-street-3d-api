from flask import Blueprint, Response, current_app, request
from sqlalchemy import exc
from index_map_3d_api.models import SpatialUnit, BAUnit, Interest, Party, Restriction, Responsibility, Right, Mortgage
from flask_negotiate import consumes, produces
import json

register_v1 = Blueprint('register_v1', __name__)

@register_v1.route("/interests", methods=["GET"])
@produces("application/json")
def get_interests():
    """Get a list of all Interests."""

    results = []

    spatial_unit_id = request.args.get('spatial_unit_id')
    ba_unit_id = request.args.get('ba_unit_id')

    query_result = Interest.query.all()

    for item in query_result:
        results.append(item.as_dict())

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

@register_v1.route("/spatial_units", methods=["GET"])
@produces("application/json")
def get_spatial_units():
    """Get a list of all SpatialUnits."""

    results = []

    query_result = SpatialUnit.query.all()

    for item in query_result:
        results.append(item.as_dict())

    return Response(response=json.dumps(results, sort_keys=True, separators=(',', ':')),
                    mimetype='application/json',
                    status=200)
