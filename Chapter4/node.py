class Node(object):
    def __init__(self, key):
        self.key = key
        self.lc = None
        self.rc = None

    def print_key(self):
        print '-' * 22
        print '  {0} '.format(self.key)

    def show(self):
        if self.lc and self.rc:
            self.print_key()
            self.show_both_children()
        elif self.lc:
            self.print_key()
            print ' /'
            print '{0}'.format(self.lc.key)
            self.lc.show()
        elif self.rc:
            self.print_key()
            print ' /  \\'
            print '     {0}'.format(self.rc.key)
            self.rc.show()

    def show_both_children(self):
        print ' /  \\'
        print '{0}    {1}'.format(self.lc.key, self.rc.key)
        self.lc.show()
        self.rc.show()

    def __str__(self):
        return self.key