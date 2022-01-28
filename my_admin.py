from admin import Admin


adm = Admin('Max', 'Churikov', 21, 'Melitopol')
adm.privileges.privileg = ['может добавить сообщение', 'может удалить сообщение'
    , "может заблокировать пользователя"]
adm.describe_user()
adm.privileges.show_privileges()