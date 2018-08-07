import jenkins


def close(session_attributes, fulfillment_state, message):
    response = {
        'sessionAttributes': session_attributes,
        'dialogAction': {
            'type': 'Close',
            'fulfillmentState': fulfillment_state,
            'message': message
        }
    }
    print(response)
    return response


def lambda_handler(event, context):
    if event['currentIntent']['slots']['BuildName'] == "prod":
        server = jenkins.Jenkins('http://54.85.232.121:8080/', username='deloitteadmin', password='')
        last_build_number = server.get_job_info('deploy_pizza_to_prod_app_server')['lastCompletedBuild']['number']
        build_info = server.get_build_info('deploy_pizza_to_prod_app_server', last_build_number)
    data = "Build " + build_info['result']
    return close(event['sessionAttributes'], 'Fulfilled', {'contentType': 'PlainText', 'content': data})

if __name__ == '__main__':
    lambda_handler(event=None, context=None)