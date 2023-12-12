# each muse is a new object
class MConfessionLog:
    author_key = ''
    confessions = []

    def __str__(self):
        return f"{self.author_key}, {self.confessions}"

    def __init__(self,user, content):
        self.author_key = user
        self.confessions.append(content)
        print('user has been created')
        print(self.confessions)

    def add_entry_content(self, content):
        print(content)
        self.confessions.append(content)
        print(self.confessions)