import sys
import os.path
# add `lib` subdirectory to `sys.path`, so our `main` module can load
# third-party libraries.

reload(sys)
sys.setdefaultencoding('utf-8')
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'lib'))
