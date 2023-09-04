class FacetedParticleUndefined(ValueError):
    def __init__(
        self,
        msg="Faceted particle requires 3 facets defined (100, 110, 111)",
        *args,
        **kwargs
    ):
        super().__init__(msg, *args, **kwargs)


class VoronoiNotSelected(ValueError):
    pass
