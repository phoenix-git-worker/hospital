import logging

from odoo import models, fields, api, exceptions, _

_logger = logging.getLogger(__name__)


class KwHospitalPatient(models.Model):
    _name = 'kw.hospital.patient'
    _description = 'Kw Hospital Patient'

    kw_name = fields.Char('Name')
