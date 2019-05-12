# main file for initializing the app
import os
import logging
import logging.config as logging_cfg
from pathlib import Path
from configparser import ConfigParser
from app import create_app


def main():
    # General app configuration

    # set root directory for the app
    root = Path('.') / os.getcwd()

    # setup configuration file path using the APP_ENV environment variable
    cfg_path = root / 'config' / '{}.ini'.format(os.environ.get('APP_ENV'))
    cfg_parser = ConfigParser()

    # read .ini file for the appropriate app setup (dev, prod or test)
    cfg = cfg_parser.read(cfg_path)

    # Logger configuration
    log_path = root / 'logs'

    # create logs directory if not present
    log_path.mkdir(mode=0o755, parents=True, exist_ok=True)

    # load the logger configuration from the configuration file
    logging_cfg.fileConfig(cfg_path, disable_existing_loggers=False)

    # initialize logger
    logger = logging.getLogger(__name__)

    # create app instance for dev, test or prod
    app = create_app(cfg)

    logger.info("Running app: " + (os.environ.get('APP_NAME') or "Anonymous App"))
    return True


if __name__ == "__main__":
    main()
