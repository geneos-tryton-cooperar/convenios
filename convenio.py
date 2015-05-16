#-*- coding: utf-8 -*-
from trytond.model import ModelSQL, ModelView, fields

__all__ = ['Convenio']

class Convenio(ModelSQL, ModelView):
    "Convenio"
    __name__ = 'convenios.convenio'

    codigo =  fields.Char('Codigo', required=True)
    monto = fields.Float('Monto', (10,2), required=True)
    descripcion = fields.Char('Descripcion', size=None)
    tipo_convenio = fields.Selection([
    	('inaes', 'Inaes'),
		('cooperar', 'Cooperar')], 'Tipo de Convenio', select=True, required=True)

    cuenta_debito = fields.Many2One('account.account', 'Cuenta Debito', required=True,
        domain=[('kind', '=', 'receivable')])
    cuenta_credito = fields.Many2One('account.account', 'Cuenta Credito', required=True,
        domain=[('kind', '=', 'payable')])

   