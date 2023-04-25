import tableauserverclient as TSC
import time

create_n = 3
tableau_auth = TSC.PersonalAccessTokenAuth('test', 'xlbwooeXRm23P68e//nk5g==:PbAvGKUEsA8nOR5BYnTUJUPWEK2XSfXF', site_id='twiki')
server = TSC.Server('https://10ax.online.tableau.com/', use_server_version=True)

with server.auth.sign_in(tableau_auth):
    print('Signed In OK')

    for i in range(1, create_n):
        print(i)
        #create new external viewer on site
        test = input("test wait ")
        user_to_add = 'ext' + str(i) + '@hot20.com'
        print(user_to_add)
        tableau_user = TSC.UserItem(user_to_add, 'Viewer',auth_setting='ServerDefault')
        tableau_user = server.users.add(tableau_user)
        user_to_add = 'twiki.like.it+user' + str(i) + '@gmail.com'
        print(user_to_add)
        tableau_user = TSC.UserItem(user_to_add, 'SiteAdministratorCreator',auth_setting='ServerDefault')
        tableau_user = server.users.add(tableau_user)
        user_id = tableau_user.id
        test = input("check email")
        tableau_user.email = 'user' + str(i) + '@hot20.com'
        tableau_user = server.users.update(tableau_user)
        # read new user id
        # req_option = TSC.RequestOptions()
        # req_option.filter.add(TSC.Filter(TSC.RequestOptions.Field.Name,
        #                          TSC.RequestOptions.Operator.Equals,
        #                          user_to_add))
        # all_users, pagination_item = server.users.get(req_options=req_option)
        # num_users = pagination_item.total_available
        # if num_users == 1:
        #     #user exists (phew!) get the id
        #     print(all_users[0].id)
        #     user_id = all_users[0].id
        # else:
        #     print('User '+ user_to_add + ' Not Found - eek!')
        #     exit()
        # create project item
        project_name = 'user' + str(i)
        print(project_name)
        new_project = TSC.ProjectItem(name=project_name)
        # create the project
        new_project = server.projects.create(new_project)
        proj_id = new_project.id
        # read new project id
        # req_option = TSC.RequestOptions()
        # req_option.filter.add(TSC.Filter(TSC.RequestOptions.Field.Name,
        #                          TSC.RequestOptions.Operator.Equals,
        #                          project_name))
        # all_projects, pagination_item = server.projects.get(req_options=req_option)
        # num_projects = pagination_item.total_available
        # if num_projects == 1:
        #     #project exists (phew!) get the id
        #     print(all_projects[0].id)
        #     proj_id = all_projects[0].id
        # else:
        #     print('User '+ project_name + ' Not Found - eek!')
        #     exit()
        # upload redirect workbook
        wb_name = 'redirect_user' + str(i)
        new_workbook = TSC.WorkbookItem(name=wb_name, project_id=proj_id)
        new_workbook = server.workbooks.publish(new_workbook, "redirect_userxxx.twbx",
                                                     mode=TSC.Server.PublishMode.Overwrite,
                                                     hidden_views=['Sheet 1'])
        wb_id=new_workbook.id
        new_workbook.owner_id = user_id
        new_workbook.hidden_views=['Sheet 1']
        new_workbook = server.workbooks.update(new_workbook)
        # upload main workbook
        wb_name = 'workbook_user' + str(i)
        new_workbook = TSC.WorkbookItem(name=wb_name, project_id=proj_id)
        new_workbook = server.workbooks.publish(new_workbook, "workbook_userxxx.twbx",
                                                     mode=TSC.Server.PublishMode.Overwrite
                                                     )
        wb_id=new_workbook.id
        new_workbook.owner_id = user_id
        #new_workbook.hidden_views=['Sheet 1']
        new_workbook = server.workbooks.update(new_workbook)