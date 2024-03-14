from flask import Flask, Blueprint, request
from application.common import route, ResMsg, ResponseCode
from application.extensions.requirment2.suggestion import get_matching_attributes
from application.extensions import get_suggestion

suggest_bp = Blueprint('suggest', __name__, url_prefix='/suggest')


@route(suggest_bp, '/', methods=['GET', 'POST'])
def suggest():
    if request.method == 'GET':
        return {"message": "suggest"}, 200
    else:
        business_id = request.form['business_id']
        business_df, res = get_matching_attributes(business_id)
        business_df = business_df.first().asDict()
        suggest = get_suggestion(business_df, res)
        response = ResMsg(code=ResponseCode.SUCCESS,
                          data=dict(result=res, advice=suggest))
        return response.data
