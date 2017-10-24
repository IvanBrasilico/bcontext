import logging.config
from bottery.app import App
from bottery.log import DEFAULT_LOGGING
import botteryext.bcontext.localizations
from botteryext.bcontext.contexthandler import ContextHandler


app = App()
ch = ContextHandler(app)

if __name__ == '__main__':
    logging.config.dictConfig(DEFAULT_LOGGING)
    logger = logging.getLogger('bottery')
    logger.setLevel(logging.DEBUG)

    app.run()
