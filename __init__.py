from trytond.pool import Pool
from .convenio import Convenio

def register():
    Pool.register(
        Convenio,
        module='convenios', type_='model'
    )
