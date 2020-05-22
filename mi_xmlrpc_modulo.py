import xmlrpc.client

url = 'http://192.168.1.80:8069'
db = 'loanbooks'
username = 'admin'
password = 'admin'

#info = xmlrpc.client.ServerProxy('http://192.168.1.80:8069/start').start()
#url, db, username, password = \
#    info['host'], info['database'], info['user'], info['password']

common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
print(common.version())
uid = common.authenticate(db, username, password, {})

print(uid)

models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))
print(models.execute_kw(db, uid, password,
    'res.partner', 'check_access_rights',
    ['read'], {'raise_exception': False}))

#
ids = models.execute_kw(db, uid, password,
    'res.partner', 'search',
    [[['is_company', '=', True]]])
print(ids)
print("Voy por los registros")
for id in ids:
  [registro] = models.execute_kw(db, uid, password,
  'res.partner', 'read', [id],{'fields': ['name', 'country_id', 'comment','student_value']})
  print(registro)

# if ids:


    # registros=models.execute_kw(db, uid, password,
    # 'res.partner', 'read',
    # [ids], {'fields': ['name', 'country_id', 'comment','student_value']})
    # for registro in registros:
    #    print(registro)
