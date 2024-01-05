import os
import json
import logging.config

logging.config.fileConfig(os.path.dirname(__file__)+'/logging.ini', disable_existing_loggers=False)

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

async def log_request(request, status_code, process_time):
    path = request.url.path
    if request.query_params:
        path += f"?{request.query_params}"
    message = {
        'request':f'{request.method} {path}',
        'response':{
            'status_code':status_code,
            'time': process_time
        }
    }
    logger.info('\n'+json.dumps(message, indent=2))
