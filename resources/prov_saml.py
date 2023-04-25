import tableauserverclient as TSC
import time

create_n = 311
tableau_auth = TSC.PersonalAccessTokenAuth('test', 'tYcCcpGYTS2Yk2IUP3NG+w==:LEjZc0t5TzygWfBvA7LL1qZNHHqg7sMl', site_id='embeddedhot')
server = TSC.Server('https://eu-west-1a.online.tableau.com/', use_server_version=True)

with server.auth.sign_in(tableau_auth):
    print('Signed In OK')

    for i in range(1, create_n):
        print(i)
        #USERS
        #create new external viewer on site
        user_to_add = 'ext' + str(i) + '@mytc23.com'
        print(user_to_add)
        tableau_user = TSC.UserItem(user_to_add, 'Viewer',auth_setting='TableauIDWithMFA')
        tableau_user = server.users.add(tableau_user)
        #create the saml user as the internal admin/creator
        user_to_add = 'user' + str(i) + '@embeddedhot.com'
        print(user_to_add)
        tableau_user = TSC.UserItem(user_to_add, 'SiteAdministratorCreator',auth_setting='SAML')
        tableau_user = server.users.add(tableau_user)
        user_id = tableau_user.id
        #PROJECTS
        project_name = 'user' + str(i)
        print(project_name)
        new_project = TSC.ProjectItem(name=project_name)
        #create the project
        new_project = server.projects.create(new_project)
        proj_id = new_project.id
        #WORKBOOKS
        #upload redirect workbook
        wb_name = 'redirect_user' + str(i)
        new_workbook = TSC.WorkbookItem(name=wb_name, project_id=proj_id)
        new_workbook = server.workbooks.publish(new_workbook, "redirect_userxxx.twbx",mode=TSC.Server.PublishMode.Overwrite)
        wb_id=new_workbook.id
        #update owner of workbook to user
        new_workbook.owner_id = user_id
        new_workbook = server.workbooks.update(new_workbook)
        #upload main workbook
        wb_name = 'workbook_user' + str(i)
        new_workbook = TSC.WorkbookItem(name=wb_name, project_id=proj_id)
        new_workbook = server.workbooks.publish(new_workbook, "workbook_userxxx.twbx",mode=TSC.Server.PublishMode.Overwrite)
        wb_id=new_workbook.id
        #update owner of workbook to user
        new_workbook.owner_id = user_id
        new_workbook = server.workbooks.update(new_workbook)