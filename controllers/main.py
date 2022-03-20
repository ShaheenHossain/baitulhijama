from odoo import http
from odoo.http import request
from datetime import datetime


class baitulhijama(http.Controller):

    @http.route('/web/bhf', type='http', website=True, auth='public')
    def hospital_signup(self, **kw):
        return request.render("baitulhijama.bhf", {})

    @http.route('/create/bhf/', type='http', website=True, auth='public')
    def create_partner(self, **kw):
        now = datetime.now()
        priority = ''
        bhf_val = {

            'name': kw.get('name'),
            'patient_age': kw.get('patient_age'),
            'marital_status': kw.get('marital_status'),
            'father_name': kw.get('father_name'),
            'mother_name': kw.get('mother_name'),
            'mobile': kw.get('mobile'),
            'email': kw.get('email'),
            'address': kw.get('address'),
            'ticket_no': 'BHF-' + now.strftime('%Y') + '-',
            'ques_01': kw.get('ques_01'),
            'ques_02': kw.get('ques_02'),
            'ques_03': kw.get('ques_03'),
            'ques_04': kw.get('ques_04'),
            'ques_05': kw.get('ques_05'),
            'ques_06': kw.get('ques_06'),
            'ques_07': kw.get('ques_07'),
            'ques_08': kw.get('ques_08'),
            'ques_09': kw.get('ques_09'),
            'ques_10': kw.get('ques_10'),
            'ques_11': kw.get('ques_11'),
            'ques_12': kw.get('ques_12'),
            'ques_13': kw.get('ques_13'),
            'ques_14': kw.get('ques_14'),
            'ques_15': kw.get('ques_15'),
            'ques_16': kw.get('ques_16'),
            'ques_17': kw.get('ques_17'),
            'ques_18': kw.get('ques_18'),
            'ques_19': kw.get('ques_19'),
            'ques_20': kw.get('ques_20'),
            'ques_21': kw.get('ques_21'),
            'ques_22': kw.get('ques_22'),
            'ques_23': kw.get('ques_23'),
            'ques_24': kw.get('ques_24'),
            'ques_25': kw.get('ques_25'),
            'ques_26': kw.get('ques_26'),
            'ques_27': kw.get('ques_27'),
            'ques_28': kw.get('ques_28'),
            'ques_29': kw.get('ques_29'),
            'ques_30': kw.get('ques_30'),
            'ques_31': kw.get('ques_31'),
            'ques_32': kw.get('ques_32'),
            'ques_33': kw.get('ques_33'),
            'ques_34': kw.get('ques_34'),
            'ques_35': kw.get('ques_35'),
            'other_problems': kw.get('other_problems'),
            'promising_true': kw.get('promising_true'),
            'payment_method': kw.get('payment_method'),
            'payment_transactionid': kw.get('payment_transactionid'),
        }

        print("BHF Values_01:", bhf_val)

        ticket_id: any = request.env['crm.bhf'].sudo().create(bhf_val)
        return request.render("baitulhijama.ticket_welcome", {
            'ticket_no': 'BHF-' + now.strftime('%Y') + '-' + str(ticket_id[0].id),
            'name': kw.get('name'),
            'patient_age': kw.get('patient_age'),
            'marital_status': kw.get('marital_status'),
            'father_name': kw.get('father_name'),
            'mother_name': kw.get('mother_name'),
            'mobile': kw.get('mobile'),
            'email': kw.get('email'),
            'address': kw.get('address'),
            'ticket_no': 'BHF-' + now.strftime('%Y') + '-',
            'ques_01': kw.get('ques_01'),
            'ques_02': kw.get('ques_02'),
            'ques_03': kw.get('ques_03'),
            'ques_04': kw.get('ques_04'),
            'ques_05': kw.get('ques_05'),
            'ques_06': kw.get('ques_06'),
            'ques_07': kw.get('ques_07'),
            'ques_08': kw.get('ques_08'),
            'ques_09': kw.get('ques_09'),
            'ques_10': kw.get('ques_10'),
            'ques_11': kw.get('ques_11'),
            'ques_12': kw.get('ques_12'),
            'ques_13': kw.get('ques_13'),
            'ques_14': kw.get('ques_14'),
            'ques_15': kw.get('ques_15'),
            'ques_16': kw.get('ques_16'),
            'ques_17': kw.get('ques_17'),
            'ques_18': kw.get('ques_18'),
            'ques_19': kw.get('ques_19'),
            'ques_20': kw.get('ques_20'),
            'ques_21': kw.get('ques_21'),
            'ques_22': kw.get('ques_22'),
            'ques_23': kw.get('ques_23'),
            'ques_24': kw.get('ques_24'),
            'ques_25': kw.get('ques_25'),
            'ques_26': kw.get('ques_26'),
            'ques_27': kw.get('ques_27'),
            'ques_28': kw.get('ques_28'),
            'ques_29': kw.get('ques_29'),
            'ques_30': kw.get('ques_30'),
            'ques_31': kw.get('ques_31'),
            'ques_32': kw.get('ques_32'),
            'ques_33': kw.get('ques_33'),
            'ques_34': kw.get('ques_34'),
            'ques_35': kw.get('ques_35'),
            'other_problems': kw.get('other_problems'),
            'promising_true': kw.get('promising_true'),
            'payment_method': kw.get('payment_method'),
            'payment_transactionid': kw.get('payment_transactionid'),

        })