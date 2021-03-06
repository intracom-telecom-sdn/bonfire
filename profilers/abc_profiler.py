import abc
import logging
import os

class ABCProfiler(object):
    __metaclass__ = abc.ABCMeta
    def __init__(self, opts):
        self.opts = opts

    @abc.abstractmethod
    def setup_env(self, env):
        if env == "karaf":
            self.setup_karaf_env()
        else:
            self.setup_java_env()

    @abc.abstractmethod
    def setup_java_opts(self):
        join_opts = ' '.join(self.opts['env']['JAVA_OPTS'])
        export_jo = 'export JAVA_OPTS="$JAVA_OPTS {0}"'.format(join_opts)
        logging.debug("[JAVA OPTS] " + export_jo)
        return export_jo

    @abc.abstractmethod
    def setup_java_env(self):
        os.environ['JAVA_OPTS'] = ' '.join(self.opts['java_opts'])
        return os.environ['JAVA_OPTS']

    @abc.abstractmethod
    def setup_karaf_env(self):
        logging.debug('changing karaf env')
        with open(self.opts['env']['KARAF_HOME'] + '/bin/setenv', 'a') as setenv:
            print(self.opts['env']['KARAF_HOME'] + '/bin/setenv')
            env_opts = self.setup_java_opts()
            logging.debug('writing ' + env_opts)
            setenv.write(env_opts + '\n')

    @abc.abstractmethod
    def start(self):
        return

    @abc.abstractmethod
    def stop(self):
        return

    @abc.abstractmethod
    def generate_flamegraph(self, in_file, flamegraph_name):
        return


