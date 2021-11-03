import sys

class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []
        groupList.append(self)

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

    def has_name(self):
        return self.name != None

def is_user_in_group(user, group):
    boolean = False
    if group in groupList:
        for userCheck in group.get_users():
            userList.append(userCheck)
        for groupCheck in group.get_groups():
            is_user_in_group(user, groupCheck)
        for userIndex in userList:
            if userIndex == user:
                boolean = True
    return boolean

global groupList
groupList = []

parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

sub_sub_child_user = "sub_sub_child_user"

child.add_group(sub_child)
parent.add_group(child)

global userList
userList = []

print(is_user_in_group(sub_child_user,child))
print(is_user_in_group(sub_child_user,sub_child))
print(is_user_in_group('',sub_child))
print(is_user_in_group('',''))
