from odoo import models, fields

class TodoTask(models.Model):
    _name = 'todo.task'
    _description = 'To-Do Task'

    name = fields.Char('Nom', required=True)
    description = fields.Char('Description', required=True)
    is_done = fields.Boolean('Faite?')
    active = fields.Boolean('Active?', default=True)
    dead_line = fields.Datetime('Date limite')
    priority = fields.Selection([
    ('high', 'Haute Priorité'),  
    ('normal', 'Priorité Normale'),
    ('low', 'Basse Priorité'),
    ], string='Niveau de Priorité', default='normal')
    employe_id = fields.Many2one('todo_app.employe', string='Assigned to Employee')
    projet_id = fields.Many2one('todo_app.projet', string='Projet')


