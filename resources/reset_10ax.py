import tableauserverclient as TSC
remove_n = 11
tableau_auth = TSC.PersonalAccessTokenAuth('test', 'xlbwooeXRm23P68e//nk5g==:PbAvGKUEsA8nOR5BYnTUJUPWEK2XSfXF', site_id='twiki')
server = TSC.Server('https://10ax.online.tableau.com/', use_server_version=True)
all_users = ''
with server.auth.sign_in(tableau_auth):
    print('Signed In OK')
    
    #projects
    for i in range(1,remove_n):
        proj_to_remove = 'user' + str(i)
        print(proj_to_remove)

        req_option = TSC.RequestOptions()
        req_option.filter.add(TSC.Filter(TSC.RequestOptions.Field.Name,
                                 TSC.RequestOptions.Operator.Equals,
                                 proj_to_remove))
        all_projects, pagination_item = server.projects.get(req_options=req_option)
        num_projects = pagination_item.total_available
        if num_projects == 1:
            #projects exists delete them
            print(all_projects[0].id)
            server.projects.delete(all_projects[0].id)

        else:
            print('projects Not Found')

    # users
    for i in range(1,remove_n):
        user_to_remove = 'user' + str(i) + '@hot20.com'
        print(user_to_remove)

        req_option = TSC.RequestOptions()
        req_option.filter.add(TSC.Filter(TSC.RequestOptions.Field.Name,
                                 TSC.RequestOptions.Operator.Equals,
                                 user_to_remove))
        all_users, pagination_item = server.users.get(req_options=req_option)
        num_users = pagination_item.total_available
        if num_users == 1:
            #user exists delete them
            print(all_users[0].id)
            server.users.remove(all_users[0].id)

        else:
            print('User Not Found')
        user_to_remove = 'ext' + str(i) + '@hot20.com'
        print(user_to_remove)

        req_option = TSC.RequestOptions()
        req_option.filter.add(TSC.Filter(TSC.RequestOptions.Field.Name,
                                 TSC.RequestOptions.Operator.Equals,
                                 user_to_remove))
        all_users, pagination_item = server.users.get(req_options=req_option)
        num_users = pagination_item.total_available
        if num_users == 1:
            #user exists delete them
            print(all_users[0].id)
            server.users.remove(all_users[0].id)

        else:
            print('User Not Found')
    