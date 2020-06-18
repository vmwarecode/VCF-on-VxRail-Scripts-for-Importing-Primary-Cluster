# Create WLD
import requests
import json
import sys
import time
import os

sys.path.append(os.path.abspath(__file__ + '/../../'))
from Utils.utils import Utils


class UpdateDomain:
    def __init__(self):
        print('Update Domain')
        self.utils = Utils(sys.argv)
        self.domain_id = sys.argv[1]
        self.hostname = sys.argv[2]

    def update_workload_domain(self):
        # validations
        payload = self.utils.read_input(os.path.abspath(__file__ + '/../') + '/update_domain_spec_vxrail.json')
        validations_url = 'https://' + self.hostname + '/v1/domains/' + self.domain_id + '/validations '
        print ('Validating the input....')
        response = self.utils.post_request(payload, validations_url)
        print ('Validatin started for domain. The valdidation id is: ' + response['id'])
        validate_poll_url = 'https://' + self.hostname + '/v1/domains/validations/' + response['id']
        print ('Polling on validation api ' + validate_poll_url)
        time.sleep(10)
        validation_status = self.utils.poll_on_id(validate_poll_url, False)
        print('Validate domain ended with status: ' + validation_status)
        if validation_status != 'SUCCEEDED':
            print ('Validation Failed.')
            exit(1)

        # Domain Update
        domain_creation_url = 'https://' + self.hostname + '/v1/domains/' + self.domain_id
        response = self.utils.patch_request(payload, domain_creation_url)
        print ('Updating Domain...')
        task_url = 'https://' + self.hostname + '/v1/tasks/' + response['id']
        print ("Domain creation task completed with status:  " + self.utils.poll_on_id(task_url, True))


if __name__ == "__main__":
    UpdateDomain().update_workload_domain()

