{
    'name': 'Hospital management system',
    'sequence': -3,
    'data': [
        'security/ir.model.access.csv',
        'data/hospital_patient_data.xml',
        'data/hospital.patient.csv',
        'wizard/cancel_appointment.xml',
        'views/menu.xml',
        'views/patient.xml',
        'views/appointment.xml',
    ],
    'depends': ["product"],
    'application': True,
}
