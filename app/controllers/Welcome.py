from system.core.controller import *

class Welcome(Controller):
    def __init__(self, action):
        super(Welcome, self).__init__(action)
        """
            This is an example of loading a model.
            Every controller has access to the load_model method.

            self.load_model('WelcomeModel')
        """

    """ This is an example of a controller method that will load a view for the client """
    def index(self):
        """
        A loaded model is accessible through the models attribute
        self.models['WelcomeModel'].get_all_users()
        """
        return self.load_view('index.html')
