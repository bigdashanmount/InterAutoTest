import os
import pytest

from common import Base
from config import Conf

if __name__ == '__main__':
    #���Ա���·��
    report_path = Conf.get_report_path()+os.sep+"result"
    print(report_path)
    #����洢·��
    report_html_path = Conf.get_report_path()+os.sep+"html"
    #print(report_html_path)
    pytest.main(["-s","--alluredir",report_path])
    #Base.send_mail()



