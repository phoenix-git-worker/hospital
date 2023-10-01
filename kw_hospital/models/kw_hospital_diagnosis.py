import logging

from odoo import models, fields, api, exceptions, _

_logger = logging.getLogger(__name__)


class HospitalDiagnosis(models.Model):
    _name = 'kw.hospital.diagnosis'
    _description = 'Hospital diagnosis model'

    kw_name = fields.Char('Name')