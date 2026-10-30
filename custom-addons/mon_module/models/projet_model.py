from odoo import models, fields

class Projet(models.Model):
    _name = 'todo_app.projet' 
    _description = 'Projet'

    name = fields.Char('Nom', required=True)
    description = fields.Char('Description', required=True)
    date_debut = fields.Date("Date de Début", required=True)
    date_fin = fields.Date("Date de Fin", required=True)
    document = fields.Binary('Cahier de Charge')
    image = fields.Binary('Image')
    employe_ids = fields.Many2many('todo_app.employe', string='Employés')
    task_ids = fields.One2many('todo.task', 'projet_id', string='Tasks')
