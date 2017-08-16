#!/usr/bin/python 

from anisble.module_utils.basic imort *

def main()
	module = AnsibleModule(arguement_spec={})
	response = {"hello" : "World" }
	module.exit_json(changed=False, meta=response )


if __name__ == '__main__'
	main()