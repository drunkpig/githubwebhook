import subprocess
from configparser import ConfigParser
from logging.config import fileConfig
import hmac
from flask import Flask
from flask import request
import json, logging
from os import path

fileConfig("logging.ini")
logger = logging.getLogger()

app = Flask(__name__)


def __do_deploy():
    """
        部署
    """
    curdir = path.dirname(path.abspath(__file__))
    deploy_script_file = f"{curdir}/run.sh"
    cmd = f"/bin/bash  {deploy_script_file}"

    (status, output) = subprocess.getstatusoutput(cmd)
    return status, output


@app.route('/deploy', methods=['POST'])
def deploy():
    if request.headers.get('X-Hub-Signature') != 'wh0syourdaddy':
        logger.error("部署失败")
        return json.dumps({"success": False, "message": "accessKey error"})
    deploy_result = {}
    logger.info("开始部署")
    deploy_result['success'], deploy_result['message'] = __do_deploy()
    logger.info("部署成功")
    return json.dumps(deploy_result)


def main(port=50001):
    app.run(port=port)

