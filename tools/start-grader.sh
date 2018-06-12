#!/bin/bash

myconf=$PWD/configs
conf=/etc/jupyter

#  -v $myconf/jupyter_notebook_config.designer.py:$conf/jupyter_notebook_config.py \
docker run --rm -it --name grader \
  -v $myconf/nbgrader_config.py:$conf/nbgrader_config.py \
  -v nbhub_exchange_inbound_albert.einstein:/submissions/albert.einstein \
  -v nbhub_exchange_inbound_jack.bauer:/submissions/jack.bauer \
  -v nbhub_exchange_outbound:/exchange/course/outbound \
  -v nbhub_course:/course:rw \
  -v $PWD/grader_tools:/home/jovyan/tools \
  -p 9999:8888 \
  nbhub/designer /bin/bash
