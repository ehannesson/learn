# fields.py


import numpy as np


class ExerciseField:
    """
    Class representing a parameter field of an Exercise.

    Parameters
    ----------
    field : str
    gen_func : callable **kwargs --> ndarray
    **kwargs

    Attributes
    ----------

    Methods
    -------
    """

    def __init__(self, field, gen_func=None, values=None, **kwargs):

        self.field = field
        self.gen_func = gen_func
        self.values = values
        self.kwargs = kwargs

    def generate_field_values(self):
        """
        Generate and return field values. If field values have already been
        generated, return those.
        """

        if self.values is None:
            self.values = self.gen_func(**self.kwargs)

        return self.values

    def fill_exercise_with_values(self, outline: str) -> str:
        """
        Fill in Exercise statement with field values.

        Parameters
        ----------
        outline : str
            Exercise statement outline. Fields to be filled must be of the form
            '__field#__'.

        Returns
        -------
        outline : str
            Exercise outline with associated field placeholders replaced by
            field values.
        """

        for i in range(self.values.size):
            outline = outline.replace(f'__{self.field}{i}__', str(self.values[i]))

        return outline

    def new_instance(self):
        """Create a duplicate ExerciseField object with self.values reset."""
        return self.__class__(field=self.field, gen_func=self.gen_func, **self.kwargs)


class IntegerField(ExerciseField):

    def __init__(
        self,
        low=1,
        high=10,
        size=2,
        p=None,
        field='val',
        **kwargs
    ):

        super().__init__(field, **kwargs)
        self._set_gen_func(low, high, size, p)

    def _set_gen_func(self, low, high, size, p) -> None:
        """TODO"""
        # if distribution `p` not specified, draw uniformly using `integers`
        if p is None:
            self.gen_func = np.random.default_rng().integers
            self.kwargs.update({'low': low, 'high': high, 'size': size})
        # otherwise, we combine `arange` with `choice` to draw non-uniformly
        else:
            def _choice(**kwargs):
                vals = np.arange(low, high)
                return np.random.default_rng().choice(vals, replace=True, **kwargs)

            self.gen_func = _choice
            self.kwargs.update({'size': size, 'p': p})
