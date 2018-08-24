# -*- coding: utf-8 -*-
# shared logger
# ganben
import logging

### set up logging
def gen_logger(self, name):

    logger = logging.getLogger('%s' % name)
    logger.setLevel(logging.DEBUG)

    # fh
    fh = logging.FileHandler('%s.log' % name)
    fh.setLevel(logging.DEBUG)
    # ch
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s -%(message)s')
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)
    logger.addHandler(fh)
    logger.addHandler(ch)
    return logger
