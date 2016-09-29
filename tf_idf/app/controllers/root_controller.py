class RootController(object):

    def index(self):
        return '''
            <ul>
                <li><a href="/calculations">Exercise #1: Calculations</a></li>
                <li><a href="/search">Exercise #2: Search</a></li>
            </ul>
        '''
