# user.py


class User:
    """
    Class representing an user.

    Parameters
    ----------
    TODO

    Attributes
    ----------

    Methods
    -------
    """

    def __init__(self, name, uuid=None):
        self.name = name
        self.uuid = self._get_uuid(uuid)



    def _get_uuid(self, uuid):
        """
        Get or create universally-unique identifier for user.

        A UUID is generated only when the user is first created; otherwise,
        this function returns the existing UUID.
        """
        if uuid is None:
            # TODO : create UUID function
            pass

        return uuid



# exercise statistics DB table
# date uuid ex_type_id ex_values user_solution actual_solution is_correct ex_time ex_level ex_subject ex_concepts user_mastery
