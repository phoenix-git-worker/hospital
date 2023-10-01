import logging

from odoo import models, fields, api, exceptions, _

_logger = logging.getLogger(__name__)


class HospitalDoctor(models.Model):
    _name = 'kw.hospital.doctor'
    _description = 'Kw Hospital Doctor model'
    
    kw_name = fields.Char('Name')
