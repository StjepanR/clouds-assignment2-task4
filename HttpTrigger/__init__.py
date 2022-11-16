import logging
import azure.functions as func

from integration import compute, compute_all

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    lower = req.route_params.get("lower")    
    upper = req.route_params.get("upper")

    if not lower or not upper:
        return func.HttpResponse("Method not found\nParameters upper or lower are not specified", status_code=404)
    
    try:
        lower = float(lower)
        upper = float(upper)
    except:
        return func.HttpResponse("Method not found\nParameters upper or lower are in wrong format", status_code=404)

    return func.HttpResponse(", ".join([str(x) for x in compute_all(lower=lower, upper=upper)]), status_code=200)
