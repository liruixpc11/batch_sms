import logging.config
import sys


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, stream=sys.stdout)

    from bsms.main import main
    import logging
    LOG = logging.getLogger(__name__)
    try:
        main('号码列表.xlsx', '短信模板.txt')
    except Exception as ex:
        LOG.exception(str(ex))
