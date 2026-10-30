from odoo import models, fields

class Employe(models.Model):
    _name = 'todo_app.employe'
    _description = 'Employé'

    name = fields.Char('Nom', required=True)
    num_tele = fields.Char('Numéro de Téléphone', required=True)
    depart = fields.Char('Département', required=True)
    date_entre = fields.Date("Date d'éntre", required=True)
    email = fields.Char('Email', required=True)
    projet_id = fields.Many2many('todo_app.projet', string='Projet')
    task_ids = fields.One2many('todo.task', 'employe_id', string='Tache')
