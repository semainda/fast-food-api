"""Module that creates role model"""
# local imports
from ..models import BaseModel


class Role(BaseModel):
    """
    Class that represents a role

    The following attributes of a role are stored in this table:
        role id
        role name
    """
    def __init__(self):
        super().__init__()

    def create_role(self, role_name):
        """Method that create role"""
        sql = "INSERT INTO roles(role_name) VALUES(%s) RETURNING role_name;"
        return self.cud_operations(sql, (role_name, ))

    def get_role_by_id(self, role_id):
        """Method that returns a specific role"""
        sql = "SELECT role_name FROM roles WHERE role_id=%s;"
        return self.cud_operations(sql, (role_id,))

    def get_role_by_name(self, role_name):
        """Method that returns a specific role"""
        sql = "SELECT role_id FROM roles WHERE role_name=%s;"
        return self.cud_operations(sql, (role_name,))

    def get_all_roles(self):
        """Method that returns a list of roles"""
        sql = "SELECT * FROM roles;"
        rows = self.read_items(sql)
        roles = []
        for _, items in enumerate(rows):
            role_id, role_name = items
            role = dict(
                Id=role_id,
                Name=role_name.upper()
            )
            roles.append(role)
        return roles

    def update_role(self, role_name, role_id):
        """Method that update specific role"""
        sql = "UPDATE roles SET role_name=(%s)\
            WHERE role_id=(%s) RETURNING role_name;"
        return self.cud_operations(sql, (role_name, role_id))

    def delete_role(self, role_id):
        """Method that delete specific role"""
        sql = "DELETE FROM roles WHERE role_id=(%s) RETURNING role_name CASCADE;"
        return self.cud_operations(sql, (role_id,))
    
    def get_user_roles(self):
        sql = """SELECT u.user_id,u.user_name, r.role_id, r.role_name
                    FROM users u, user_roles s, roles r 
                    WHERE u.user_id=s.user_id AND r.role_id=s.role_id;"""
        rows = self.read_items(sql)
        user_roles = []
        for _, role_items in enumerate(rows):
            user_id, user_name, role_id, role_name = role_items
            user = dict(
                user_id=user_id,
                user_name=user_name,
                role_id=role_id,
                role_name=role_name
            )
            user_roles.append(user)
        return user_roles
    
    def update_user_roles(self, role_id, user_id):
        sql = """UPDATE user_roles SET role_id=%s WHERE user_id=%s RETURNING role_id"""
        return self.cud_operations(sql, (role_id, user_id))

