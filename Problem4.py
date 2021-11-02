import sys

class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name

def is_user_in_group(user, group):
    boolean = False
    for _ in group.get_users():
        if user == _:
            boolean = True
    return boolean

parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

sub_sub_child_user = "sub_sub_child_user"

child.add_group(sub_child)
parent.add_group(child)

print(is_user_in_group(sub_child_user,sub_child))
print(is_user_in_group(sub_child_user,child))
print(is_user_in_group('',child))
print(is_user_in_group(sub_sub_child_user,child))
